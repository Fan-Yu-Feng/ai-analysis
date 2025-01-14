import request from '@/config/axios'
import type { CommonRespResult } from './utils'
// 'TaskStatusEnum' | 'TaskTypeEnum'
export enum EnumName {
  TaskStatusEnum = 'TaskStatusEnum',
  TaskTypeEnum = 'TaskTypeEnum',
}

export interface EnumItem {
  msg: string
  code: string
}

export const EnumsApi = {
  getList: async (name: EnumName) => {
    return (await request.get)<CommonRespResult<EnumItem[]>>({ url: `/enum/name=${name}` })
  },
  getTaskStatusEnum: async () => {
    const { data } = await EnumsApi.getList(EnumName.TaskStatusEnum)
    return data
  },
  getTaskTypeEnum: async () => {
    const { data } = await EnumsApi.getList(EnumName.TaskTypeEnum)
    return data
  },
}
