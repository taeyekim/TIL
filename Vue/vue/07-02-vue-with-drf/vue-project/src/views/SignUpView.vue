<template>
  <div>
    <h1>회원가입</h1>
      <form @submit.prevent="createArticle">
        <div>
          <label for="username">username : </label>
          <input type="text" v-model.trim="username" id="username">
        </div>
        <div>
          <label for="password">password : </label>
          <textarea v-model.trim="password" id="password"></textarea>
        </div>
        <div>
          <label for="password2">password confirmation : </label>
          <textarea v-model.trim="password2" id="password2"></textarea>
        </div>
        <input type="submit">
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()
const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
}
</script>

<style>

</style>
