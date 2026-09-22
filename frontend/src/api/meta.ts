import request from './request'

export interface Allergen {
  id: number
  name: string
  category: string
  keywords: string[]
  description: string
}

export interface DietPreference {
  id: number
  name: string
  keywords: string[]
  description: string
}

export const getAllergensApi = () => request.get<Allergen[]>('/meta/allergens').then((r) => r.data)

export const getDietPreferencesApi = () =>
  request.get<DietPreference[]>('/meta/diet-preferences').then((r) => r.data)
