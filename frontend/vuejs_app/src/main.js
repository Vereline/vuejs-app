import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue';
import VueI18n from 'vue-i18n';

import './styles/theme_colors.scss';
// import './styles/bootswatch_darkly.scss';

import router from './router'
import store from './store'
import apolloProvider from './apollo-client'

Vue.use(BootstrapVue);
Vue.use(VueI18n);

new Vue({
  el: '#app',
  router,
  store,
  apolloProvider: apolloProvider,
  render: h => h(App)
});
