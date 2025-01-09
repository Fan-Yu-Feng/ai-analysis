from enum import Enum, unique


@unique
class Weekday(Enum):
	Sun = 0  # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


class GenderEnum(Enum):
	Male = 1
	Female = 2


class TaskTypeEnum(Enum):
	"""任务类型"""
	# 分析评论任务
	AnalysisComment = 'AnalysisComment'


class TaskStatusEnum(Enum):
	"""任务状态"""
	# 任务创建
	WAIT = 'wait'
	# 任务处理中
	PROGRESS = 'progress'
	# 任务完成
	SUCCESS = 'success'
	# 任务失败
	FAILED = 'failed'
