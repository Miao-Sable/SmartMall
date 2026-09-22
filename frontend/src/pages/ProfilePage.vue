<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()

onMounted(() => {
  void userStore.fetchProfile()
})

function onLogout() {
  userStore.logout()
  router.push('/')
}
</script>

<template>
  <div class="page">
    <van-nav-bar title="我的" />
    <template v-if="userStore.isLoggedIn">
      <van-cell-group inset title="账号">
        <van-cell title="邮箱" :value="userStore.profile?.email ?? '加载中…'" />
        <van-cell title="昵称" :value="userStore.profile?.nickname || '未设置'" />
      </van-cell-group>
      <van-cell-group inset title="功能">
        <van-cell title="过敏源与饮食偏好" is-link to="/profile/setup" />
        <van-cell title="扫描历史" is-link to="/history" />
      </van-cell-group>
      <van-cell-group inset title="关于">
        <van-cell title="隐私与免责声明" is-link to="/privacy" />
        <van-cell title="版本" value="v0.2 MVP" />
      </van-cell-group>
      <div class="logout-wrap">
        <van-button block type="danger" plain round @click="onLogout">退出登录</van-button>
      </div>
    </template>
    <van-empty v-else description="登录后可使用扫码、档案与历史功能">
      <van-button round type="primary" to="/login">去登录</van-button>
    </van-empty>
  </div>
</template>

<style scoped>
.logout-wrap {
  margin: 24px 16px;
}
</style>
