/** 匹配度等级与颜色（与后端业务规则保持一致） */
export const SCORE_LEVELS = [
  { min: 90, label: '非常适合', color: '#07c160' },
  { min: 70, label: '比较适合', color: '#1989fa' },
  { min: 50, label: '一般', color: '#ff976a' },
  { min: 0, label: '不适合', color: '#ee0a24' },
] as const

export function scoreLevel(score: number) {
  return SCORE_LEVELS.find((l) => score >= l.min) ?? SCORE_LEVELS[SCORE_LEVELS.length - 1]
}

export function formatTime(iso: string) {
  return new Date(iso).toLocaleString('zh-CN', { hour12: false })
}
