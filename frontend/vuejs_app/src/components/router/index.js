import Vue from 'vue'
import Router from 'vue-router'
// import Main from '@/components/Main'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      // component: Main
    },
    {
      path: '/about',
      name: 'About',
      // component: About
    }
    ,
    {
      path: '/events',
      name: 'Events',
      // component: Events
    },
    {
      path: '/locations',
      name: 'Locations',
      // component: Locations
    },
    {
      path: '/items',
      name: 'Items',
      // component: Items
    },
    {
      path: '/blog',
      name: 'Blog',
      // component: Blog
    }
    ,
    {
      path: '/heroes',
      name: 'Heroes',
      // component: Heroes
    }
  ]
})
