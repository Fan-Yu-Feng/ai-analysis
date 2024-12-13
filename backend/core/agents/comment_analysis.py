import asyncio
import json

import pandas as pd
from backend.core.llms.openai_wrapper import openai_llm as llm
# from core.llms.siliconflow_wrapper import sfa_llm
from loguru import logger
from backend.core.utils.pb_api import PbTalker
import os
from datetime import datetime
from urllib.parse import urlparse

from backend.core.utils.general_utils import get_logger


class GeneralAnalysisInfoExtractor:
    def __init__(self, _logger: logger) -> None:
        self.logger = _logger
        # self.model = os.environ.get("PRIMARY_MODEL","qwen2:7b")  # better to use "Qwen/Qwen2.5-14B-Instruct"
        # self.model = os.environ.get("PRIMARY_MODEL", "moonshot-v1-8k")  # better to use "Qwen/Qwen2.5-14B-Instruct"
        self.model = os.environ.get("PRIMARY_MODEL", "qwen2.5:14b")  # better to use "Qwen/Qwen2.5-14B-Instruct"
        self.secondary_model = os.environ.get("SECONDARY_MODEL", "THUDM/glm-4-9b-chat")

        self.get_info_prompt = f'''作为评论分析助手，我将会给你视频营销内容下方的评论数据，你的任务是从给定的多条评论文本中提取以下信息：
1. 情感倾向，为枚举数据：只包含正面、负面、中性
2. 主要主题
3. 关键词
4. 归纳总结，为枚举数据：对产品的看法，对营销手段的评论，表达向往，表达讽刺，其他。
5. 原始评论内容：提供的原始评论数据，不得修改，直接使用对应的原文文本。

请遵循以下原则进行信息提取：

- 理解每个评论的内容，确保提取的信息准确。
- 无论原文是什么语言，请使用中文输出提取结果。
- 每条评论都带有 id，在返回总结时需要提供对应的 id，如果评论中不含 id，则不需要分析。
- 请忽略评论文本中的不必要空格和换行符。'''
        self.get_info_suffix = '''如果评论文本中包含相关信息，请按以下JSON格式输出提取的信息：
[{"id":"提供的 id","sentiment": "情感倾向", "topic": "主要主题", "keywords": ["关键词1", "关键词2", ...], "summary": "对产品的看法|对营销手段的评论|表达向往|表达讽刺|其他。","comment":"原始评论内容，不得修改"}]

示例：
[{"id":"1234","sentiment": "正面", "topic": "服务质量", "keywords": ["友好", "快速"], "summary": "表达向往", "comment": "服务速度快、质量好，工作人员很友好"}, {"id":"1235","sentiment": "负面", "topic": "产品质量", "keywords": ["破损"], "summary": "表达讽刺","comment":"产品质量太差，破损严重"}]
如果评论文本中不包含任何相关信息，请输出：[]。'''

    async def get_anlalysis_res(self, text: str) -> list[dict]:

        if not text:
            return []
        content = f'评论内容：{text}\n\n{self.get_info_suffix}'
        message = [{'role': 'system', 'content': self.get_info_prompt}, {'role': 'user', 'content': content}]
        result = await llm(message,
                           model=self.model, temperature=0.1
                           # , response_format={"type": "json_object"}
                           )
        self.logger.debug(f'input : {message}\n get_info llm output:\n{result}')
        if not result:
            return []
        # result = json_repair.repair_json(result, return_objects=True)
        print("get analysis result" + result)
        if not isinstance(result, list):
            self.logger.warning("failed to parse from llm output")
            return []
        if not result:
            self.logger.debug("no info found")
            return []
        # 业务数据清洗
        return result

    async def __call__(self, text: str, link_dict: dict, base_url: str, author: str = None, publish_date: str = None) -> \
            tuple[list, set, str, str]:
        if not author and not publish_date and text:
            author, publish_date = await self.get_author_and_publish_date(text)

        if not author or author.lower() == 'na':
            author = urlparse(base_url).netloc

        if not publish_date or publish_date.lower() == 'na':
            publish_date = datetime.now().strftime('%Y-%m-%d')

        related_urls = await self.get_more_related_urls(link_dict, base_url)

        info_prefix = f"//{author} {publish_date}//"
        lines = text.split('\n')
        text = ''
        infos = []
        for line in lines:
            text = f'{text}{line}'
            if len(text) > 2048:
                cache = await self.get_info(text, info_prefix, link_dict)
                infos.extend(cache)
                text = ''
        if text:
            cache = await self.get_info(text, info_prefix, link_dict)
            infos.extend(cache)

        return infos, related_urls, author, publish_date


def read_comments_from_excel(file_path: str) -> list[dict]:
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Convert DataFrame to a list of dictionaries
        comments = []
        for _, row in df.iterrows():
            # 根据逗号分割
            commentInfo = row[0].split('.')
            comments.append({"id": commentInfo[0], "comment": commentInfo[1]})

        return comments
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    comments = read_comments_from_excel('/Users/yohong/code/DR/ai-comment-analysis/backend/core/agents/comments.xlsx')

    async def main():
        project_dir = os.environ.get("PROJECT_DIR", "/Users/yohong/code/yohong/wiseflow")
        wiseflow_logger = get_logger('general_process', project_dir)
        gie = GeneralAnalysisInfoExtractor(wiseflow_logger)
        # comment_list = json.loads(comment)

        # 每 10 个 comment 拼接为 str 然后调用一次接口
        results = []
        res = await gie.get_anlalysis_res(comments)
        results.extend(res)
        print(res)


    # 读取 comments.xlsx 文件，获取数据，文本分割，第一个为 id 第二个为 comment 生成 json 格式为 [{"id": 123, "comment": "comment"}]
    asyncio.run(main())
