import { createRouter, createWebHistory, type RouteRecordRaw} from 'vue-router'
import ViewBooksView from '@/views/ViewBooksView.vue'
import AddBookView from '@/views/AddBookView.vue'
import EditBookView from '@/views/EditBookView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: ViewBooksView,
    meta: {title: 'Litlist | View Books'}
  },
  {
    path: '/add-book',
    name: 'add-book',
    component: AddBookView,
    meta: {title: 'Litlist | Add Book'}
  },
  {
    path: '/edit-book/:id',
    name: 'edit-book',
    component: EditBookView,
    meta: {title: 'Litlist | EditBook'}
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
