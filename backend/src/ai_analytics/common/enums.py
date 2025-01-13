import inspect
import sys
from enum import Enum, unique

from enum import Enum, unique


class BaseEnum(Enum):
	def __init__(self, code: str, msg: str):
		self.code = code
		self.msg = msg

	@classmethod
	def list_all(cls):
		return [{'code': item.code, 'msg': item.msg} for item in cls]

	@classmethod
	def get_by_code(cls, code: str):
		for item in cls:
			if item.code == code:
				return item
		return None

	@classmethod
	def get_by_msg(cls, msg: str):
		for item in cls:
			if item.msg == msg:
				return item
		return None




class TaskTypeEnum(BaseEnum):
	"""任务类型"""
	# 分析评论任务
	AnalysisComment = ('AnalysisComment', '分析评论任务')


@unique
class TaskStatusEnum(BaseEnum):
	"""任务状态"""
	WAIT = ('wait', '任务创建')
	PROGRESS = ('progress', '任务处理中')
	SUCCESS = ('success', '任务完成')
	FAILED = ('failed', '任务失败')


def get_enum_data(enum_name: str):
	current_module = sys.modules[__name__]
	for name, obj in inspect.getmembers(current_module, inspect.isclass):
		if issubclass(obj, BaseEnum) and obj.__name__ == enum_name:
			return obj.list_all()
	return None

print(get_enum_data('TaskStatusEnum'))  # [{'code': 'wait', 'msg': '任务创建'}, {'code': 'progress', 'msg': '任务处理中'}, {'code': 'success', 'msg': '任务完成'}, {'code': 'failed', 'msg': '��务失败'}]
