import request from './request'

export interface NutritionItem {
  name: string
  value: string
  unit: string
  per: string
}

export interface Product {
  id: number
  barcode: string
  name: string
  brand: string
  category: string
  image_url: string
  description: string
  ingredients: string[]
  tags: string[]
  nutrition: NutritionItem[]
}

export interface PricePoint {
  date: string
  price: number
}

export interface PriceHistory {
  product_id: number
  barcode: string
  points: PricePoint[]
}

export const getProductApi = (barcode: string) =>
  request.get<Product>(`/products/${barcode}`).then((r) => r.data)

export const getPriceHistoryApi = (productId: number) =>
  request.get<PriceHistory>(`/products/${productId}/price-history`).then((r) => r.data)
