<template>
  <main>
    <h2 class="title">Ссылки</h2>
    <ol>
      <li v-for="link in links" :key="link.id">
        <a :href="link.link" target="_blank">
          {{ link.name }}
        </a>
      </li>
    </ol>
  </main>
</template>

<script>
export default {
  name: "Links",
  data() {
    return {
      links: [
        {
          id: 1,
          link: 'https://www.programiz.com/python-programming/online-compiler/',
          name: 'Онлайн компилятор Python'
        },
        {
          id: 2,
          link: 'https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe',
          name: 'Скачать Python 3.11.2'
        },
        {
          id: 3,
          link: 'https://wingware.com/get&prod=wing-101&target=pub/wing-101/9.0.2.1/wing-101-9.0.2.1.exe',
          name: 'Скачать Wing 9.0.2'
        },
        {
          id: 4,
          link: 'https://codeforces.com/',
          name: 'Codeforces'
        },
        {
          id: 5,
          link: 'https://www.eolymp.com/ru/',
          name: 'eolymp'
        },
      ],
    }
  },
}
</script>

<style scoped>

</style>