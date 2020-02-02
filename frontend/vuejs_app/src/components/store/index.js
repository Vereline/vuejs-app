import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // put variables and collections here
    token: '',
  },
  mutations: {
    // put synchronous functions for changing state e.g. add, edit, delete
    setToken(state, token) {
      state.token = token
    }
  },
  actions: {
    // put asynchronous functions that can call one or more mutation functions
  }
})
