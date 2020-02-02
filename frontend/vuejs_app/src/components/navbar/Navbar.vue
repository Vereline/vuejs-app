<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="/" class="text-uppercase">Elven Scroll</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/heroes">Heroes</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/locations">Locations</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/items">Items</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/events">Events</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/blog">Blog</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about">About</router-link></b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">CZ</b-dropdown-item>
        </b-nav-item-dropdown>

        <div v-if="isLogin">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>

          </b-nav-item-dropdown>
        </div>
        <div v-else>
          <b-nav-item href="#" v-b-modal.login-modal>Log In</b-nav-item>
        </div>
      </b-navbar-nav>
    </b-collapse>

    <login-modal></login-modal>
  </b-navbar>
</template>

<script>
  import LoginModal from "../login/Login";
  export default {
    name: "Navbar",
    components: {
        'login-modal': LoginModal
    },
    props: ['isLogin'],
    data () {
      return {
        isLogin: false,
      }
    }
  }
</script>

<style scoped>

</style>
