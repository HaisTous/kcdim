<template>
  <main>
    <h2 class="title">Значения и типы</h2>
    <p class="mb-4">
      <span class="font-semibold italic">Значение</span> — это одно из основных понятий, с которым работает программа,
      например буква или цифра. Например, значения: <code>2</code>, <code>42.0</code> и <code>"Привет, мир!"</code>
    </p>
    <p class="mb-4">
      Эти значения принадлежат разному <span class="font-semibold italic">типу</span>: <code>2</code> — это
      <span class="font-semibold italic">целое число</span> (<code class="code">int</code>), <code>42.0</code> —
      <span class="font-semibold italic">число с плавающей точкой (вещественное число)</span> (<code>float</code>), а
      <code>"Привет, мир!"</code> — <span class="font-semibold italic">строка</span> (<code>str</code>).
    </p>
    <p>
      А как насчет таких значений, как <code>"2"</code> и <code>"42.0"</code>?
      Они выглядят как числа, но указаны в кавычках как строки. Интерпретатор определяет их как строки.
    </p>
  </main>
</template>

<script>
export default {
  name: "ValueTypes"
}
</script>

<style scoped>

</style>