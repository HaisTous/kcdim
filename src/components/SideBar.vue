<template>
  <aside class="sidebar">
    <h3>На этой странице</h3>
    <nav class="sidebar-nav">
      <ul>
        <li
            v-for="section in sections"
            :data-section="section.link"
            class="sidebar-nav__li">
          <router-link :to="`#${section.link}`">{{ section.name }}</router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
import '@/assets/nav.js'
export default {
  name: "SideBar",
  props: {
    sections: {
      type: Array,
      required: true,
    },
  }
}
</script>

<style scoped>
aside.sidebar {
  @apply w-80 flex-shrink-0 hidden rounded-lg px-6 py-3 sticky top-16 md:block bg-gray-100 text-gray-700
  dark:bg-slate-900 dark:text-gray-300;
}

aside.sidebar h3 {
  @apply text-sm font-semibold tracking-wide text-gray-900 uppercase mb-4
  dark:text-gray-100
}

aside.sidebar > nav > ul > li {
  @apply py-1;
}

aside.sidebar > nav > ul > li > a {
  @apply pl-4 border-l-4 border-transparent;
}

aside.sidebar > nav > ul > li > a:hover {
  @apply border-rose-700 text-rose-700
  dark:border-rose-400 dark:text-rose-400;
}

aside.sidebar > nav > ul > li.sidebar-nav__active > a {
  @apply border-l-4 border-rose-700 text-rose-700 transition-none duration-200
  dark:border-rose-400 dark:text-rose-400;
}
</style>