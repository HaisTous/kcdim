<template>
  <main>
    <h2 class="title">Список учащихся</h2>
    <p class="updated_date">Последнее обновление: {{ date }}</p>
    <div class="stripped-table">
      <table>
        <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col" class="text-left">Учащийся</th>
          <th scope="col" v-for="topic in topics" :key="topic.id">
            <a :href="topic.link" class="tooltip group">{{ topic.id }}
              <span class="tooltip-text">{{ topic.name }}</span>
            </a>
          </th>
          <th scope="col">Всего</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(student, num) in students" :key="student.id">
          <td>{{ num + 1 }}</td>
          <th scope="row" class="name">{{ student.name }}</th>
          <td v-for="score in student.scores">{{ score }}</td>
          <td>{{ student.totalScore }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script>
export default {
  name: "Students",
  data() {
    return {
      date: '13 марта 2023 года в 16:52',
      topics: [
        {'id': 1, 'link': 'topics/data-output.html', 'name': 'Вывод данных'},
        {'id': 2, 'link': 'topics/data-input.html', 'name': 'Ввод данных'},
        {'id': 3, 'link': 'topics/arithmetic.html', 'name': 'Арифметические операции'},
        {'id': 4, 'link': 'topics/condition.html', 'name': 'Условный оператор'},
        {'id': 5, 'link': 'topics/loops.html', 'name': 'Операторы цикла'},
      ],
      students: [
        {'id': 1, 'name': 'Шипневский Иван, 9 кл', 'scores': [16, 15, 30, 50, 35,], 'totalScore': 146},
        {'id': 2, 'name': 'Коваль Максим, 9 кл', 'scores': [16, 15, 30, 50, 35,], 'totalScore': 146},
        {'id': 3, 'name': 'Коцур Александр, 8 кл', 'scores': [16, 15, 30, 50, 12,], 'totalScore': 123},
        {'id': 4, 'name': 'Смолечков Матвей, 5 кл', 'scores': [16, 15, 30, 41, 11,], 'totalScore': 113},
        {'id': 5, 'name': 'Бута Андрей, 7 кл', 'scores': [16, 15, 30, 49, 0,], 'totalScore': 110},
        {'id': 6, 'name': 'Гудыменко Иван, 6 кл', 'scores': [16, 15, 30, 44, 0,], 'totalScore': 105},
        {'id': 7, 'name': 'Рогов Егор, 5 кл', 'scores': [16, 15, 30, 42, 0,], 'totalScore': 103},
        {'id': 8, 'name': 'Джумагазиев Алан, 5 кл', 'scores': [16, 15, 30, 41, 0,], 'totalScore': 102},
        {'id': 9, 'name': 'Ковалёв Даниил, 6 кл', 'scores': [16, 15, 30, 36, 0,], 'totalScore': 97},
        {'id': 10, 'name': 'Клименок Глеб, 5 кл', 'scores': [16, 15, 30, 33, 0,], 'totalScore': 94},
        {'id': 11, 'name': 'Зотов Илья, 8 кл', 'scores': [16, 15, 30, 26, 0,], 'totalScore': 87},
        {'id': 12, 'name': 'Шенец Ростислав, 5 кл', 'scores': [16, 15, 30, 26, 0,], 'totalScore': 87},
        {'id': 13, 'name': 'Трифонов Ярослав, 5 кл', 'scores': [16, 15, 30, 25, 0,], 'totalScore': 86},
        {'id': 14, 'name': 'Петерюхин Дамир, 5 кл', 'scores': [16, 15, 30, 25, 0,], 'totalScore': 86},
        {'id': 15, 'name': 'Граюшев Глеб, 5 кл', 'scores': [16, 13, 30, 27, 0,], 'totalScore': 86},
        {'id': 16, 'name': 'Беспалько Максим, 6 кл', 'scores': [16, 15, 30, 25, 0,], 'totalScore': 86},
        {'id': 17, 'name': 'Козырев Кирилл, 6 кл', 'scores': [16, 15, 30, 22, 0,], 'totalScore': 83},
        {'id': 18, 'name': 'Лещик Тимур, 5 кл', 'scores': [16, 15, 30, 21, 0,], 'totalScore': 82},
        {'id': 19, 'name': 'Кострома Владимир, 6 кл', 'scores': [16, 15, 30, 15, 0,], 'totalScore': 76},
        {'id': 20, 'name': 'Шевеленко Арсений, 8 кл', 'scores': [16, 15, 30, 15, 0,], 'totalScore': 76},
        {'id': 21, 'name': 'Воронов Прохор, 5 кл', 'scores': [16, 15, 30, 12, 0,], 'totalScore': 73},
        {'id': 22, 'name': 'Крук Михаил, 9 кл', 'scores': [16, 10, 15, 27, 3,], 'totalScore': 71},
        {'id': 23, 'name': 'Радченко Никита, 8 кл', 'scores': [16, 15, 30, 9, 0,], 'totalScore': 70},
        {'id': 24, 'name': 'Крышнев Иван, 6 кл', 'scores': [16, 15, 30, 7, 0,], 'totalScore': 68},
        {'id': 25, 'name': 'Брундуков Дмитрий, 6 кл', 'scores': [16, 15, 30, 4, 0,], 'totalScore': 65},
        {'id': 26, 'name': 'Жигунов Константин, 6 кл', 'scores': [16, 15, 30, 0, 0,], 'totalScore': 61},
        {'id': 27, 'name': 'Сологубов Максим, 6 кл', 'scores': [16, 15, 25, 4, 0,], 'totalScore': 60},
        {'id': 28, 'name': 'Донкин Александр, 6 кл', 'scores': [16, 15, 26, 0, 0,], 'totalScore': 57},
        {'id': 29, 'name': 'Глушец Ярослав, 9 кл', 'scores': [16, 15, 24, 0, 0,], 'totalScore': 55},
        {'id': 30, 'name': 'Рудой Фёдор, 6 кл', 'scores': [16, 15, 23, 0, 0,], 'totalScore': 54},
        {'id': 31, 'name': 'Журавский Тимофей, 6 кл', 'scores': [16, 15, 23, 0, 0,], 'totalScore': 54},
        {'id': 32, 'name': 'Дыгун Станислав, 4 кл', 'scores': [16, 15, 22, 0, 0,], 'totalScore': 53},
        {'id': 33, 'name': 'Поляк Артём, 5 кл', 'scores': [16, 15, 21, 0, 0,], 'totalScore': 52},
        {'id': 34, 'name': 'Сувалов Андрей, 5 кл', 'scores': [16, 15, 16, 0, 0,], 'totalScore': 47},
        {'id': 35, 'name': 'Сологубов Артём, 6 кл', 'scores': [16, 15, 14, 0, 0,], 'totalScore': 45},
        {'id': 36, 'name': 'Мигай Глеб, 4 кл', 'scores': [16, 15, 12, 0, 0,], 'totalScore': 43},
        {'id': 37, 'name': 'Гошко Владислав, 6 кл', 'scores': [16, 15, 8, 0, 0,], 'totalScore': 39},
        {'id': 38, 'name': 'Смажевский Павел, 5 кл', 'scores': [16, 14, 7, 0, 0,], 'totalScore': 37},
        {'id': 39, 'name': 'Дробышевский Тимофей, 5 кл', 'scores': [16, 15, 5, 0, 0,], 'totalScore': 36},
        {'id': 40, 'name': 'Коваль Лев, 7 кл', 'scores': [16, 15, 0, 0, 0,], 'totalScore': 31},
        {'id': 41, 'name': 'Смолечков Дмитрий, 2 кл', 'scores': [16, 15, 0, 0, 0,], 'totalScore': 31},
        {'id': 42, 'name': 'Кожедуб Александр, 6 кл', 'scores': [16, 12, 0, 0, 0,], 'totalScore': 28},
        {'id': 43, 'name': 'Медведев Василий, 6 кл', 'scores': [16, 8, 0, 0, 0,], 'totalScore': 24},
        {'id': 44, 'name': 'Кисляков Владислав, 7 кл', 'scores': [16, 5, 0, 0, 0,], 'totalScore': 21},
        {'id': 45, 'name': 'Сидоренко Кира, 4 кл', 'scores': [16, 2, 0, 0, 0,], 'totalScore': 18},
        {'id': 46, 'name': 'Тымчишин Даниил, 6 кл', 'scores': [16, 1, 0, 0, 0,], 'totalScore': 17},
        {'id': 47, 'name': 'Матвеенко Дарья, 5 кл', 'scores': [16, 1, 0, 0, 0,], 'totalScore': 17},
        {'id': 48, 'name': 'Ромась Глеб, 5 кл', 'scores': [16, 0, 0, 0, 0,], 'totalScore': 16},
        {'id': 49, 'name': 'Дайнеко  Сергей, 6 кл', 'scores': [16, 0, 0, 0, 0,], 'totalScore': 16},
        {'id': 50, 'name': 'Семёнов Алексей, 4 кл', 'scores': [16, 0, 0, 0, 0,], 'totalScore': 16},
        {'id': 51, 'name': 'Тимофеев Назар, 5 кл', 'scores': [16, 0, 0, 0, 0,], 'totalScore': 16},
        {'id': 52, 'name': 'Филипчик Матвей, 5 кл', 'scores': [16, 0, 0, 0, 0,], 'totalScore': 16},
        {'id': 53, 'name': 'Друзик Никита, 4 кл', 'scores': [16, 0, 0, 0, 0,], 'totalScore': 16},
        {'id': 54, 'name': 'Гайшун Дарья, 9 кл', 'scores': [15, 1, 0, 0, 0,], 'totalScore': 16},
        {'id': 55, 'name': 'Лёгенький Андрей, 6 кл', 'scores': [14, 0, 0, 0, 0,], 'totalScore': 14},
        {'id': 56, 'name': 'Жолик Артём, 5 кл', 'scores': [14, 0, 0, 0, 0,], 'totalScore': 14},
        {'id': 57, 'name': 'Лобанов Сергей, 4 кл', 'scores': [11, 0, 0, 0, 0,], 'totalScore': 11},
        {'id': 58, 'name': 'Асадчий Артём, 6 кл', 'scores': [10, 0, 0, 0, 0,], 'totalScore': 10},
        {'id': 59, 'name': 'Друзик Алексей, 4 кл', 'scores': [9, 0, 0, 0, 0,], 'totalScore': 9},
        {'id': 60, 'name': 'Храповский Алексей, 5 кл', 'scores': [8, 0, 0, 0, 0,], 'totalScore': 8},
        {'id': 61, 'name': 'Зиболис Ренат, 4 кл', 'scores': [7, 0, 0, 0, 0,], 'totalScore': 7},
        {'id': 62, 'name': 'Климов Артём, 3 кл', 'scores': [6, 0, 0, 0, 0,], 'totalScore': 6},
        {'id': 63, 'name': 'Тукач Максим, 5 кл', 'scores': [5, 0, 0, 0, 0,], 'totalScore': 5},
        {'id': 64, 'name': 'Ринейский Кирилл, 5 кл', 'scores': [0, 0, 0, 0, 0,], 'totalScore': 0},
      ],
    }
  },
}
</script>

<style scoped>
.updated_date {
  @apply mb-4 text-right text-xs
  dark:text-gray-400;
}

.tooltip {
  @apply relative inline-block;
}

.tooltip-text {
  @apply invisible group-hover:visible group-hover:opacity-100 bg-gray-100 text-gray-900 text-center px-4 py-2
  rounded-md right-[105%] top-[-5px] absolute z-auto opacity-0 transition-opacity duration-700
  dark:bg-gray-900 dark:text-gray-100;
}
</style>