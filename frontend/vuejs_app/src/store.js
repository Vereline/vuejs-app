import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist'

Vue.use(Vuex);

const vuexPersist = new VuexPersist({
  key: 'vuejs-app',
  storage: window.localStorage
})

export default new Vuex.Store({
  state: {
    // put variables and collections here
    token: "",
    isLogin: false,
    isAdmin: false,
    id: "",
    username: "",
    siteTheme: "light",
    locale: "en",
    firstName: "",
    lastName: "",
    openedLoginModal: false,
    openedSignupModal: false,
  },
  mutations: {
    // put synchronous functions for changing state e.g. add, edit, delete
    setToken(state, token) {
      state.token = token
    },
    setIsLogin(state) {
      state.isLogin = true
    },
    setIsLogout(state) {
      state.isLogin = false
    },
    setIsAdmin(state) {
      state.isAdmin = true
    },
    setIsNotAdmin(state) {
      state.isAdmin = false
    },
    setOpenSignupModal(state) {
      state.openedSignupModal = true
    },
    setCloseSignupModal(state) {
      state.openedSignupModal = false
    },
    setOpenLoginModal(state) {
      state.openedLoginModal = true
    },
    setCloseLoginModal(state) {
      state.openedLoginModal = false
    },
    setUsername(state, username) {
      state.username = username
    },
    setId(state, id) {
      state.id = id
    },
    setFirstName(state, firstName) {
      state.firstName = firstName
    },
    setLastName(state, lastName) {
      state.lastName = lastName
    },
    setSiteTheme(state, theme) {
      state.siteTheme = theme
    },
    setLocale(state, locale) {
      state.locale = locale
    },
  },
  actions: {
    logout(context) {
      context.commit('setIsLogout');
      context.commit('setIsNotAdmin');
      context.commit('setLastName', "");
      context.commit('setFirstName', "");
      context.commit('setId', "");
      context.commit('setUsername', "");
      context.commit('setToken', "");
    }
    // put asynchronous functions that can call one or more mutation functions
  },
  plugins: [vuexPersist.plugin],
})
