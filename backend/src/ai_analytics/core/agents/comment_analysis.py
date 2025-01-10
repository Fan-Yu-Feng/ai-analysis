import asyncio
import json

import pandas as pd
from ai_analytics.core.llms.openai_wrapper import openai_llm as llm

from ai_analytics.common.log import logger
import os
from datetime import datetime
from urllib.parse import urlparse


class GeneralAnalysisInfoExtractor:
    def __init__(self, system_prompt: str, user_prompt: str ) -> None:
        self.model = os.environ.get("PRIMARY_MODEL", "qwen2.5:14b")  # better to use "Qwen/Qwen2.5-14B-Instruct"
        self.secondary_model = os.environ.get("SECONDARY_MODEL", "THUDM/glm-4-9b-chat")
        self.get_info_prompt = f'''{system_prompt}'''
        self.get_info_suffix = f'''{user_prompt}'''

    async def get_anlalysis_res(self, text: str) -> dict:
        if not text:
            return {}
        content = f'评论内容：{text}\n\n{self.get_info_suffix}'
        message = [{'role': 'system', 'content': self.get_info_prompt}, {'role': 'user', 'content': content}]
        result = await llm(message, model=self.model, temperature=0.1, response_format={"type": "json_object"})
        logger.debug(f'input : {message}\n get_info llm output:\n{result}')
        if not result:
            return {}
        # result = json_repair.repair_json(result, return_objects=True)
        try:
            result_dict = json.loads(result)
        except json.JSONDecodeError as e:
            logger.warning(f"failed to parse from llm output: {e}")
            return {}
        if not isinstance(result_dict, dict):
            logger.warning("parsed result is not a dictionary")
            return {}
        if not result_dict:
            logger.debug("no info found")
            return {}
            # 业务数据清洗
        return result_dict
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
    comments = read_comments_from_excel('/backend/src/core/agents/comments.xlsx')

    async def main():
        gie = GeneralAnalysisInfoExtractor()
        # comment_list = json.loads(comment)

        # 每 10 个 comment 拼接为 str 然后调用一次接口
        results = []
        res = await gie.get_anlalysis_res(comments)
        results.extend(res)
        print(res)


    # 读取 comments.xlsx 文件，获取数据，文本分割，第一个为 id 第二个为 comment 生成 json 格式为 [{"id": 123, "comment": "comment"}]
    asyncio.run(main())
