<template>
  <header>
    <div class="header">
      <logo-kcdim/>
      <nav-bar/>
      <dark-mode/>
    </div>
  </header>
  <div class="wrapper">
    <router-view></router-view>
  </div>
</template>

<script>
import LogoKcdim from "@/components/LogoKcdim.vue";
import NavBar from "@/components/NavBar.vue";
import DarkMode from "@/components/DarkMode.vue";

export default {
  components: {
    DarkMode,
    LogoKcdim,
    NavBar,

  },
}
</script>

<style>
.header {
  @apply flex flex-row justify-between items-center flex-wrap mx-auto max-w-screen-xl px-2;
}

.wrapper {
  @apply flex flex-row items-start mx-auto max-w-screen-xl gap-2 px-2;
}


h2.title {
  @apply uppercase text-lg font-bold text-gray-900 mb-4
  dark:text-gray-100;
}

.stripped-table {
  @apply relative overflow-x-auto rounded-lg;
}

.stripped-table table {
  @apply w-full text-sm text-center text-gray-700
  dark:text-gray-300;
}

.stripped-table thead {
  @apply text-xs uppercase text-gray-900 bg-gray-300
  dark:text-gray-100 dark:bg-gray-800;
}

.stripped-table th, .stripped-table td {
  @apply px-4 py-2;
}

.stripped-table .name {
  @apply font-medium text-gray-900 whitespace-nowrap text-left
  dark:text-gray-100;
}

.stripped-table tbody tr:nth-child(even) {
  @apply border-b bg-gray-200
  dark:bg-slate-800 dark:border-gray-700;
}

.stripped-table tbody tr:nth-child(odd) {
  @apply bg-white bg-gray-100
  dark:bg-slate-700 dark:border-slate-600;
}

.line-number {
  @apply inline-block w-12 text-gray-500;
}

.number {
  @apply text-orange-600
  dark:text-orange-400;
}

.string {
  @apply text-green-600
  dark:text-green-400;
}

.function {
  @apply text-blue-600
  dark:text-blue-400;
}

.method {
  @apply text-cyan-600
  dark:text-cyan-400;
}

.statement {
  @apply text-fuchsia-600
  dark:text-fuchsia-400;
}

.comment {
  @apply text-gray-500;
}

.tab1 {
  @apply ml-8;
}

.tab2 {
  @apply ml-16;
}

.block-link {
  @apply inline-flex items-center justify-center p-3 text-base font-medium rounded-lg my-4
  text-gray-100 bg-gradient-to-br from-pink-500 to-orange-400 hover:bg-gradient-to-bl;
}

.disabled-block-link {
  @apply inline-flex items-center justify-center p-3 text-base font-medium rounded-lg my-4
  text-gray-100 bg-gradient-to-br from-gray-500 to-neutral-400;
}
</style>
