<script setup lang="ts">
import TableRow from './TableRow.vue'

interface Book {
  id: string
  title: string
  genre: string
  author: string
  pages: number
  readStatus: boolean
}

const books: Book[] = [
  {
    id: '1',
    title: 'Harry Potter',
    genre: 'Fantasy',
    author: 'J.K. Rowling',
    pages: 350,
    readStatus: true,
  },
  {
    id: '2',
    title: 'Lord of the Rings',
    genre: 'Adventure',
    author: 'Tolkien',
    pages: 670,
    readStatus: true,
  },
]
</script>

<template>
  <div
    class="bg-[#434343] min-h-130 rounded-xl border border-[#868484] shadow-[10px_10px_4px_rgba(0,0,0,0.375)]"
  >
    <div class="grid grid-cols-[1fr_1fr_1fr_1fr_1fr_100px] mt-1 mb-1">
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Title</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Primary Genre</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Author</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Pages</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Read Status</div>
      <div class="text-center text-white px-3 py-1 font-bold text-xl">Actions</div>
    </div>

    <hr class="border-t border-[#868484]" />

    <TableRow v-for="book in books.slice(0, books.length)" :key="book.id" :book="book" />
  </div>
</template>
