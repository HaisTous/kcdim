<template>
  <main>
    <div v-for="section in sections" key="{{ section.id }}">
      <h2
          :data-section="section.link"
          :id="section.link"
          class="title section">
        {{ section.name }}
      </h2>
      <div class="event" v-for="event in section.events" key="{{ event.id }}">
        <p class="event__description">{{ event.description }}</p>
        <div class="event__results">
          <a :href="event.resultsLink" target="_blank">Результаты:</a>
          <ul>
            <li v-for="winner in event.winners">{{ winner }}</li>
          </ul>
        </div>
        <div v-if="event.diplomas.length > 0" class="event__diplomas">
          <a
              :href="getImageUrl(diploma)"
              target="_blank"
              v-for="diploma in event.diplomas">
            <img :src="getImageUrl(diploma)" alt="Диплом">
          </a>
        </div>
      </div>
    </div>
  </main>
  <side-bar :sections="sections"/>
</template>

<script>
import SideBar from "@/components/SideBar.vue";

export default {
  name: "Home",
  components: {SideBar},
  data() {
    return {
      sections: [
        {
          id: 1,
          name: '2022-2023 гг.',
          link: '2022-2023',
          events: [
            {
              id: 8,
              description: '23-24 февраля 2023 года состоялся "Февральский Кубок" для учеников 3-7 класса.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1tmeTKVw5BFq36yrvucaCbDSXnwKCvm6G1GV6UEWW-U8/edit#gid=0',
              winners: [
                'Смолечков Матвей - Диплом 3 степени',
                'Воронов Прохор - Сертификат участника',
                'Трифонов Ярослав - Сертификат участника',
              ],
              diplomas: [
                'smolechkov-24022023.webp',
                'voronov-24022023.webp',
                'trifonov-2402023.webp',
              ],
            },
            {
              id: 7,
              description: '4 января 2023 года прошёл первый тур Кубка по программированию Светлогорского района.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1RgYLhwUKn5Ing4NgaHzC4B0uOchfIBsDv1WGlma5E94/edit#gid=0',
              winners: [
                'Смолечков Матвей - проход в финал',
                'Трифонов Ярослав - проход в финал',
                'Клименок Глеб - проход в финал',
                'Дайнеко Матвей - проход в финал',
                'Шипневский Иван - проход в финал',
              ],
              diplomas: [
              ],
            },
            {
              id: 6,
              description: '17-18 декабря 2022 года состоялся Первый отборочный тур X Открытой олимпиады по программированию для учащихся 1-4 класса.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1ZpaVa4_RhWbgaW02Yp8tDEl1R26-EMrwxk7B1sQ3tFU/edit#gid=0',
              winners: [
                'Дыгун Станислав - Похвальный лист',
              ],
              diplomas: [
                'dygun-17122022.webp',
              ],
            },
            {
              id: 5,
              description: '17-18 декабря 2022 года состоялся "Декабрьский Кубок" для учеников 3-7 класса.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1uArrJ4mpQ0xckS18EezQpS3v3NS-4LnaXvQFd8GtUCU/edit#gid=0',
              winners: [
                'Смолечков Матвей - Диплом 3 степени',
              ],
              diplomas: [
                'smolechkov-17122022.webp',
              ],
            },
            {
              id: 4,
              description: '12 ноября 2022 года состоялся второй этап Республиканской олимпиады по информатике.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1le4qvs1XgKZxsXZLcDa9naL7mK4beHrH/edit#gid=1466457640',
              winners: [
                'Дыгун Станислав - Диплом 2 степени',
                'Шипневский Иван - Диплом 3 степени',
              ],
              diplomas: [
              ],
            },
            {
              id: 3,
              description: '4 ноября 2022 состоялись районные соревнования по программированию.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1P-Uuejn8T_nIZkI_QLy3rCDSQO9b-bukccFS9Q4ea50/edit#gid=0',
              winners: [
                'Смолечков Матвей - Диплом 1 степени',
                'Дайнеко Матвей - Диплом 2 степени',
                'Дыгун Станислав - Диплом 2 степени',
                'Воронов Прохор - Диплом 3 степени',
                'Трифонов Ярослав - Диплом 3 степени',
                'Шипневский Иван - Диплом 3 степени',
              ],
              diplomas: [
                'smolechkov-04112022.webp',
                'dayneko-04112022.webp',
                'dygun-04112022.webp',
                'voronov-04112022.webp',
                'trifonov-04112022.webp',
                'shipnevsky-04112022.webp',
              ],
            },
            {
              id: 2,
              description: '29-30 октября 2022 года прошла Санкт-Петербургская открытая олимпиада для 3-7 классов "Осенний программист".',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1eD8xDAol2Ick8ozChDLH4erZj6Tq5MlhNu1XAr_gpBA/edit#gid=0',
              winners: [
                'Смолечков Матвей - Диплом 3 степени',
              ],
              diplomas: [
                'smolechkov-30102022.webp',
              ],
            },
            {
              id: 1,
              description: '17 сентября 2022 года состоялась областная Интернет-олимпиада по информатике.',
              resultsLink: 'https://docs.google.com/spreadsheets/d/1z0mnVBlFyRu9cj4WCB2414k-EDmWzvt9/edit#gid=1913548864',
              winners: [
                'Шипневский Иван - Диплом 2 степени',
                'Коваль Максим - Диплом 3 степени',
              ],
              diplomas: [
                'shipnevsky-17092022.webp',
                'koval-17092022.webp',
              ],
            },
          ],
        },
      ]
    }
  },
  methods: {
    getImageUrl(name) {
      return new URL(`/src/assets/diplomas/${name}`, import.meta.url).href
    }
  }
}

</script>

<style scoped>
.event {
  @apply border-b-2 border-gray-300 mb-4 last:border-b-0
  dark:border-gray-700;
}

.event__description {
  @apply italic;
}

.event__results {
  @apply my-4;
}

.event__results a {
  @apply hover:text-red-500;
}

.event__results ul {
  @apply font-bold;
}

.event__diplomas {
  @apply flex flex-row justify-center gap-4 flex-wrap my-4;
}

.event__diplomas a {
  @apply hover:scale-110 ease-linear duration-300;
}

.event__diplomas img {
  @apply w-32 h-auto;
}
</style>