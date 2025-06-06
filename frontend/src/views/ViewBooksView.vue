<script setup lang="ts">
import { ref, type Ref } from 'vue'
import Table from '@/components/Table.vue'
import SortAndSearch from '@/components/SortAndSearch.vue'
import PageControls from '@/components/PageControls.vue'
import { getEffectiveTypeParameterDeclarations } from 'typescript'
// import NavBar from '@/components/NavBar.vue'

const selectedSortType: Ref<string> = ref('Title')
const selectedSortBy: Ref<string> = ref('Ascending')

const selectedSearchType: Ref<string> = ref('All')
const searchInput: Ref<string> = ref('')

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
</script>

<template>
  <div class="mx-40 mt-15">
    <SortAndSearch @sort="updateValues" @search="updateValues" />
    <Table
      :sortType="selectedSortType"
      :sortBy="selectedSortBy"
      :searchType="selectedSearchType"
      :searchInput="searchInput"
    />
    <PageControls />
  </div>
</template>
