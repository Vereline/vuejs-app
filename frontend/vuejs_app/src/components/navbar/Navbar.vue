<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="/" class="text-uppercase">Elven Scroll</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
<!--        <b-nav-item href="#" class="text-uppercase"><router-link to="/heroes"><span class="navbar-item-link">Heroes</span></router-link></b-nav-item>-->
<!--        <b-nav-item href="#" class="text-uppercase"><router-link to="/locations"><span class="navbar-item-link">Locations</span></router-link></b-nav-item>-->
<!--        <b-nav-item href="#" class="text-uppercase"><router-link to="/items"><span class="navbar-item-link">Items</span></router-link></b-nav-item>-->
<!--        <b-nav-item href="#" class="text-uppercase"><router-link to="/events"><span class="navbar-item-link">Events</span></router-link></b-nav-item>-->
        <b-nav-item href="#" class="text-uppercase"><router-link to="/blog"><span class="navbar-item-link">Blog</span></router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about"><span class="navbar-item-link">About</span></router-link></b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
<!--          <b-dropdown-item href="#">RU</b-dropdown-item>-->
<!--          <b-dropdown-item href="#">BY</b-dropdown-item>-->
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
          <b-nav-item href="#" v-b-modal.signup-modal>Sign Up</b-nav-item>
        </div>
      </b-navbar-nav>
    </b-collapse>

    <login-modal></login-modal>
  </b-navbar>
</template>

<script>
  import LoginModal from "../login/Login";
  import SignupModal from "../signup/Signup";
  import store from '../../store';

  export default {
    name: "Navbar",
    components: {
        'login-modal': LoginModal,
        'signup-modal': SignupModal,
    },
    store,
    computed : {
      isLogin () {
        return this.$store.state.isLogin
      }
    },
    data () {
      return {
      }
    }
  }
</script>

<style scoped lang="scss">
 .navbar-item-link {
   color: rgba(0, 0, 0, 0.5);
   text-decoration: none;

   &:active, &:hover {
     color: rgba(0, 0, 0, 0.7);
     text-decoration: none;
   }
 }

 a {
   text-decoration: none;
 }
</style>
