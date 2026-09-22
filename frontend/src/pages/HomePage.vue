<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getStatsApi, type StatsOverview } from '@/api/stats'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const stats = ref<StatsOverview | null>(null)

onMounted(async () => {
  if (!userStore.isLoggedIn) return
  try {
    stats.value = await getStatsApi()
  } catch {
    // 拦截器已统一提示
  }
})
</script>

<template>
  <div class="page">
    <van-nav-bar title="智慧购物" />
    <template v-if="userStore.isLoggedIn && stats">
      <!-- 核心统计（TODO：后续用 ECharts 展示近 7 天扫描趋势） -->
      <van-grid :column-num="2" :border="false" class="stats-grid">
        <van-grid-item icon="scan" :text="`${stats.total_scans} 次累计扫描`" />
        <van-grid-item icon="warning-o" :text="`${stats.allergen_alerts} 次过敏警报`" />
        <van-grid-item icon="fire-o" :text="`${stats.today_scans} 次今日扫描`" />
        <van-grid-item icon="chart-trending-o" :text="`${stats.avg_score} 平均匹配分`" />
      </van-grid>
      <div class="quick-actions">
        <van-button type="primary" block round to="/scan">去扫码</van-button>
      </div>
    </template>
    <van-empty v-else description="登录后可查看个人扫描统计与过敏警报">
      <van-button round type="primary" to="/login">去登录 / 注册</van-button>
    </van-empty>
  </div>
</template>

<style scoped>
.stats-grid {
  margin-top: 12px;
}
.quick-actions {
  margin: 16px;
}
</style>
