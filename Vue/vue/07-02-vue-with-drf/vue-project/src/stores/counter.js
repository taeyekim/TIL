import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const sighUp = function () {
    // 1. 사용자 입력 데이터를 받아
    // 2. axios로 django에 요청을 보냄
  }

  return { articles, API_URL, getArticles, signUp }
}, { persist: true })
