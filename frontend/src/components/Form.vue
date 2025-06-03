<script setup lang="ts">
import { withDefaults, defineProps } from 'vue'

const handleSubmit = () => {
  console.log('Submit')
}

interface Props {
  formType?: string
}

const props = withDefaults(defineProps<Props>(), {
  formType: 'add-book',
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
                type="radio"
                name="read-status"
                value="read"
                class="w-3 h-3 mr-2 cursor-pointer"
                required
              />
              <span class="text-[#D9D9D9]">Finished</span>
            </label>

            <label class="inline-flex items-center cursor-pointer">
              <input
                type="radio"
                name="read-status"
                value="unread"
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
