export const baseUrlApi = (url: string) => `/api/v1/${url}`

export interface CommonRespResult<T> {
  success: boolean
  data: T
  code: number
}

export interface BasePageParams {
  pageNo?: number
  pageSize?: number
}
