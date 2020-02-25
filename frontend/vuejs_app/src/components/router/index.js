import Vue from 'vue'
import Router from 'vue-router'
import Main from '../main/Main'
import Events from '../events/Events'
import Locations from '../locations/Locations'
import About from '../about/About'
import Items from '../items/Items'
import Blog from '../blog/Blog'
import Heroes from '../heroes/Heroes'
import Login from '../login/Login'
import Signup from '../signup/Signup'
import NotFound from '../notFound/notFound'

Vue.use(Router);

export default new Router({
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
      path: '/heroes',
      name: 'Heroes',
      component: Heroes
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
        {
      path: '*',
      name: 'NotFound',
      component: NotFound
    },
  ]
})
