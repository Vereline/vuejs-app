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
        <b-nav-item v-if="isLogin" href="#" class="text-uppercase"><router-link to="/blog" tag="li"><span class="navbar-item-link">{{ $t("navbarMessages.blog") }}</span></router-link></b-nav-item>
        <b-nav-item href="#" class="text-uppercase"><router-link to="/about" tag="li"><span class="navbar-item-link">{{ $t("navbarMessages.about") }}</span></router-link></b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <div class="theme-switch-wrapper">
          <label class="theme-switch" for="checkbox">
            <input type="checkbox" id="checkbox" />
            <div class="slider round" v-on:click="darkMode = !darkMode"/>
          </label>
        </div>

        <b-nav-item-dropdown right>
          <template v-slot:button-content>
            {{ $t("navbarMessages.lang") }}
          </template>
          <b-dropdown-item  class="text-uppercase"
                            v-for="(lang, i) in locales"
                            :key="`Lang${i}`"
                            :value="lang"
                            v-on:click="changeLocale(lang)">
            {{ lang }}
          </b-dropdown-item>
        </b-nav-item-dropdown>

        <div v-if="isLogin">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>{{ fullName }}</em>
            </template>
            <b-dropdown-item href="#">
              <router-link :to="{ name: 'PersonProfile', params: {id: userId }}" tag="li">
                <span class="navbar-item-link">Profile</span>
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item href="#" v-on:click="signOut">Sign Out</b-dropdown-item>

          </b-nav-item-dropdown>
        </div>
        <div v-else>
          <b-navbar-nav>
            <b-nav-item href="#" v-on:click="openLoginModal">{{ $t("navbarMessages.login") }}</b-nav-item>
            <b-nav-item href="#" v-on:click="openSignupModal">{{ $t("navbarMessages.signup") }}</b-nav-item>
<!--            <b-nav-item href="#" v-b-modal.login-modal>{{ $t("navbarMessages.login") }}</b-nav-item>-->
<!--            <b-nav-item href="#" v-b-modal.signup-modal>{{ $t("navbarMessages.signup") }}</b-nav-item>-->
          </b-navbar-nav>
        </div>
      </b-navbar-nav>
    </b-collapse>

    <signup-modal></signup-modal>
    <login-modal></login-modal>
  </b-navbar>
</template>

<script>
  import LoginModal from "../login/Login";
  import SignupModal from "../signup/Signup";
  import store from '../../store';
  import $i18n from '../../locales';

  export default {
    name: "Navbar",
    components: {
        'login-modal': LoginModal,
        'signup-modal': SignupModal,
    },
    store,
    $i18n,
    computed : {
      isLogin () {
        return this.$store.state.isLogin
      },
      userId () {
        return this.$store.state.id
      },
      fullName () {
          return this.$store.state.firstName + ' ' + this.$store.state.lastName;
      },
    },
    data () {
      return {
        darkMode: false,
        locales: ['en', 'ru'],
        // locales: ['en', 'ru', 'by'],
      }
    },
    mounted() {
      // check for active theme
      let htmlElement = document.documentElement;
      let theme = this.$store.state.siteTheme;

      if (theme === 'dark') {
        htmlElement.setAttribute('theme', 'dark');
        this.darkMode = true;
      } else {
        htmlElement.setAttribute('theme', 'light');
        this.darkMode = false;
      }
    },
    watch: {
      darkMode: function () {
        // add/remove class to/from html tag
        // get :root element
        let htmlElement = document.documentElement;

        if (this.darkMode) {
          store.commit('setSiteTheme', 'dark');
          localStorage.darkMode = true;
          htmlElement.setAttribute('theme', 'dark');
        } else {
          store.commit('setSiteTheme', 'light');
          localStorage.darkMode = false;
          htmlElement.setAttribute('theme', 'light');
        }
      }
    },
    methods: {
      changeLocale: function (locale) {
        $i18n.locale = locale;
        localStorage.locale = locale;
        store.commit('setLocale', 'locale');
      },
      signOut: function() {
        store.dispatch("logout");
        localStorage.clear();
      },
      openLoginModal: function () {
        store.commit('setOpenLoginModal');
      },
      openSignupModal: function () {
        store.commit('setOpenSignupModal');
      },
    },
  }
</script>

<style scoped lang="scss">
 /*.navbar-item-link {*/
 /*  color: rgba(0, 0, 0, 0.5);*/
 /*  text-decoration: none;*/

 /*  &:active, &:hover {*/
 /*    color: rgba(0, 0, 0, 0.7);*/
 /*    text-decoration: none;*/
 /*  }*/
 /*}*/

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

  //  on some devices this color on navbar is not applied, set up explicitly to ensure it works
  [theme="dark"] .bg-light.navbar {
    background-color: #303030 !important;
  }

</style>
