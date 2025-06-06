<script setup lang="ts"></script>

<template>
  <div class="flex h-8 mt-5 mb-5 justify-center items-center">
    <div class="flex h-8 gap-2 max-w-full">
      <button
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/first-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>
      <button
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/prev-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>

      <input
        type="number"
        min="1"
        max="9999999"
        id="number"
        name="number"
        class="flex-1 font-primary w-15 border rounded text-[#D9D9D9] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none hover:bg-[#2e2e2e] ml-3 text-xl"
      />

      <div class="flex flex-1 items-center mr-3 w-full">
        <p
          class="font-primary text-white text-center w-full text-xl whitespace-nowrap overflow-x-auto"
        >
          of 15123
        </p>
      </div>

      <button
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/next-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>
      <button
        class="bg-[#434343] border border-[#868484] rounded-sm min-w-0 cursor-pointer hover:bg-[#2e2e2e] inline-flex items-center justify-center"
      >
        <img src="@/assets/images/last-page.svg" alt="Logo" class="w-[30px] h-auto" />
      </button>
    </div>
  </div>
</template>
