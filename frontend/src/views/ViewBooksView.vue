<script setup lang="ts">
import { ref, type Ref } from 'vue'
import Table from '@/components/Table.vue'
import SortAndSearch from '@/components/SortAndSearch.vue'
// import NavBar from '@/components/NavBar.vue'

const selectedSortType: Ref<string> = ref('')
const selectedSortBy: Ref<string> = ref('')

const handleDelete = (params: { sortType: string; sortBy: string }) => {
  // console.log('')
  // console.log(`Selected: ${params.sortType} ${params.sortBy}`)

  selectedSortType.value = params.sortType
  selectedSortBy.value = params.sortBy
}
</script>

<template>
  <div class="mx-40 mt-15">
    <SortAndSearch @sort="handleDelete" />
    <Table :sortType="selectedSortType" :sortBy="selectedSortBy" />
  </div>
</template>
