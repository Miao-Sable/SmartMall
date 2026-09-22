<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()

const email = ref('')
const password = ref('')
const confirm = ref('')
const loading = ref(false)

async function onSubmit() {
  if (password.value !== confirm.value) {
    showToast('两次输入的密码不一致')
    return
  }
  loading.value = true
  try {
    await userStore.register({ email: email.value.trim(), password: password.value })
    showToast({ message: '注册成功，请登录', type: 'success' })
    router.replace('/login')
  } catch {
    // 注册失败已由拦截器提示
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="page">
    <van-nav-bar title="注册" left-arrow @click-left="$router.back()" />
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
          placeholder="至少 6 位"
          :rules="[
            { required: true, message: '请填写密码' },
            { validator: (v: string) => v.length >= 6, message: '密码至少 6 位' },
          ]"
        />
        <van-field
          v-model="confirm"
          type="password"
          name="confirm"
          label="确认密码"
          placeholder="再次输入密码"
          :rules="[{ required: true, message: '请再次输入密码' }]"
        />
      </van-cell-group>
      <div class="form-actions">
        <van-button round block type="primary" native-type="submit" :loading="loading">注册</van-button>
        <van-button round block plain type="primary" class="gap" to="/login">已有账号？去登录</van-button>
      </div>
      <p class="tip">注册即代表同意隐私政策；过敏源等敏感信息仅加密存储于个人账号</p>
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
