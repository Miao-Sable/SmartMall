import request from './request'

export interface UserProfile {
  user_id: number
  email: string
  nickname: string
  gender: string
  birth_year: number | null
  allergen_ids: number[]
  diet_ids: number[]
}

export interface UserProfileUpdate {
  nickname?: string
  gender?: string
  birth_year?: number | null
  allergen_ids?: number[]
  diet_ids?: number[]
}

export const getProfileApi = () => request.get<UserProfile>('/user/profile').then((r) => r.data)

export const updateProfileApi = (data: UserProfileUpdate) =>
  request.put<UserProfile>('/user/profile', data).then((r) => r.data)
