<template>
  <main>
    <h2 class="title section" data-section="loops" id="loops">Операторы цикла</h2>
    <p>При написании программ зачастую встаёт задача сделать однотипное действие много раз. Например, перебрать все
      числа от 1 до 10 и для каждого выполнить одинаковый код. Для многократного повторения одного участка кода
      предусмотрены циклы.</p>
    <h2 class="title section my-4" data-section="for-loop" id="for-loop">Цикл for</h2>
    <p>Более сложный, но при этом самый распространённый цикл — цикл <code class="statement">for</code>.</p>
    <p class="mt-4">Выглядит он так:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">for</span> ‹переменная-счётчик› <span
        class="statement">in</span> <span class="function">range</span>(‹начало›, ‹конец›, ‹шаг›):
<span class="line-number">2</span><span class="comment tab1"># тело цикла</span></code></pre>
    <p>Давайте разберёмся, что означает каждая часть, на примере. Цикл ниже выполняет
      <code><span class="function">print</span>(<span class="string">f"</span><span class="function">{</span>i<span
          class="function">}</span><span class="string">"</span>)</code> для <code>i</code> от <code>0</code> до (но
      не включая)
      <code>3</code>:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">0</span>, <span class="number">3</span>, <span
        class="number">1</span>):
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>0
<span class="line-number">>>></span>1
<span class="line-number">>>></span>2</code></pre>
    <p>Одно выполнение тела цикла по-научному называется <span class="font-semibold">итерация</span>. Цикл в примере
      выше совершает три итерации.</p>
    <p class="mt-4">Рассмотрим конструкцию <span class="statement">for</span> подробней. Код выше будет представлять
      собой такую
      инструкцию:</p>
    <ol class="my-4">
      <li>Начать отсчет с <code>0</code> и остановиться, не доходя до числа <code>3</code>.</li>
      <li>Каждое отсчитанное значение сохранять в переменной <code>i</code>.</li>
      <li>Выводить на экран значение переменной <code>i</code>.</li>
    </ol>
    <p>Если записать этот код без цикла <code class="statement">for</code>, он будет выглядеть примерно так:</p>
    <pre><code>
<span class="line-number">1</span>i = <span class="number">0</span>
<span class="line-number">2</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)
<span class="line-number">3</span>i += <span class="number">1</span>
<span class="line-number">4</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)
<span class="line-number">5</span>i += <span class="number">1</span>
<span class="line-number">6</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)</code></pre>
    <p>Выходит, цикл избавил от необходимости писать четыре дополнительных строк кода. Хорошие программисты терпеть не
      могут делать одно и то же несколько раз, поэтому цикл — одна из самых популярных программных конструкций.</p>
    <h2 class="title my-4">Примеры функции range()</h2>
    <pre><code>
<span class="line-number">>>></span><span class="comment"># 5 чисел, начиная с 0</span>
<span class="line-number">>>></span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">5</span>):
<span class="line-number">>>></span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span class="string">"</span>, <span
        class="number">end</span>=<span class="string">" "</span>)
<span class="line-number">>>></span>0 1 2 3 4
<span class="line-number">>>></span>
<span class="line-number">>>></span><span class="comment"># числа от 3 до 6 (не включительно)</span>
<span class="line-number">>>></span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">3</span>, <span class="number">6</span>):
<span class="line-number">>>></span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span class="string">"</span>, <span
        class="number">end</span>=<span class="string">" "</span>)
<span class="line-number">>>></span>3 4 5
<span class="line-number">>>></span>
<span class="line-number">>>></span><span class="comment"># числа от 1 до 10 (не включительно) с шагом 2</span>
<span class="line-number">>>></span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">1</span>, <span class="number">10</span>, <span
        class="number">2</span>):
<span class="line-number">>>></span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span class="string">"</span>, <span
        class="number">end</span>=<span class="string">" "</span>)
<span class="line-number">>>></span>1 3 5 7 9
<span class="line-number">>>></span>
<span class="line-number">>>></span><span class="comment"># числа от 0 до -10 (не включительно) с шагом -1</span>
<span class="line-number">>>></span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">0</span>, <span class="number">-10</span>, <span
        class="number">-1</span>):
<span class="line-number">>>></span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span class="string">"</span>, <span
        class="number">end</span>=<span class="string">" "</span>)
