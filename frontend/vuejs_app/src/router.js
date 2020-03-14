import Vue from 'vue'
import Router from 'vue-router'

import store from './store';
import axios from 'axios';
import {API_URL} from "./constants";

import Main from './components/main/Main'
import Events from './components/events/Events'
import Locations from './components/locations/Locations'
import About from './components/about/About'
import Items from './components/items/Items'
import BlogDetail from './components/blogDetail/blogDetail'
import CreateBlog from './components/createBlog/createBlog'
import Blog from './components/blog/Blog'
import Heroes from './components/heroes/Heroes'
// import Login from './components/login/Login'
// import Signup from './components/signup/Signup'
import NotFound from './components/notFound/notFound'
import personProfile from './components/personProfile/personProfile'

Vue.use(Router);

const router =  new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/events',
      name: 'Events',
      component: Events
    },
    {
      path: '/locations',
      name: 'Locations',
      component: Locations
    },
    {
      path: '/items',
      name: 'Items',
      component: Items
    },
    {
      path: '/blog',
      name: 'Blog',
      component: Blog
    },
    {
      path: '/blog/create',
      name: 'CreateBlog',
      component: CreateBlog,
    },
    {
      path: '/blog/:blogId',
      name: 'BlogDetail',
      component: BlogDetail,
    },
    {
      path: '/heroes',
      name: 'Heroes',
      component: Heroes
    },
    // {
    //   path: '/signup',
    //   name: 'Signup',
    //   component: Signup
    // },
    // {
    //   path: '/login',
    //   name: 'Login',
    //   component: Login
    // },
    {
      path: '/person/:id',
      name: 'PersonProfile',
      component: personProfile
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    },
  ]
});

router.beforeEach((to, from, next) => {
  let allowedRoutes = ["Main", "About", "NotFound"];

  if(allowedRoutes.includes(to.name)){
    next();
  } else {
    let token = store.state.token;

    if (!token) {
      router.push({name:'Main'});
      return
    }

    // validate token
    const data = {
      'token': token,
    };
    const url = 'accounts/token-verify';
    const options = {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      data: data,
      url: `${API_URL}/${url}/`,
    };
    axios.post(options.url, options.data, options)
      .then(response => {
        if(response.status === 201) {
          store.commit('setToken', response.data['token']);
          next();
        } else {
          router.push({name:'Main'});
        }
      }).catch(response => {
        console.log(response);
        router.push({name:'Main'});
    });
  }
});

export default router
