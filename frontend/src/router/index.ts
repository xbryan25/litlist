import { createRouter, createWebHistory, type RouteRecordRaw} from 'vue-router'
import ViewBooksView from '@/views/ViewBooksView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: ViewBooksView,
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