<span class="line-number">>>></span>0 -1 -2 -3 -4 -5 -6 -7 -8 -9</code></pre>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Даны два целых числа <code>a, b (a ≤ b)</code>. Выведите сумму всех целых чисел от <code>a</code> до
      <code>b</code>.</p>
    <pre><code>
<span class="line-number">1</span>a, b = <span class="function">map</span>(<span class="function">int</span>, <span
        class="function">input</span>().<span class="method">split</span>())
<span class="line-number">2</span>s = <span class="number">0</span>
<span class="line-number">3</span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(a, b + <span class="number">1</span>):
<span class="line-number">4</span><span class="tab1">s += i</span>
<span class="line-number">5</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>s<span
        class="function">}</span><span class="string">"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>1 10
<span class="line-number">>>></span>55</code></pre>
    <a href="https://official.contest.yandex.ru/contest/46846/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
    <h2 class="title section my-4" data-section="while-loop" id="while-loop">Цикл while</h2>
    <p>Цикл <code class="statement">for</code> — не единственный вид циклов в языке <code>Python</code>. Есть также цикл
      <code class="statement">while</code>, который используется, если нужное количество повторов заранее неизвестно,
      тогда как <code class="statement">for</code> расчитан на определенное число повторов.</p>
    <p class="mt-4">Цикл <code class="statement">while</code> имеет следующий синтаксис:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">while</span> condition:
<span class="line-number">2</span><span class="comment tab1"># тело цикла</span></code></pre>
    <p>Код из тела цикла выполняется, пока условие <code>condition</code> истинно.</p>
    <p class="mt-4">Например, цикл ниже выводит <code>i</code>, пока <code>i &lt; 3</code>:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">while</span> i &lt; <span class="number">3</span>:
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)
<span class="line-number">3</span><span class="tab1">i +=</span> <span class="number">1</span></code></pre>
    <pre><code>
<span class="line-number">>>></span>0
<span class="line-number">>>></span>1
<span class="line-number">>>></span>2</code></pre>
    <p>Если бы строка <code>i += <span class="number">1</span></code> отсутствовала в примере выше, то цикл бы
      повторялся вечно, формируя так называемый <span class="font-semibold">бесконечный цикл</span>.</p>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Дано целое <code>x</code>. Выведите все положительные четные числа до тех пор, пока они не больше заданного
      числа <code>x</code>.</p>
    <pre><code>
<span class="line-number">1</span>x = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">2</span>i = <span class="number">2</span>
<span class="line-number">3</span><span class="statement">while</span> i &lt;= x:
<span class="line-number">4</span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)
<span class="line-number">5</span><span class="tab1">i += </span><span class="number">2</span></code></pre>
    <pre><code>
<span class="line-number">>>></span>6
<span class="line-number">>>></span>2
<span class="line-number">>>></span>4
<span class="line-number">>>></span>6</code></pre>
    <a href="https://official.contest.yandex.ru/contest/46990/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
    <h2 class="title section mt-4" data-section="break-statement" id="break-statement">Оператор break</h2>
    <p>Оператор <code class="statement">break</code> служит для досрочного выхода из цикла. Например, для цикла
      <code class="statement">for</code>:</p>
    <pre><code>
