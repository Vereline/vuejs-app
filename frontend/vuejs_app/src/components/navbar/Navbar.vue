<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="#" class="text-uppercase">Elven Scroll</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about">Heroes</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about">Locations</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about">Items</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about">Events</router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about">Blog</router-link></b-nav-item>
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
        <div v-else="isLogin">
          <b-nav-item href="#" disabled>Log In</b-nav-item>
          <b-nav-item href="#" disabled>Sign Up</b-nav-item>
        </div>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
  export default {
    name: "Navbar",
    data () {
      return {
        isLogin: false,
      }
    }
  }
</script>

<style scoped>

</style>
