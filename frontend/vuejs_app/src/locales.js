import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n);

// Ready translated locale messages
const messages = {
  en: {
    navbarMessages: {
      blog: 'Blog',
      about: 'About',
      login: 'Log In',
      signup: 'Sign Up',
      lang: 'Lang',
    },
    blogMessages: {
      createBlog: 'Create Blog',
      blogs: 'Blog',
      viewFull: 'View full',
    },
  },
  ru: {
    navbarMessages: {
      blog: 'Блог',
      about: 'О сайте',
      login: 'Логин',
      signup: 'Регистрация',
      lang: 'Язык',
    },
    blogMessages: {
      createBlog: 'Создфть блог',
      blogs: 'Блоги',
      viewFull: 'Посмотреть полностью',
    },
  },
  // by: {
  //   navbarMessages: {
  //     blog: 'hello world',
  //     about: 'hello world'
  //   }
  // }
};

// Create VueI18n instance with options
const i18n = new VueI18n({
  locale: 'en', // set locale
  fallbackLocale: 'en', // set locale
  messages, // set locale messages
});

export default i18n
