<script setup lang="ts">
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { showToast } from 'vant'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

const email = ref('')
const password = ref('')
const loading = ref(false)

async function onSubmit() {
  if (!email.value.trim() || !password.value) {
    showToast('请输入邮箱和密码')
    return
  }
  loading.value = true
  try {
    await userStore.login(email.value.trim(), password.value)
    showToast({ message: '登录成功', type: 'success' })
    // 首次登录（尚未建立档案）时引导填写个人信息表，可跳过；老用户直接进入
    const redirect = typeof route.query.redirect === 'string' ? route.query.redirect : undefined
    if (userStore.profile?.onboarded) {
      router.replace(redirect || '/')
    } else {
      router.replace({ path: '/profile/setup', query: { from: 'login', ...(redirect ? { redirect } : {}) } })
    }
  } catch {
    // 登录失败已由拦截器提示
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="page">
    <van-nav-bar title="登录" />
    <van-form class="form" @submit="onSubmit">
      <van-cell-group inset>
        <van-field
          v-model="email"
          name="email"
          label="邮箱"
          type="email"
          placeholder="请输入邮箱"
          :rules="[{ required: true, message: '请填写邮箱' }]"
        />
        <van-field
          v-model="password"
          type="password"
          name="password"
          label="密码"
          placeholder="请输入密码"
          :rules="[{ required: true, message: '请填写密码' }]"
        />
      </van-cell-group>
      <div class="form-actions">
        <van-button round block type="primary" native-type="submit" :loading="loading">登录</van-button>
        <van-button round block plain type="primary" class="gap" to="/register">没有账号？去注册</van-button>
      </div>
      <p class="tip">MVP 阶段支持邮箱 + 密码登录，短信验证码暂未接入</p>
    </van-form>
  </div>
</template>

<style scoped>
.form {
  margin-top: 16px;
}
.form-actions {
  margin: 24px 16px;
}
.gap {
  margin-top: 12px;
}
.tip {
  padding: 0 24px;
  color: #969799;
  font-size: 12px;
  text-align: center;
}
</style>
