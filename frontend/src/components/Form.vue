<script setup lang="ts">
import { withDefaults, defineProps, reactive, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

interface Book {
  id: string | string[]
  title: string
  genre: string
  author: string
  pages: number
  read_status: boolean
}

interface Props {
  formType?: string
}

type BookForm = Omit<Book, 'id'>

const route = useRoute()
const router = useRouter()
const toast = useToast()
const bookId = route.params.id

const props = withDefaults(defineProps<Props>(), {
  formType: 'add-book',
})

const form = reactive<BookForm>({
  title: '',
  genre: '',
  author: '',
  pages: 0,
  read_status: false,
})

const handleSubmit = async () => {
  const newBook: BookForm = {
    title: form.title,
    genre: form.genre,
    author: form.author,
    pages: form.pages,
    read_status: form.read_status,
  }

  try {
    if (props.formType === 'add-book') {
      const response = await axios.post(`/api/books/add-book`, newBook)

      toast.success('Book added successfully')
    } else if (props.formType === 'edit-book') {
      const response = await axios.put(`/api/books/book/${bookId}`, newBook)
      toast.success('Book edited successfully')
    }

    router.push('/')
  } catch (error) {
    if (props.formType === 'add-book') {
      console.error('Error adding book', error)
      toast.error('Book added unsuccessfully')
    } else if (props.formType === 'edit-book') {
      console.error('Error editing book', error)
      toast.error('Book edited unsuccessfully')
    }
  }
}

onMounted(async () => {
  if (props.formType === 'edit-book') {
    try {
      const response = await axios.get(`/api/books/book/${bookId}`)

      form.title = response.data.books.title
      form.genre = response.data.books.genre
      form.author = response.data.books.author
      form.pages = response.data.books.pages
      form.read_status = response.data.books.read_status == 1 ? true : false

      // console.log(response.data.books.title)
      console.log(form)
    } catch (error) {
      console.error('Error fetching book', error)
    }
  }
})
</script>

<template>
  <section>
    <div
      class="container m-auto max-w-2xl py-5 mt-15 bg-[#434343] rounded-xl border border-[#868484] shadow-[10px_10px_4px_rgba(0,0,0,0.375)]"
    >
      <form @submit.prevent="handleSubmit">
        <h2 class="text-center text-3xl text-[#D9D9D9] font-bold">
          {{ formType === 'add-book' ? 'Add Book' : 'Edit Book' }}
        </h2>

        <div class="mx-10 mt-2">
          <label class="block text-[#D9D9D9] font-bold mb-2 text-xl"> Title </label>
          <input
            v-model="form.title"
            type="text"
            id="title"
            name="title"
            class="border rounded w-full py-2 px-3 mb-2 text-[#D9D9D9] hover:bg-[#2e2e2e]"
            placeholder="Title"
            required
          />
        </div>

        <div class="mx-10 mt-2">
          <label class="block text-[#D9D9D9] font-bold mb-2 text-xl"> Genre </label>
          <input
            v-model="form.genre"
            type="text"
            id="genre"
            name="genre"
            class="border rounded w-full py-2 px-3 mb-2 text-[#D9D9D9] hover:bg-[#2e2e2e]"
            placeholder="Genre"
            required
          />
        </div>

        <div class="mx-10 mt-2">
          <label class="block text-[#D9D9D9] font-bold mb-2 text-xl"> Author </label>
          <input
            v-model="form.author"
            type="text"
            id="author"
            name="author"
            class="border rounded w-full py-2 px-3 mb-2 text-[#D9D9D9] hover:bg-[#2e2e2e]"
            placeholder="Author"
            required
          />
        </div>

        <div class="mx-10 mt-2">
          <label class="block text-[#D9D9D9] font-bold mb-2 text-xl"> Pages </label>
          <input
            v-model="form.pages"
            type="number"
            min="1"
            max="9999999"
            id="number"
            name="number"
            class="border rounded w-full py-2 px-3 mb-2 text-[#D9D9D9] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none hover:bg-[#2e2e2e]"
            placeholder="Number of pages"
            required
          />
        </div>

        <div class="mx-10 mt-2">
          <label class="block text-[#D9D9D9] font-bold mb-2 text-xl"> Read Status </label>

          <div class="mb-2">
            <label class="inline-flex items-center mr-4 cursor-pointer">
              <input
                v-model="form.read_status"
                type="radio"
                name="read-status"
                :value="true"
                class="w-3 h-3 mr-2 cursor-pointer"
                required
              />
              <span class="text-[#D9D9D9]">Finished</span>
            </label>

            <label class="inline-flex items-center cursor-pointer">
              <input
                v-model="form.read_status"
                type="radio"
                name="read-status"
                :value="false"
                class="w-3 h-3 mr-2 cursor-pointer"
                required
              />
              <span class="text-[#D9D9D9]">Not finished</span>
            </label>
          </div>
        </div>

        <div class="mx-10 mt-10">
          <button
            class="container w-full cursor-pointer text-center py-1 rounded-lg text-2xl font-bold bg-[#363636] text-[#F2EFEF] border border-[#868484] hover:bg-[#2e2e2e]"
            type="submit"
          >
            {{ formType === 'add-book' ? 'Add Book' : 'Edit Book' }}
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
