<script setup lang="ts">
import { defineProps, ref, computed, type Ref } from 'vue'
// import delete_icon from '@/assets/images/delete.svg'
// import edit_icon from '@/assets/images/edit.svg'

interface Book {
  id: string
  title: string
  genre: string
  author: string
  pages: number
  read_status: boolean
}

interface Props {
  book: Book
}

const props = defineProps<Props>()
</script>

<template>
  <div class="grid grid-cols-[1fr_1fr_1fr_1fr_1fr_100px] mt-1 mb-1">
    <div class="text-center text-white px-3 py-1 text-xl">{{ book.author }}</div>
    <div class="text-center text-white px-3 py-1 text-xl">{{ book.genre }}</div>
    <div class="text-center text-white px-3 py-1 text-xl">{{ book.author }}</div>
    <div class="text-center text-white px-3 py-1 text-xl">{{ book.pages }}</div>
    <div class="text-center text-white px-3 py-1 text-xl">
      {{ book.read_status ? 'Finished' : 'Not finished' }}
    </div>
    <div class="flex gap-1 mx-2">
      <div
        class="flex flex-1 rounded-lg border border-[#868484] justify-center items-center cursor-pointer hover:bg-[#2e2e2e]"
      >
        <RouterLink to="/edit-book">
          <img src="@/assets/images/edit.svg" alt="Logo" class="w-[26px] h-auto" />
        </RouterLink>
      </div>
      <div
        class="flex flex-1 rounded-lg border border-[#868484] justify-center items-center cursor-pointer hover:bg-[#2e2e2e]"
      >
        <img src="@/assets/images/delete.svg" alt="Logo" class="w-[26px] h-auto" />
      </div>
    </div>
  </div>
</template>
