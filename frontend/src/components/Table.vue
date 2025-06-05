<script setup lang="ts">
import { onMounted, reactive, defineProps, watch } from 'vue'
import axios from 'axios'
import TableRow from './TableRow.vue'

interface Book {
  id: string
  title: string
  genre: string
  author: string
  pages: number
  read_status: boolean
}

interface Props {
  sortType?: string
  sortBy?: string
  searchType?: string
  searchInput?: string
}

interface State {
  books: Book[]
}

const props = withDefaults(defineProps<Props>(), {
  sortType: 'Title',
  sortBy: 'Ascending',
})

const state = reactive<State>({
  books: [],
})

const handleDelete = (id: string) => {
  state.books = state.books.filter((book) => book.id !== id)
}

const fetchData = async () => {
  try {
    const response = await axios.get('/api/books', {
      params: {
        sort_type: props.sortType,
        sort_by: props.sortBy,
        search_type: props.searchType,
        search_input: props.searchInput,
      },
    })

    state.books = response.data.books
  } catch (error) {
    console.error('Error fetching jobs', error)
  }
}

watch(
  [() => props.sortType, () => props.sortBy, () => props.searchType, () => props.searchInput],
  () => {
    fetchData()
  },
  { immediate: true }, // Replaces onMounted
)
</script>

<template>
  <div
    class="bg-[#434343] min-h-[70vh] rounded-xl border border-[#868484] shadow-[10px_10px_4px_rgba(0,0,0,0.375)]"
  >
    <div class="grid grid-cols-[1fr_1fr_1fr_1fr_1fr_100px] mt-1 mb-1">
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Title</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Genre</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Author</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Pages</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Read Status</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Actions</div>
    </div>

    <hr class="border-t border-[#868484]" />

    <TableRow
      v-for="book in state.books.slice(0, state.books.length)"
      :key="book.id"
      :book="book"
      @deleted="handleDelete"
    />
  </div>
</template>
