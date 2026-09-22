import request from './request'

export interface DailyCount {
  date: string
  count: number
}

export interface StatsOverview {
  total_scans: number
  allergen_alerts: number
  today_scans: number
  avg_score: number
  recent_days: DailyCount[]
}

export const getStatsApi = () => request.get<StatsOverview>('/stats/overview').then((r) => r.data)
