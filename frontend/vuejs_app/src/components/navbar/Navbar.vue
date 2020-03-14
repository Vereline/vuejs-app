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

        <div class="theme-switch-wrapper">
          <label class="theme-switch" for="checkbox">
            <input type="checkbox" id="checkbox" />
            <div class="slider round" v-on:click="darkMode = !darkMode"/>
          </label>
<!--          <em>Enable Dark Mode!</em>-->
        </div>

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">BY</b-dropdown-item>
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
      },
      userId () {
        return this.$store.state.id
      },
    },
    data () {
      return {
        darkMode: false,
      }
    },
    mounted() {
      // check for active theme
      let htmlElement = document.documentElement;
      let theme = this.$store.state.siteTheme;

      if (theme === 'dark') {
        htmlElement.setAttribute('theme', 'dark');
        this.darkMode = true
      } else {
        htmlElement.setAttribute('theme', 'light');
        this.darkMode = false
      }
    },
    watch: {
      darkMode: function () {
        // add/remove class to/from html tag
        // get :root element
        let htmlElement = document.documentElement;

        if (this.darkMode) {
          store.commit('setSiteTheme', 'dark');
          htmlElement.setAttribute('theme', 'dark');
        } else {
          store.commit('setSiteTheme', 'light');
          htmlElement.setAttribute('theme', 'light');
        }
      }
    },
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

  /*Simple css to style it like a toggle switch*/
  .theme-switch-wrapper {
    display: flex;
    align-items: center;

    em {
      margin-left: 10px;
      font-size: 1rem;
    }
  }

  .theme-switch {
    display: inline-block;
    height: 34px;
    position: relative;
    width: 60px;

    input {
      display:none;
    }
  }

  .slider {
    background-color: #ccc;
    bottom: 0;
    cursor: pointer;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    transition: .4s;

    &:before {
    background-color: #fff;
    bottom: 4px;
    content: "";
    height: 26px;
    left: 4px;
    position: absolute;
    transition: .4s;
    width: 26px;
    }
  }

  input:checked + .slider {
    background-color: #66bb6a;
  }

  input:checked + .slider:before {
    transform: translateX(26px);
  }

  .slider.round {
    border-radius: 34px;

    &:before {
      border-radius: 50%;
    }
  }

</style>
