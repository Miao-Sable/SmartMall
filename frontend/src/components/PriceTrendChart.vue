<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'
import type { PricePoint } from '@/api/product'

// MVP 阶段完整引入 ECharts，后续可按需引入以减小体积
const props = defineProps<{ points: PricePoint[]; productName?: string }>()

const chartRef = ref<HTMLDivElement>()
let chart: ReturnType<typeof echarts.init> | null = null

function render() {
  if (!chartRef.value) return
  if (!chart) chart = echarts.init(chartRef.value)
  chart.setOption({
    title: { text: props.productName ?? '历史价格', left: 'center', textStyle: { fontSize: 14 } },
    tooltip: { trigger: 'axis' },
    grid: { left: 48, right: 16, top: 40, bottom: 24 },
    xAxis: { type: 'category', data: props.points.map((p) => p.date) },
    yAxis: { type: 'value', scale: true, name: '元' },
    series: [
      {
        name: '价格',
        type: 'line',
        smooth: true,
        data: props.points.map((p) => p.price),
        areaStyle: { opacity: 0.15 },
      },
    ],
  })
}

function onResize() {
  chart?.resize()
}

onMounted(() => {
  render()
  window.addEventListener('resize', onResize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', onResize)
  chart?.dispose()
  chart = null
})

watch(() => props.points, render, { deep: true })
</script>

<template>
  <div ref="chartRef" class="price-chart" />
</template>

<style scoped>
.price-chart {
  width: 100%;
  height: 220px;
}
</style>
