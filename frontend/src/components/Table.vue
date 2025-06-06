<script setup lang="ts">
import {
  onMounted,
  reactive,
  defineProps,
  watch,
  type Ref,
  ref,
  nextTick,
  onBeforeUnmount,
} from 'vue'
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
  visibleBooks: Book[]
}

const props = withDefaults(defineProps<Props>(), {
  sortType: 'Title',
  sortBy: 'Ascending',
})

const state = reactive<State>({
  books: [],
  visibleBooks: [],
})

const handleDelete = (id: string) => {
  state.books = state.books.filter((book) => book.id !== id)
}

// rowHeight = tableRow + tableRow.marginTop + tableRow.marginBottom
const rowHeight: number = 36 + 4 + 4
const visibleRows: Ref<number> = ref(0)

const tableRef: Ref<HTMLElement | null> = ref<HTMLElement | null>(null)

async function updateVisibleRows(): Promise<void> {
  await nextTick()

  if (tableRef.value) {
    const tableTop = tableRef.value.getBoundingClientRect().top
    const viewportHeight = window.innerHeight

    // rowHeight + 1 -> header and line
    const excess = rowHeight + 1 + rowHeight
    const availableHeight = viewportHeight - tableTop - excess

    visibleRows.value = Math.floor(availableHeight / rowHeight)

    state.visibleBooks = state.books.slice(0, visibleRows.value)
  } else {
    return
  }
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
  async () => {
    await fetchData()
    await updateVisibleRows()
  },

  { immediate: true }, // Supplements onMounted
)

onMounted(async () => {
  window.addEventListener('resize', updateVisibleRows)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateVisibleRows)
})
</script>

<template>
  <div
    ref="tableRef"
    class="bg-[#434343] min-h-[60vh] rounded-xl border border-[#868484] shadow-[10px_10px_4px_rgba(0,0,0,0.375)] overflow-y-hidden h-full"
  >
    <div class="grid grid-cols-[1fr_1fr_1fr_1fr_1fr_100px] mt-1 mb-1">
      <div class="font-primary text-center text-white px-3 py-1 font-bold text-xl">Title</div>
      <div class="font-primary text-center text-white px-3 py-1 font-bold text-xl">Genre</div>
      <div class="font-primary text-center text-white px-3 py-1 font-bold text-xl">Author</div>
      <div class="font-primary text-center text-white px-3 py-1 font-bold text-xl">Pages</div>
      <div class="font-primary text-center text-white px-3 py-1 font-bold text-xl">Read Status</div>
      <div class="font-primary text-center text-white px-3 py-1 font-bold text-xl">Actions</div>
    </div>

    <hr class="border-t border-[#868484]" />

    <TableRow
      v-for="book in state.visibleBooks.slice(0, state.visibleBooks.length)"
      :key="book.id"
      :book="book"
      @deleted="handleDelete"
    />
  </div>
</template>
