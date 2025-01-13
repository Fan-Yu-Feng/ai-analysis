import request from '@/config/axios'

type TaskConfigResult = {
  success: boolean
  data: Array<any>
}

// 任务配置 VO
export interface ConfigVO {
  id: number // ID
  promptConfigId: number // 评论配置表 id
  status: string // 任务状态：待处理、处理中、已完成、失败
  priority: number // 任务优先级，数值越大优先级越高
  configDetail: string // 配置明细
  errorMessage: string // 错误信息，如果任务失败则记录错误信息
  createBy: string // 创建者
  updateBy: string // 修改者
  taskType: string // 任务类型：评论分析、舆情分析，等等
}

type TaskConfigReqParams = {
  status: string
  task_type: string
  priority?: number
  config_detail?: string
  error_message?: string
}

export const TaskConfigApi = {
  getTypeTaskPage: async (params: TaskConfigReqParams) => {
    return await request.get({ url: `/task-config/page`, params })
  },
  add: async (data: TaskConfigReqParams) => {
    return await request.post<TaskConfigResult>({ url: `/task-config/add`, data })
  },
  getById: async (id: number) => {
    return await request.get<TaskConfigResult>({ url: `/task-config/get-by-id/` + id })
  },
  updateById: async (data: TaskConfigReqParams) => {
    return await request.post<TaskConfigResult>({ url: `/task-config/update`, data })
  },
  delete: async (id: number) => {
    return await request.delete<TaskConfigResult>({ url: `/task-config/delete/` + id })
  },
}
