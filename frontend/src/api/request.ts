import axios from 'axios'
import { showToast } from 'vant'

/** axios 实例：请求自动携带 JWT，错误统一 Toast 提示 */
const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? '/api',
  timeout: 10000,
})

request.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

request.interceptors.response.use(
  (res) => res,
  (err) => {
    const detail: unknown = err.response?.data?.detail
    const message = typeof detail === 'string' ? detail : '网络异常，请稍后重试'
    showToast({ message, type: 'fail' })
    return Promise.reject(err)
  },
)

export default request
