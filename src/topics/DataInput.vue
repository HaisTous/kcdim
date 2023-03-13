<template>
  <main>
    <h2 class="title">Ввод данных</h2>
    <p><span class="font-semibold italic">Python</span> предоставляет встроенную функцию
      <code class="function">input()</code>, которая останавливает программу и ждет ввода данных от пользователя.
      Когда пользователь нажимает клавишу <span class="font-semibold italic">Return/Enter</span>, программа
      возобновляет работу и функция <code class="function">input()</code> возвращает ввод пользователя в виде
      <span class="underline">строки</span>.
    </p>
    <pre><code>
<span class="line-number">1</span>a = <span class="function">input</span>()</code></pre>
    <p>Если пользователь должен ввести целое число, то вы можете попробовать преобразовать возвращаемое значение в тип
      <code class="function">int</code>:</p>
    <pre><code>
<span class="line-number">1</span>a = <span class="function">int</span>(<span
        class="function">input</span>())</code></pre>
    <p>Для ввода вещественных чисел используется функция <code class="function">float()</code>:</p>
    <pre><code>
<span class="line-number">1</span>a = <span class="function">float</span>(<span class="function">input</span>())</code></pre>
    <p>Если пользователь должен ввести несколько значений через пробел, то можно использовать следующие конструкции:</p>
    <pre><code>
<span class="line-number">1</span>a, b = <span class="function">map</span>(<span class="function">int</span>, <span
        class="function">input</span>().<span class="method">split</span>()) <span class="comment"> # 1 2</span>
<span class="line-number">2</span>c, d, e = <span class="function">map</span>(<span class="function">float</span>, <span
        class="function">input</span>().<span class="method">split</span>())<span
        class="comment"> # 1.0 2.43 -1.234</span>
<span class="line-number">3</span>f, g, h, k, l = <span class="function">input</span>().<span
        class="method">split</span>()</code><span class="comment"> # Компьютерный центр детей и молодёжи</span></pre>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Требуется вывести равенство в следующем формате: <code>a+b = b+a</code>. <code>a</code> и <code>b</code> - целые
      числа, записанные в столбик.</p>
    <pre><code>
<span class="line-number">1</span>a = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">2</span>b = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">3</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>a<span class="function">}</span><span class="string">+</span><span
        class="function">{</span>b<span class="function">}</span> <span class="string">=</span> <span
        class="function">{</span>b<span class="function">}</span><span class="string">+</span><span
        class="function">{</span>a<span class="function">}</span><span class="string">"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>3
<span class="line-number">>>></span>5
<span class="line-number">>>></span>3+5 = 5+3</code></pre>
    <a href="https://official.contest.yandex.ru/contest/45344/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
  </main>
</template>

<script>
import IconRightArrow from "@/components/icons/IconRightArrow.vue";

export default {
  name: "DataInput",
  components: {IconRightArrow}
}
</script>

<style scoped>

</style>