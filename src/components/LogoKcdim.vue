<template>
  <router-link to="/" class="logo group">
    <img src="/src/assets/logo.png" alt="Логотип">
    <div class="logo__header">
      <h1>Компьютерный центр г. Светлогорска</h1>
      <p>Спортивное программирование</p>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "LogoKcdim"
}
</script>

<style scoped>
.logo {
  @apply flex items-center text-sm font-bold;
}

.logo img {
  @apply h-10 mr-3;
}

.logo__header {
  @apply hidden md:block group-hover:text-red-500;
}
</style>