import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // put variables and collections here
    token: "",
    isLogin: false,
    id: "",
    username: "",
    siteTheme: "light",
    locale: "en",
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
    setUsername(state, username) {
      state.username = username
    },
    setId(state, id) {
      state.id = id
    },
    setSiteTheme(state, theme) {
      state.siteTheme = theme
    },
  },
  actions: {
    // put asynchronous functions that can call one or more mutation functions
  }
})
