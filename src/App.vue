<template>
  <div id="app">
    <Main/>
  </div>
</template>

<script>
import Main from './components/main.vue'

export default {
  name: 'App',
  components: {
    Main
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
