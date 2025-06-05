<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="bg-[#434343] shadow-[0px_6px_4px_rgba(0,0,0,0.375)]">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <RouterLink class="flex flex-shrink-0 items-center mr-4 cursor-pointer" to="/">
            <div class="w-13 h-13 rounded-full bg-[#D9D9D9] mr-3"></div>
            <span class="font-primary font-bold hidden md:block text-[#F2EFEF] text-4xl ml-2"
              >LitList</span
            >
          </RouterLink>
          <div class="md:ml-auto mt-2">
            <div class="flex space-x-2">
              <RouterLink
                to="/"
                class="font-primary text-[#F2EFEF] hover:bg-[#2e2e2e] hover:text-white rounded-md px-3 py-1 font-bold text-2xl"
                >View Books</RouterLink
              >
              <RouterLink
                to="/add-book"
                class="font-primary text-[#F2EFEF] hover:bg-[#2e2e2e] hover:text-white rounded-md px-3 py-1 font-bold text-2xl"
                >Add Book</RouterLink
              >
              <div class="w-9 h-9 rounded-full bg-[#D9D9D9] mt-0.5 ml-1 cursor-pointer"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
