import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Result from '../views/Result.vue'
require('typeface-roboto')
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/integrals',
    name: 'Integral Calculator',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Integrals.vue')
  },
  {
    path: '/solution/:solution/message/:message',
    name: 'Result',
    component: Result
  }
]

const router = new VueRouter({
  routes
})

export default router
