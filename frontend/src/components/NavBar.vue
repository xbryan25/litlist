<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import bookImage from '@/assets/images/book.png'
import lightModeImage from '@/assets/images/light-mode.png'
import darkModeImage from '@/assets/images/dark-mode.png'

const imageSrc = ref(darkModeImage)
let changeImageText: string = 'Change to dark mode?'

function changeThemeImage() {
  if (imageSrc.value === lightModeImage) {
    imageSrc.value = darkModeImage
    document.documentElement.classList.remove('dark')
    changeImageText = 'Change to dark mode?'
  } else {
    imageSrc.value = lightModeImage
    document.documentElement.classList.toggle('dark')
    changeImageText = 'Change to light mode?'
  }
}
</script>

<template>
  <nav class="bg-[#f2f2f2] dark:bg-[#434343] shadow-[0px_6px_4px_rgba(0,0,0,0.375)]">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <RouterLink class="flex flex-shrink-0 items-center mr-4 cursor-pointer" to="/">
            <div class="w-13 h-13 mr-1"><img :src="bookImage" /></div>
            <span
              class="font-primary font-bold hidden md:block text-4xl ml-2 text-black dark:text-[#F2EFEF]"
              >LitList</span
            >
          </RouterLink>
          <div class="md:ml-auto mt-2">
            <div class="flex space-x-2">
              <RouterLink
                to="/"
                class="font-primary text-black hover:bg-[#cccccc] hover:text-black dark:text-[#F2EFEF] dark:hover:bg-[#2e2e2e] dark:hover:text-white rounded-md px-3 py-1 font-bold text-2xl"
                >View Books</RouterLink
              >
              <RouterLink
                to="/add-book"
                class="font-primary text-black hover:bg-[#cccccc] hover:text-black dark:text-[#F2EFEF] dark:hover:bg-[#2e2e2e] dark:hover:text-white rounded-md px-3 py-1 font-bold text-2xl"
                >Add Book</RouterLink
              >
              <div
                @click="changeThemeImage"
                class="w-9 h-9 mt-0.5 ml-1 cursor-pointer"
                :title="changeImageText"
              >
                <img :src="imageSrc" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
