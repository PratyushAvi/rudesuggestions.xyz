<template>
  <div id="app">
    <smort-agent/>
  </div>
</template>

<script>
// import Main from './components/main.vue'
import SmortAgent from './components/SmortAgent.vue'

export default {
  name: 'App',
  components: {
    SmortAgent
  }
}
</script>

<style>
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 0;
  background-color: #121212;
}
</style>