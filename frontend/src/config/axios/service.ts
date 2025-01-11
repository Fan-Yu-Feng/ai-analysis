import axios, {
  type AxiosError,
  type AxiosInstance,
  type AxiosRequestHeaders,
  type AxiosResponse,
  type InternalAxiosRequestConfig,
} from 'axios'

import { config } from '@/config/axios/config'
import { getProtocol } from '@/utils'

const { result_code, base_url, request_timeout } = config

// 是否显示重新登录
export const isRelogin = { show: false }
// Axios 无感知刷新令牌，参考 https://www.dashingdog.cn/article/11 与 https://segmentfault.com/a/1190000020210980 实现
// 请求队列

const customBaseURL = getProtocol() + base_url
// 创建axios实例
const service: AxiosInstance = axios.create({
  baseURL: customBaseURL, // api 的 base_url
  timeout: request_timeout, // 请求超时时间
  withCredentials: false, // 禁用 Cookie 等信息
})

export { service }
