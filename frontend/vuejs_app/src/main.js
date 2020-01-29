import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue';

import './styles/bootswatch_flatly.scss';

import router from './components/router'

Vue.use(BootstrapVue);

new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
