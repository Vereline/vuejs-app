import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue';

import './styles/theme_colors.scss';
// import './styles/bootswatch_darkly.scss';

import router from './router'
import store from './store'
import i18n from './locales'
import apolloProvider from './apollo-client'

Vue.use(BootstrapVue);

new Vue({
  el: '#app',
  router,
  store,
  i18n,
  apolloProvider: apolloProvider,
  render: h => h(App)
});
