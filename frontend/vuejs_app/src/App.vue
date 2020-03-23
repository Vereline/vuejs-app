<template>
  <div id="app" class="main-page">
    <div id="main-page" class="content-wrap">
    <!-- Navbar -->
      <navbar :isLogin="isLoginUser"></navbar>
      <router-view></router-view>
      <!-- Copyright Section -->
      <div class="mb-3"></div>
    </div>
    <section class="copyright py-4 text-center text-white bg-primary page-footer">
      <b-container>
        <small>Now I dont have a Copyright &copy; Elven Scroll 2019</small>
      </b-container>
    </section>
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

  .main-page {
    position: relative;
    min-height: 100vh;
  }

  .content-wrap {
    padding-bottom: 4.5rem;    /* Footer height */
  }

  .page-footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 4.5rem;            /* Footer height */
  }
</style>
