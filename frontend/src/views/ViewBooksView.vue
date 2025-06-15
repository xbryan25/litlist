<script setup lang="ts">
import { ref, type Ref } from 'vue'
import ContentTable from '@/components/ContentTable.vue'
import SortAndSearch from '@/components/SortAndSearch.vue'
import PageControls from '@/components/PageControls.vue'

const selectedSortType: Ref<string> = ref('Title')
const selectedSortBy: Ref<string> = ref('Ascending')

const selectedSearchType: Ref<string> = ref('All')
const searchInput: Ref<string> = ref('')

const currentTotalPages: Ref<number> = ref(1)
const currentPageNumber: Ref<number | null> = ref(1)

const updateValues = (params: {
  sortType: string
  sortBy: string
  searchType: string
  searchInput: string
}) => {
  selectedSortType.value = params.sortType
  selectedSortBy.value = params.sortBy
  selectedSearchType.value = params.searchType
  searchInput.value = params.searchInput
}

const updatePageNumber = (params: { pageNumber: number | null }) => {
  currentPageNumber.value = params.pageNumber
}

const updateTotalPages = (params: { totalPages: number }) => {
  currentTotalPages.value = params.totalPages
}
</script>

<template>
  <div class="flex flex-col h-[calc(100vh-80px)] mx-40 pt-10">
    <SortAndSearch @sort="updateValues" @search="updateValues" />
    <ContentTable
      :sortType="selectedSortType"
      :sortBy="selectedSortBy"
      :searchType="selectedSearchType"
      :searchInput="searchInput"
      :currentPageNumber="currentPageNumber"
      @totalPages="updateTotalPages"
    />
    <PageControls :totalPages="currentTotalPages" @pageChanged="updatePageNumber" />
  </div>
</template>
