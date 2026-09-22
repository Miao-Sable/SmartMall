<template>
  <div class="page">
    <van-nav-bar title="隐私与免责声明" left-arrow @click-left="$router.back()" />
    <div class="content">
      <h3>免责声明</h3>
      <p>本应用提供的过敏提醒和成分分析仅供参考，不构成医疗建议。请以商品包装说明和医生意见为准。</p>

      <h3>隐私说明</h3>
      <ul>
        <li>账号信息与过敏源、饮食偏好仅用于生成个人分析结果，不对外公开。</li>
        <li>扫描历史仅保存在您的个人账号下，可随时删除（TODO：删除功能）。</li>
        <li>本应用不采集商品包装以外的个人信息，不向第三方出售数据。</li>
      </ul>

      <h3>数据说明</h3>
      <p>MVP 阶段商品数据为本地模拟数据（mock），价格趋势为模拟数据，仅用于功能演示。</p>
    </div>
  </div>
</template>

<style scoped>
.content {
  padding: 16px;
  color: #323233;
  line-height: 1.7;
}
.content h3 {
  margin: 16px 0 8px;
}
.content p,
.content li {
  font-size: 14px;
}
</style>
