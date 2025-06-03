<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="bg-[#434343] shadow-[0px_4px_4px_rgba(0,0,0,0.25)]">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <RouterLink class="flex flex-shrink-0 items-center mr-4" to="/">
            <div class="w-13 h-13 rounded-full bg-[#D9D9D9] mr-3"></div>
            <span class="hidden md:block text-[#F2EFEF] text-4xl font-bold ml-2">LitList</span>
          </RouterLink>
          <div class="md:ml-auto mt-2">
            <div class="flex space-x-2">
              <RouterLink
                to="/"
                class="text-white hover:bg-gray-900 hover:text-white rounded-md px-3 py-1 font-bold text-xl"
                >View Books</RouterLink
              >
              <a
                href="jobs.html"
                class="text-white hover:bg-gray-900 hover:text-white rounded-md px-3 py-1 font-bold text-xl"
                >Add Book</a
              >
              <div class="w-9 h-9 rounded-full bg-[#D9D9D9] mt-0.5 ml-1 cursor-pointer"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
