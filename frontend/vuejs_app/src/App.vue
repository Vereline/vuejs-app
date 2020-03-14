<template>
  <div id="app">
    <div id="main-page">
    <!-- Navbar -->
      <navbar :isLogin="isLoginUser"></navbar>
      <router-view></router-view>
      <!-- Copyright Section -->
      <div class="mb-3"></div>
      <section class="copyright py-4 text-center text-white bg-primary">
        <b-container>
          <small>Now I dont have a Copyright &copy; Elven Scroll 2019</small>
        </b-container>
      </section>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/navbar/Navbar";
import store from './store';

export default {
  name: 'app',
  components: {
    'navbar': Navbar
  },
  store,
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      isLoginUser: false,
    }
  },
}
</script>

<style lang="scss">

  #app {

  }

</style>
