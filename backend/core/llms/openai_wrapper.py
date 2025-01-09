import os
from openai import OpenAI
from openai import RateLimitError
import asyncio
from loguru import logger
base_url = os.environ.get('LLM_API_BASE', "http://192.168.15.8:3001/v1")
token = os.environ.get('LLM_API_KEY', "sk-dmzReHcJzXoP9b6J6f042d36E9A14c72B8F4Ce1139DcC431") # "qwen2.5:14b"

if not base_url and not token:
    raise ValueError("LLM_API_BASE or LLM_API_KEY must be set")
elif base_url and not token:
    client = OpenAI(base_url=base_url, api_key="not_use")
elif not base_url and token:
    client = OpenAI(api_key=token)
else:
    client = OpenAI(api_key=token, base_url=base_url)

llm_lock = asyncio.Lock()

async def openai_llm(messages: list, model: str, _logger = None, **kwargs) -> str:
    if _logger:
        _logger.debug(f'messages:\n {messages}')
        _logger.debug(f'model: {model}')
        _logger.debug(f'kwargs:\n {kwargs}')
    # _logger.info(f'messages:\n {messages}')
    async with llm_lock:
        try:
            response = client.chat.completions.create(messages=messages, model=model, **kwargs)
        except RateLimitError as e:
            _logger.warning(f'{e}\nRetrying in 60 second...')
            await asyncio.sleep(60)
            response = client.chat.completions.create(messages=messages, model=model, **kwargs)
            if response.status_code == 200 and response.choices:
                return response.choices[0].message.content
            else:
                _logger.error(f'after many try, llm error: {response}')
                return ""
        except Exception as e:
            if _logger:
                _logger.error(f'openai_llm error: {e}')
            return ''

    if _logger:
        _logger.debug(f'result:\n {response.choices[0]}')
        _logger.debug(f'usage:\n {response.usage}')

    return response.choices[0].message.content
