<script setup lang="ts">
import { ref, type Ref, watch, defineEmits, defineProps } from 'vue'
import debounce from 'lodash.debounce'

interface Props {
  totalPages?: number
}

const props = withDefaults(defineProps<Props>(), {
  totalPages: 1,
})

const currentPageNumber: Ref<number | null> = ref(null)

const emit = defineEmits<{
  (e: 'pageChanged', payload: { pageNumber: number | null }): void
}>()

const goToNextPage = () => {
  if (!currentPageNumber.value) {
    currentPageNumber.value = 2
  } else if (currentPageNumber.value && currentPageNumber.value! <= props.totalPages) {
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
  currentPageNumber.value = props.totalPages

  emitPageNumber()
}

const goToSpecificPage = () => {
  if (currentPageNumber.value! < 1 && currentPageNumber.value) {
    currentPageNumber.value = 1
  } else if (currentPageNumber.value! > props.totalPages) {
    currentPageNumber.value = props.totalPages
  }

  emitPageNumber()
}

const emitPageNumber = debounce(() => {
  let tempPageNumber: number

  if (!currentPageNumber.value) {
    tempPageNumber = 1
  } else {
    tempPageNumber = currentPageNumber.value
  }

  emit('pageChanged', {
    pageNumber: tempPageNumber,
  })
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
        class="dark:bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img
          src="@/assets/images/first-page-light-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto hidden dark:block"
        />
        <img
          src="@/assets/images/first-page-dark-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto block dark:hidden"
        />
      </button>
      <button
        @click="goToPreviousPage"
        class="dark:bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img
          src="@/assets/images/prev-page-light-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto hidden dark:block"
        />
        <img
          src="@/assets/images/prev-page-dark-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto block dark:hidden"
        />
      </button>

      <input
        v-model="currentPageNumber"
        type="number"
        min="0"
        max="9999999"
        id="number"
        name="number"
        :placeholder="`${currentPageNumber ? String(currentPageNumber) : '1'}`"
        class="flex-1 font-primary w-15 border rounded text-black dark:text-[#D9D9D9] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none dark:hover:bg-[#2e2e2e] ml-3 text-xl pl-1 pr-1"
      />

      <div class="flex flex-1 items-center mr-3 w-full">
        <p
          class="font-primary text-black dark:text-white text-center w-full text-xl whitespace-nowrap overflow-x-auto"
        >
          of {{ props.totalPages }}
        </p>
      </div>

      <button
        @click="goToNextPage"
        class="dark:bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img
          src="@/assets/images/next-page-light-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto hidden dark:block"
        />
        <img
          src="@/assets/images/next-page-dark-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto block dark:hidden"
        />
      </button>
      <button
        @click="goToLastPage"
        class="dark:bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img
          src="@/assets/images/last-page-light-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto hidden dark:block"
        />
        <img
          src="@/assets/images/last-page-dark-mode.svg"
          alt="Logo"
          class="w-[30px] h-auto block dark:hidden"
        />
      </button>
    </div>
  </div>
</template>
