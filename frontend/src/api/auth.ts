import request from './request'

export interface RegisterParams {
  email: string
  password: string
  phone?: string
}

export interface LoginParams {
  email: string
  password: string
}

export interface TokenResponse {
  access_token: string
  token_type: string
  user_id: number
  email: string
}

export const registerApi = (data: RegisterParams) =>
  request.post<TokenResponse>('/auth/register', data).then((r) => r.data)

export const loginApi = (data: LoginParams) =>
  request.post<TokenResponse>('/auth/login', data).then((r) => r.data)
