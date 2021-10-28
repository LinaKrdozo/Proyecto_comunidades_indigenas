import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'

import Home                  from './components/home.vue'
import formularioComunidades from './components/formularioComunidades.vue'
import formularioProductos from './components/formularioProductos.vue'
import formularioComProd from './components/formularioComProd.vue'
import formularioTabla from './components/formularioTabla.vue'

const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },

  {
    path: '/home',
    name: 'home',
    component: Home
  },

  {
    path: '/formularioComunidades',
    name: 'formularioComunidades',
    component: formularioComunidades
  },
  

  {
    path: '/formularioProductos',
    name: 'formularioProductos',
    component: formularioProductos
  },

  {
    path: '/formularioComProd',
    name: 'formularioComProd',
    component: formularioComProd
  },
  {
    path: '/formularioTabla',
    name: 'formularioTabla',
    component: formularioTabla
  }

]; 

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
