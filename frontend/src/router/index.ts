import { createRouter, createWebHistory, type RouteRecordRaw} from 'vue-router'
import ViewBooksView from '@/views/ViewBooksView.vue'
import AddBookView from '@/views/AddBookView.vue'
import EditBookView from '@/views/EditBookView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: ViewBooksView,
  },
  {
    path: '/add-book',
    name: 'add-book',
    component: AddBookView,
  },
  {
    path: '/edit-book/:id',
    name: 'edit-book',
    component: EditBookView,
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
