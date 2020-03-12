import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n);

// Ready translated locale messages
const messages = {
  en: {
    navbarMessages: {
      blog: 'Blog',
      about: 'About'
    }
  },
  ru: {
    navbarMessages: {
      blog: 'Блог',
      about: 'О сайте'
    }
  },
  // by: {
  //   navbarMessages: {
  //     blog: 'hello world',
  //     about: 'hello world'
  //   }
  // }
};

// Create VueI18n instance with options
export default new VueI18n({
  locale: 'en', // set locale
  messages, // set locale messages
});
