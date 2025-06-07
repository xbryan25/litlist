<script setup lang="ts">
import { defineProps, defineEmits, ref, computed, type Ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toastification'
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

const toast = useToast()
const router = useRouter()
const emit = defineEmits(['deleted'])

const deleteBook = async () => {
  try {
    const confirm = window.confirm('Are you sure you want to delete this book?')

    if (confirm) {
      await axios.delete(`/api/books/book/${props.book.id}`)

      toast.success('Book deleted successfully')

      emit('deleted', props.book.id)
    }
  } catch (error) {
    console.error('Error deleting book', error)
    toast.error('Book not deleted successfully')
  }
}
</script>

<template>
  <div class="grid grid-cols-[1fr_1fr_1fr_1fr_1fr_100px] mt-1 mb-1 max-h-[36px] h-[36px]">
    <div class="font-primary font-medium text-center text-white px-3 py-1 text-xl">
      {{ book.title }}
    </div>
    <div class="font-primary font-medium text-center text-white px-3 py-1 text-xl">
      {{ book.genre }}
    </div>
    <div class="font-primary font-medium text-center text-white px-3 py-1 text-xl">
      {{ book.author }}
    </div>
    <div class="font-primary font-medium text-center text-white px-3 py-1 text-xl">
      {{ book.pages }}
    </div>
    <div class="font-primary font-medium text-center text-white px-3 py-1 text-xl">
      {{ book.read_status ? 'Finished' : 'Not finished' }}
    </div>
    <div class="flex gap-2 mx-2 py-0.5">
      <div
        class="flex flex-1 rounded-lg border border-[#868484] justify-center items-center cursor-pointer hover:bg-[#2e2e2e]"
      >
        <RouterLink :to="`/edit-book/${props.book.id}`">
          <img src="@/assets/images/edit.svg" alt="Logo" class="w-[26px] h-auto" />
        </RouterLink>
      </div>
      <div
        @click="deleteBook"
        class="flex flex-1 rounded-lg border border-[#868484] justify-center items-center cursor-pointer hover:bg-[#2e2e2e]"
      >
        <img src="@/assets/images/delete.svg" alt="Logo" class="w-[26px] h-auto" />
      </div>
    </div>
  </div>
</template>
