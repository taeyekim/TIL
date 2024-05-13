import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([
    { id: 1, title: 'Article 1', content: 'Content 1'},
    { id: 2, title: 'Article 2', content: 'Content 2'},
  ])
  return { }
}, { persist: true })
