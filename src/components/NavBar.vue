<template>
  <nav class="menu">
    <ul >
      <li v-for="router in routers" :key="router.id">
        <router-link :to="router.link">
          {{ router.name }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      routers: [
        {id: 1, link: '/topics', name: 'Темы'},
        {id: 2, link: '/students', name: 'Учащиеся'},
        {id: 3, link: '/events', name: 'Олимпиады'},
        {id: 4, link: '/links', name: 'Ссылки'},
      ],
    }
  },
}
</script>

<style scoped>
.menu {
  @apply flex;
}

.menu ul {
  @apply flex flex-row font-medium space-x-6 lg:space-x-10;
}

.menu a {
  @apply hover:text-red-500;
}

a.router-link-exact-active {
  @apply text-red-500;
}
</style>