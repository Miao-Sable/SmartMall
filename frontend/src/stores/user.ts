import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

import { loginApi, registerApi } from '@/api/auth'
import { getProfileApi, type UserProfile } from '@/api/user'

export const useUserStore = defineStore('user', () => {
  const token = ref(localStorage.getItem('token') ?? '')
  const profile = ref<UserProfile | null>(null)

  const isLoggedIn = computed(() => token.value !== '')

  async function login(email: string, password: string) {
    const res = await loginApi({ email, password })
    token.value = res.access_token
    localStorage.setItem('token', res.access_token)
    await fetchProfile()
  }

  async function register(data: { email: string; password: string; phone?: string }) {
    const res = await registerApi(data)
    token.value = res.access_token
    localStorage.setItem('token', res.access_token)
  }

  function logout() {
    token.value = ''
    profile.value = null
    localStorage.removeItem('token')
  }

  async function fetchProfile() {
    if (!isLoggedIn.value) return
    profile.value = await getProfileApi()
  }

  return { token, profile, isLoggedIn, login, register, logout, fetchProfile }
})
