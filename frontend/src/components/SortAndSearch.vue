<script setup lang="ts"></script>

<template>
  <div class="flex max-h-10 h-10 my-5 gap-60">
    <div class="flex-1 grid grid-cols-[95px_1fr_1fr] gap-4 min-w-0">
      <div class="flex items-center justify-center min-w-0">
        <p class="flex-1 text-xl font-bold text-[#F2EFEF] text-left min-w-0">Sort By</p>
      </div>

      <select
        class="text-xl font-bold text-[#F2EFEF] bg-[#434343] border border-[#868484] rounded-sm min-w-0"
      >
        <option value="Title">Title</option>
        <option value="Genre">Genre</option>
        <option value="Author">Author</option>
        <option value="Pages">Pages</option>
        <option value="Read Status">Read Status</option>
      </select>

      <select
        class="text-xl font-bold text-[#F2EFEF] bg-[#434343] border border-[#868484] rounded-sm min-w-0"
      >
        <option value="Ascending">Ascending</option>
        <option value="Descending">Descending</option>
      </select>
    </div>

    <div class="flex-1 grid grid-cols-[95px_1fr_1fr] gap-4 min-w-0">
      <div class="flex items-center justify-center min-w-0">
        <p class="flex-1 text-xl font-bold text-[#F2EFEF] text-left min-w-0">Search By</p>
      </div>

      <select
        class="text-xl font-bold text-[#F2EFEF] bg-[#434343] border border-[#868484] rounded-sm min-w-0"
      >
        <option value="Title">Title</option>
        <option value="Genre">Genre</option>
        <option value="Author">Author</option>
        <option value="Pages">Pages</option>
        <option value="Read Status">Read Status</option>
      </select>

      <input
        type="search"
        placeholder="Search..."
        class="text-xl font-bold text-[#F2EFEF] rounded border border-gray-300 min-w-0 pl-1.5"
      />
    </div>
  </div>
</template>
