<template>
  <main>
    <h2 class="title">Ближайшие олимпиады</h2>
    <div class="stripped-table">
      <table>
        <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Начало</th>
          <th scope="col">Длительность</th>
          <th scope="col">Олимпиада</th>
          <th scope="col">Возрастная категория</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(event, index) in events" :key="event.id">
          <td>{{ index + 1 }}</td>
          <td>
            <p>{{ event.startDate }}</p>
            <p>{{ event.startTime }}</p>
          </td>
          <td>{{ event.duration }}</td>
          <th scope="row">
            <a v-if="event.link.length > 0" :href="event.link" class="hover:underline" target="_blank">
              {{ event.name }}
            </a>
            <span v-else>{{ event.name }}</span>
          </th>
          <td>
            <p v-for="category in event.ageCategories">{{ category }}</p>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      events: [
        {
          id: 1,
          startDate: '18.03.2023',
          startTime: '10:00',
          duration: '5 часов',
          name: 'Гомельская областная Интернет-олимпиада для 1-8 классов',
          link: 'https://dl.gsu.by/',
          ageCategories: ['1-4 классы', '5-8 классы']
        },
        {
          id: 2,
          startDate: '18.03.2023',
          startTime: '09:00',
          duration: '36 часов',
          name: 'Второй отборочный онлайн тур X Открытой олимпиады по программированию среди учащихся начальной школы',
          link: 'https://vk.com/olimp_prog_spb',
          ageCategories: ['1-4 классы']
        },
        {
          id: 3,
          startDate: '19.03.2023',
          startTime: '17:35',
          duration: '135 минут',
          name: 'Codeforces Round 858 (Div. 4)',
          link: 'https://codeforces.com/contests',
          ageCategories: ['Любой желающий']
        },
        {
          id: 4,
          startDate: '29.03.2023',
          startTime: '14:30',
          duration: '4 часа',
          name: 'Кубок Компьютерного центра 2023 - 2 отборочный раунд',
          link: 'https://www.eolymp.com/ru/contests/29462',
          ageCategories: ['1-5 классы', '6-8 классы', '9-11 классы']
        },
        {
          id: 5,
          startDate: '08.04.2023',
          startTime: '11:00',
          duration: 'до 5 часов',
          name: 'Второй этап областной олимпиады по информатике учащихся I-IX классов',
          link: '',
          ageCategories: ['1-4 классы (dl)', '5-7 классы (dl)', '8-9 классы (Яндекс)']
        },
        {
          id: 6,
          startDate: '20.04.2023',
          startTime: '',
          duration: 'до 5 часов',
          name: 'Третий этап областной олимпиады по информатике учащихся I-IX классов',
          link: '',
          ageCategories: ['1-4 классы (dl)', '5-7 классы (dl)', '8-9 классы (Яндекс)']
        },
        {
          id: 7,
          startDate: '27.05.2023',
          startTime: '',
          duration: 'до 5 часов',
          name: 'Кубок Компьютерного центра 2023 - Финал',
          link: '',
          ageCategories: ['1-5 классы', '6-8 классы', '9-11 классы']
        },
      ],
    }
  },
}
</script>

<style scoped>

</style>