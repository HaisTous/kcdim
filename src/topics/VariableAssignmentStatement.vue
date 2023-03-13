<template>
  <main>
    <h2 class="title">Вывод данных</h2>
    <p>Инструкция печати <code class="function">print</code> отображает результат на экране. На языке Python программа
      выглядит так:</p>
    <pre><code>
<span class="line-number">1</span><span class="function">print</span>(<span class="string">"Привет, мир!"</span>)</code></pre>
    <p>Это пример <span class="font-semibold italic">инструкции печати</span>, хотя на самом деле она ничего не печатает
      на бумаге. Она отображает результат на экране. В этом случае результатом будут следующие слова:</p>
    <pre><code>
<span class="line-number">>>></span>Привет, мир!</code></pre>
    <p>Кавычки в программе отмечают начало и конец отображаемого текста; они не видны в выводе. Скобки () указывают,
      что <code class="function">print</code> — это функция.</p>
    <h3 class="subtitle">f-строки</h3>
    <p><span class="font-semibold italic">f-строки</span> делают очень простую вещь — они берут значения переменных,
      которые есть в текущей области видимости, и подставляют их в строку. В самой строке вам лишь нужно указать имя
      этой переменной в фигурных скобках.</p>
    <pre><code>
<span class="line-number">1</span>name = <span class="string">"Дмитрий"</span>
<span class="line-number">2</span>age = <span class="number">13</span>
<span class="line-number">3</span><span class="function">print</span>(<span class="string">f"Меня зовут </span><span
        class="function">{</span>name<span class="function">}</span><span class="string">. Мне</span> <span
        class="function">{</span>age<span class="function">}</span><span class="string"> лет."</span>)</code></pre>
    <p>Результат:</p>
    <pre><code>
<span class="line-number">>>></span>Меня зовут Дмитрий. Мне 13 лет.</code></pre>
    <p><span class="font-semibold italic">f-строки</span> также поддерживают расширенное форматирование чисел:</p>
    <pre><code>
<span class="line-number">1</span>a = <span class="number">1.56789</span>
<span class="line-number">2</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>a<span class="function">}</span><span class="string">"</span>)
<span class="line-number">3</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>a<span class="function">:</span><span class="string">.2f</span><span
        class="function">}</span><span class="string">"</span>)</code></pre>
    <p>Результат:</p>
    <pre><code>
<span class="line-number">>>></span>1.56789
<span class="line-number">>>></span>1.57</code></pre>
    <p>Запись <code>a:.<span class="font-semibold">2</span>f</code> означает, что нужно вывести округленное значение
      переменной <code>a</code> с <span class="font-semibold italic">двумя знаками после запятой</span>.</p>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Требуется вывести надпись: <code>The bird's tail</code>.</p>
    <pre><code>
<span class="line-number">1</span><span class="function">print</span>(<span
        class="string">f"The bird's tail"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>The bird's tail</code></pre>
    <a href="https://official.contest.yandex.ru/contest/45316/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <svg
          aria-hidden="true"
          class="w-6 h-6 ml-3"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg">
        <path
            fill-rule="evenodd"
            d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0
              110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd">
        </path>
      </svg>
    </a>
  </main>
</template>

<script>
export default {
  name: "VariableAssignmentStatement"
}
</script>

<style scoped>

</style>