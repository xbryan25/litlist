<script setup lang="ts">
import { ref, type Ref, watch } from 'vue'
import debounce from 'lodash.debounce'

const totalRows: number = 0
const totalPages: number = 20
const currentPageNumber: Ref<number | null> = ref(null)

const goToNextPage = () => {
  if (!currentPageNumber.value) {
    currentPageNumber.value = 2
  } else if (currentPageNumber.value && currentPageNumber.value! <= totalPages) {
    currentPageNumber.value!++
  }

  emitPageNumber()
}

const goToPreviousPage = () => {
  if (!currentPageNumber.value) {
    currentPageNumber.value = 1
  } else if (currentPageNumber.value && currentPageNumber.value! > 1) {
    currentPageNumber.value!--
  }

  emitPageNumber()
}

const goToFirstPage = () => {
  currentPageNumber.value = 1

  emitPageNumber()
}

const goToLastPage = () => {
  currentPageNumber.value = totalPages

  emitPageNumber()
}

const goToSpecificPage = () => {
  if (currentPageNumber.value! < 1 && currentPageNumber.value) {
    currentPageNumber.value = 1
  } else if (currentPageNumber.value! > totalPages) {
    currentPageNumber.value = totalPages
  }

  emitPageNumber()
}

const emitPageNumber = debounce(() => {
  // if currentPageNumber is 0, then emit 1

  console.log(currentPageNumber.value)
}, 200)

watch(currentPageNumber, () => {
  goToSpecificPage()
})
</script>

<template>
  <div class="flex h-8 mt-5 mb-5 justify-center items-center">
    <div class="flex h-8 gap-2 max-w-full">
      <button
        @click="goToFirstPage"
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/first-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>
      <button
        @click="goToPreviousPage"
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/prev-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>

      <input
        v-model="currentPageNumber"
        type="number"
        min="0"
        max="9999999"
        id="number"
        name="number"
        :placeholder="`${currentPageNumber ? String(currentPageNumber) : '1'}`"
        class="flex-1 font-primary w-15 border rounded text-[#D9D9D9] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none hover:bg-[#2e2e2e] ml-3 text-xl pl-1 pr-1"
      />

      <div class="flex flex-1 items-center mr-3 w-full">
        <p
          class="font-primary text-white text-center w-full text-xl whitespace-nowrap overflow-x-auto"
        >
          of {{ totalPages }}
        </p>
      </div>

      <button
        @click="goToNextPage"
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/next-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>
      <button
        @click="goToLastPage"
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/last-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>
    </div>
  </div>
</template>
