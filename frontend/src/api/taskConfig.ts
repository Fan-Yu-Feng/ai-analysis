import request from '@/config/axios'

type TaskConfigResult = {
  success: boolean
  data: Array<any>
}

export const TaskConfigApi = {
  getTypeTaskPage: async (params: any) => {
    return await request.get({ url: `/grid/type-task/page`, params })
  },
  getTypeTaskList: async (params: any) => {
    return await request.get<TaskConfigResult>({ url: `/task-config?id=1` })
  },
}
