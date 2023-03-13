<template>
  <button
      @click="toggleDark()"
  >
    <icon-dark-theme v-if="isDark"/>
    <icon-light-theme v-else/>
  </button>
</template>

<script setup>
import {useDark, useToggle} from "@vueuse/core";
import IconLightTheme from "@/components/icons/IconLightTheme.vue";
import IconDarkTheme from "@/components/icons/IconDarkTheme.vue";

const isDark = useDark({
  onChanged(isDark) {
    if (isDark) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }
})
const toggleDark = useToggle(isDark)
</script>

<style scoped>
button {
  @apply hover:bg-gray-200 rounded-lg p-2.5 block text-gray-500 text-sm
  dark:text-gray-400 dark:hover:bg-gray-700;
}
</style>