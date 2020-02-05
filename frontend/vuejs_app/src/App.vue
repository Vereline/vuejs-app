<template>
  <div id="app">
    <div id="main-page">
    <!-- Navbar -->
      <navbar :isLogin="isLoginUser"></navbar>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/navbar/Navbar";
export default {
  name: 'app',
  components: {
      'navbar': Navbar
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      isLoginUser: false,
    }
  }
}
</script>

<style lang="scss">

  #app {

  }

</style>
