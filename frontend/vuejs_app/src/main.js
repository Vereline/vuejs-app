import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue';

import './styles/bootswatch_flatly.scss';
// import './styles/bootswatch_darkly.scss';

import router from './router'
import store from './store'
import apolloProvider from './apollo-client'

Vue.use(BootstrapVue);

new Vue({
  el: '#app',
  router,
  store,
  apolloProvider: apolloProvider,
  render: h => h(App)
});
