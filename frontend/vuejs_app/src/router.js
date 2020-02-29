import Vue from 'vue'
import Router from 'vue-router'
import Main from './components/main/Main'
import Events from './components/events/Events'
import Locations from './components/locations/Locations'
import About from './components/about/About'
import Items from './components/items/Items'
import BlogDetail from './components/blogDetail/blogDetail'
import CreateBlog from './components/createBlog/createBlog'
import Blog from './components/blog/Blog'
import Heroes from './components/heroes/Heroes'
import Login from './components/login/Login'
import Signup from './components/signup/Signup'
import NotFound from './components/notFound/notFound'

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
