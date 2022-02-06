<template>
  <app-header/>
  <app-content/>
  <app-footer/>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import AppContent from './components/AppContent.vue'
import AppFooter from './components/AppFooter.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppContent,
    AppFooter,
  },
  data(){
    return {
      TOTAL_SAVINGS : '$0', TOTAL_LOSS : '$0'
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  flex-direction: column;
}
</style>
