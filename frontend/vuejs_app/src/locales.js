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
    aboutMessages: {
      header: 'About Us',
      teamHeader: 'Our Team',
      contactButton: 'Contact',
    },
    loginModal: {
      loginHeader: 'Login',
      emailLabel: 'Username or email',
      emailPlaceholder: 'Enter your username or email',
      passwordLabel: 'Password',
      passwordPlaceholder: 'Enter your password',
      loginButton: 'Login',
      signupLink: 'Don\'t have an account? Sign Up.',
    },
    signupModal: {
      signupHeader: 'Sign up',
      usernameLabel: 'Username',
      usernamePlaceholder: 'Enter your username',
      emailLabel: 'Email',
      emailPlaceholder: 'Enter your email',
      firstNameLabel: 'First name',
      firstNamePlaceholder: 'Enter your first name',
      lastNameLabel: 'Last name',
      lastNamePlaceholder: 'Enter your last name',
      passwordLabel: 'Password',
      passwordPlaceholder: 'Enter your password',
      confirmPasswordLabel: 'Confirm Password',
      confirmPasswordPlaceholder: 'Confirm your password',
      signupButton: 'Sign up',
      loginLink: 'Already have an account? Log In.',
    },
    blogDetail: {
      byWord: 'By',
      postedOn: 'Posted on',
      updatedOn: 'Updated on',
      commentsHeader: 'Comments',
    },
    commentForm: {
      commentHeader: 'Leave a comment',
      commentPlaceholder: 'Enter something...',
      commentSubmit: 'Submit',
    },
    createBlog: {
      createTitle: 'Create blog',
      titleLabel: 'Title',
      titlePlaceholder: 'Title',
      imageText: 'Click to add blog image',
      uploadImageText: 'Upload blog image',
      descriptionLabel: 'Description',
      descriptionPlaceholder: 'Description',
      createButton: 'Create blog',
    },
    mainPage: {
      mastheadText: 'Welcome to \ "ELVEN SCROLL \"!',
      mastheadSubText: 'An exciting adventure game (in development)',
      firstCol: 'Explore new imaginary world...',
      secondCol: 'Read and enjoy an exciting story!',
    },
    notFound: {
      mainDiv: 'Go to main page',
      mainLink: 'To main page',
    },
    personProfile: {
      photoText: 'Click on image to add profile photo',
      savePhotoButton: 'Save profile photo',
      joinDate: 'Date of join: ',
      birthDate: 'Birth date: ',
      activity: 'Activity: ',
      activeUser: 'Active user',
      inactiveUser: 'Not Active user',
    },
    errorMessages: {
      good: 'Looks good!',
      notEmpty: 'It shouldn\'t be empty at least.',
      minSymbols: 'Minimum length should be at least 5 symbols',
    }
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
      createBlog: 'Создать блог',
      blogs: 'Блоги',
      viewFull: 'Посмотреть полностью',
    },
    aboutMessages: {
      header: 'О нас',
      teamHeader: 'Наша команда',
      contactButton: 'Связаться',
    },
    loginModal: {
      loginHeader: 'Логин',
      emailLabel: 'Юзернейм или email',
      emailPlaceholder: 'Веедите email или имя пользователя',
      passwordLabel: 'Пароль',
      passwordPlaceholder: 'Введите пароль',
      loginButton: 'Логин',
      signupLink: 'Нет аккаунта? Зарегистрироваться.',
    },
    signupModal: {
      signupHeader: 'Зарегистрироваться',
      usernameLabel: 'Имя пользователя',
      usernamePlaceholder: 'Введите ваше имя пользователя',
      emailLabel: 'Email',
      emailPlaceholder: 'Введите ваш email',
      firstNameLabel: 'Имя',
      firstNamePlaceholder: 'Введите ваше имя',
      lastNameLabel: 'Фамилия',
      lastNamePlaceholder: 'Введите свою фамилию',
      passwordLabel: 'Пароль',
      passwordPlaceholder: 'Введите свой пароль',
      confirmPasswordLabel: 'Подтвердить пароль',
      confirmPasswordPlaceholder: 'Подтвердите свой пароль',
      signupButton: 'Зарегистрироваться',
      loginLink: 'Уже есть аккаунт? Авторизоваться.',
    },
    blogDetail: {
      byWord: 'От',
      postedOn: 'Создано',
      updatedOn: 'Обновлено',
      commentsHeader: 'Комментарии',
    },
    commentForm: {
      commentHeader: 'Оставьте комментарий',
      commentPlaceholder: 'Введите что-нибудь...',
      commentSubmit: 'Комментировать',
    },
    createBlog: {
      createTitle: 'Создать блог',
      titleLabel: 'Название',
      titlePlaceholder: 'Название',
      imageText: 'Нажмите, чтобы добавить изображение',
      uploadImageText: 'Загрузить изображение',
      descriptionLabel: 'Описание',
      descriptionPlaceholder: 'Описание',
      createButton: 'Создать блог',
    },
    mainPage: {
      mastheadText: 'Добро пожаловать в \"ELVEN SCROLL\"!',
      mastheadSubText: 'Захватывающая приключенческая игра (в разработке)',
      firstCol: 'Исследуйте новый воображаемый мир ...',
      secondCol: 'Читайте и наслаждайтесь захватывающей историей!',
    },
    notFound: {
      mainDiv: 'Вернуться на главную страницу',
      mainLink: 'На главную',
    },
    personProfile: {
      photoText: 'Нажмите, чтобы добавить фото профиля',
      savePhotoButton: 'Сохранить фото',
      joinDate: 'Дата регистрации: ',
      birthDate: 'Дата рождения: ',
      activity: 'Активность: ',
      activeUser: 'Активен',
      inactiveUser: 'Неактивен',
    },
    errorMessages: {
      good: 'Looks good!',
      notEmpty: 'It shouldn\'t be empty at least.',
      minSymbols: 'Minimum length should be at least 5 symbols',
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
const i18n = new VueI18n({
  locale: 'en', // set locale
  fallbackLocale: 'en', // set locale
  messages, // set locale messages
});

export default i18n
