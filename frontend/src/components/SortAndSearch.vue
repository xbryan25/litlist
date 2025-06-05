<script setup lang="ts">
import { defineEmits, ref, type Ref, watch } from 'vue'
import debounce from 'lodash.debounce'

const emit = defineEmits<{
  (
    e: 'sort',
    payload: { sortType: string; sortBy: string; searchType: string; searchInput: string },
  ): void
  (
    e: 'search',
    payload: { sortType: string; sortBy: string; searchType: string; searchInput: string },
  ): void
}>()

const selectedSortType: Ref<string> = ref('Title')
const selectedSortBy: Ref<string> = ref('Ascending')

const selectedSearchType: Ref<string> = ref('All')
const searchInput: Ref<string> = ref('')

const handleSortChange = () => {
  // console.log(`Selected: ${selectedSortType.value} ${selectedSortBy.value}`)
  emit('sort', {
    sortType: selectedSortType.value,
    sortBy: selectedSortBy.value,
    searchType: selectedSearchType.value,
    searchInput: searchInput.value,
  })
}

const handleSearchChange = debounce(() => {
  emit('search', {
    sortType: selectedSortType.value,
    sortBy: selectedSortBy.value,
    searchType: selectedSearchType.value,
    searchInput: searchInput.value,
  })
}, 400)

watch(searchInput, () => {
  handleSearchChange()
})
</script>

<template>
  <div class="flex max-h-10 h-10 my-5 gap-60">
    <div class="flex-1 grid grid-cols-[95px_1fr_1fr] gap-4 min-w-0">
      <div class="flex items-center justify-center min-w-0">
        <p class="font-primary flex-1 text-xl font-bold text-[#F2EFEF] text-left min-w-0">
          Sort By
        </p>
      </div>

      <select
        v-model="selectedSortType"
        @change="handleSortChange"
        class="font-primary text-xl font-bold text-[#F2EFEF] bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e]"
      >
        <option value="Title">Title</option>
        <option value="Genre">Genre</option>
        <option value="Author">Author</option>
        <option value="Pages">Pages</option>
        <option value="Read Status">Read Status</option>
      </select>

      <select
        v-model="selectedSortBy"
        @change="handleSortChange"
        class="font-primary text-xl font-bold text-[#F2EFEF] bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e]"
      >
        <option value="Ascending">Ascending</option>
        <option value="Descending">Descending</option>
      </select>
    </div>

    <div class="flex-1 grid grid-cols-[95px_1fr_1fr] gap-4 min-w-0">
      <div class="flex items-center justify-center min-w-0">
        <p class="font-primary flex-1 text-xl font-bold text-[#F2EFEF] text-left min-w-0">
          Search By
        </p>
      </div>

      <select
        v-model="selectedSearchType"
        class="font-primary text-xl font-bold text-[#F2EFEF] bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e]"
      >
        <option value="All">All</option>
        <option value="Title">Title</option>
        <option value="Genre">Genre</option>
        <option value="Author">Author</option>
        <option value="Pages">Pages</option>
        <option value="Read Status">Read Status</option>
      </select>

      <input
        v-model="searchInput"
        @change="handleSearchChange"
        type="search"
        placeholder="Search..."
        class="font-primary text-xl font-bold text-[#F2EFEF] rounded border border-gray-300 min-w-0 pl-1.5 hover:bg-[#2e2e2e]"
      />
    </div>
  </div>
</template>