<span class="line-number">1</span>age = <span class="number">10</span>
<span class="line-number">2</span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">1</span>, <span class="number">100</span>):
<span class="line-number">3</span><span class="function tab1">print</span>(<span class="string">f"отсчёт </span><span
        class="function">{</span>i<span
        class="function">}</span><span class="string">"</span>)
<span class="line-number">4</span><span class="statement tab1">if</span> i == age:
<span class="line-number">5</span><span class="function tab2">print</span>(<span
        class="string">f"закончили считать"</span>)
<span class="line-number">6</span><span class="statement tab2">break</span></code></pre>
    <pre><code>
<span class="line-number">>>></span>отсчёт 1
<span class="line-number">>>></span>отсчёт 2
<span class="line-number">>>></span>отсчёт 3
<span class="line-number">>>></span>отсчёт 4
<span class="line-number">>>></span>отсчёт 5
<span class="line-number">>>></span>отсчёт 6
<span class="line-number">>>></span>отсчёт 7
<span class="line-number">>>></span>отсчёт 8
<span class="line-number">>>></span>отсчёт 9
<span class="line-number">>>></span>отсчёт 10
<span class="line-number">>>></span>закончили считать</code></pre>
    <p>Слово <code class="statement">else</code>, примененное в цикле <code class="statement">for</code> или
      <code class="statement">while</code>, проверяет, был ли произведен выход из цикла оператором
      <code class="statement">break</code>, или же "естественным" образом. Блок инструкций внутри
      <code class="statement">else</code> выполнится только в том случае, если выход из цикла произошел без помощи
      <code class="statement">break</code>.</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">10</span>, <span class="number">100</span>):
<span class="line-number">2</span><span class="statement tab1">if</span> <span class="number">-9</span> &lt;= i &lt;= <span
        class="number">9</span>:
<span class="line-number">3</span><span class="function tab2">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span class="string"> - однозначное число"</span>)
<span class="line-number">4</span><span class="statement tab2">break</span>
<span class="line-number">4</span><span class="statement">else</span>:
<span class="line-number">3</span><span class="function tab1">print</span>(<span class="string">f"однозначных чисел в цикле нет"</span>)</code></pre>
    <h2 class="title section mt-4" data-section="continue-statement" id="continue-statement">Оператор continue</h2>
    <p>Оператор <code class="statement">continue</code> позволяет «перескочить» к следующему повтору цикла, так что
      следующая после <code class="statement">continue</code> часть тела цикла будет пропущена. В отличие от
      <code class="statement">break</code> происходит не выход из цикла, а досрочное завершение текущего повтора
      с переходом к следующему.</p>
    <p class="mt-4">Оператор используют, если понятно, что на текущем повторе цикла делать больше нечего.</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">for</span> i <span class="statement">in</span> <span
        class="function">range</span>(<span class="number">1</span>, <span class="number">16</span>):
<span class="line-number">2</span><span class="statement tab1">if</span> i % <span class="number">2</span> == <span
        class="number">0</span>:
<span class="line-number">3</span><span class="function tab2">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span class="string"> - чётное число"</span>)
<span class="line-number">4</span><span class="statement tab2">continue</span>
<span class="line-number">5</span><span class="function tab1">print</span>(<span class="string">f"</span><span
        class="function">{</span>i<span class="function">}</span><span
        class="string"> - нечётное число"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>1 - нечётное число
<span class="line-number">>>></span>2 - чётное число
<span class="line-number">>>></span>3 - нечётное число
<span class="line-number">>>></span>4 - чётное число
<span class="line-number">>>></span>5 - нечётное число
<span class="line-number">>>></span>6 - чётное число
<span class="line-number">>>></span>7 - нечётное число
<span class="line-number">>>></span>8 - чётное число
<span class="line-number">>>></span>9 - нечётное число
<span class="line-number">>>></span>10 - чётное число
<span class="line-number">>>></span>11 - нечётное число
<span class="line-number">>>></span>12 - чётное число
<span class="line-number">>>></span>13 - нечётное число
<span class="line-number">>>></span>14 - чётное число
<span class="line-number">>>></span>15 - нечётное число</code></pre>
    <p>Для чётных значений <code>i</code>, оператор <code class="statement">continue</code> прекращает выполнение тела
      цикла и передаёт управление на следующую итерацию <code class="statement">for</code> (со следующим числом).
      Таким образом, нечётные значения <code>i</code> выводятся без условия.</p>
    <p class="mt-4">Оператор <code class="statement">continue</code> можно использовать вместо вложенного условного
      кода или для оптимизации цикла.</p>
  </main>
  <side-bar :sections="sections"/>
</template>

<script>
import SideBar from "@/components/SideBar.vue";
import IconRightArrow from "@/components/icons/IconRightArrow.vue";

export default {
  name: "LoopStatement",
  components: {IconRightArrow, SideBar},
    data() {
    return {
      sections: [
        {id: 1, name: 'Операторы цикла', link: 'loops'},
        {id: 2, name: 'Цикл for', link: 'for-loop'},
        {id: 3, name: 'Цикл while', link: 'while-loop'},
        {id: 4, name: 'Оператор break', link: 'break-statement'},
        {id: 5, name: 'Оператор continue', link: 'continue-statement'},
      ]
    }
  }
}
</script>

<style scoped>

</style>