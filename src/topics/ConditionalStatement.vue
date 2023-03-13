<template>
  <main>
    <h2 class="title section" data-section="conditional-operator" id="conditional-operator">Условный оператор</h2>
    <p><span class="font-semibold italic">Логическим</span> (булевым) называется выражение, которое может быть
      <span class="underline">истинным</span> или <span class="underline">ложным</span>. В следующих примерах
      используется оператор <code>==</code>, который сравнивает два операнда и возвращает <code>True</code>, если
      они равны, и <code>False</code> — если нет:
    </p>
    <pre><code>
<span class="line-number">>>></span>5 == 5
<span class="line-number">>>></span>True
<span class="line-number">>>></span>5 == 6
<span class="line-number">>>></span>False</code></pre>
    <p><code>True</code> и <code>False</code> — это специальные значения, принадлежащие типу <code>bool</code>.</p>
    <h2 class="title section my-4" data-section="comparison-operators" id="comparison-operators">Операторы
      сравнения</h2>
    <div class="stripped-table my-4">
      <table>
        <thead>
        <tr>
          <th scope="col">Оператор в математике</th>
          <th scope="col">Оператор в Python</th>
          <th scope="col">Пояснение</th>
          <th scope="col">Пример</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td>></td>
          <td>></td>
          <td>Больше</td>
          <td class="whitespace-nowrap">
            <code>5 > 3 - True</code>
            <br>
            <code>5 > 5 - False</code>
          </td>
        </tr>
        <tr>
          <td>&lt;</td>
          <td>&lt;</td>
          <td>Меньше</td>
          <td class="whitespace-nowrap">
            <code>-1 &lt; 1 - True</code>
            <br>
            <code>8 &lt; 6 - False</code>
          </td>
        </tr>
        <tr>
          <td>=</td>
          <td>==</td>
          <td>Равно</td>
          <td class="whitespace-nowrap">
            <code>2 == 2 - True</code>
            <br>
            <code>-3 == 3 - False</code>
          </td>
        </tr>
        <tr>
          <td>≠</td>
          <td>!=</td>
          <td>Не равно</td>
          <td class="whitespace-nowrap">
            <code>4 != 7 - True</code>
            <br>
            <code>1 != 1 - False</code>
          </td>
        </tr>
        <tr>
          <td>≥</td>
          <td>>=</td>
          <td>Больше или равно</td>
          <td class="whitespace-nowrap">
            <code>9 >= 9 - True</code>
            <br>
            <code>0 >= 1 - False</code>
          </td>
        </tr>
        <tr>
          <td>≤</td>
          <td>&lt;=</td>
          <td>Меньше или равно</td>
          <td class="whitespace-nowrap">
            <code>-8 &lt;= -7 - True</code>
            <br>
            <code>5 &lt;= -5 - False</code>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <h2 class="title section my-4" data-section="сonditional-execution" id="сonditional-execution">Условное
      выполнение</h2>
    <p>Для написания полезных программ почти всегда нужна возможность проверять условия и соответственно изменять
      поведение программы. Условные инструкции дают нам эту возможность. Самая простая форма — это инструкция
      <code class="statement">if</code>:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> x > <span class="number">0</span>:
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"x - положительное число"</span>)</code></pre>
    <p>Количество инструкций, которые могут быть указаны в теле, не ограничено, но должна быть хотя бы одна.</p>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Требуется увеличить число <code>x</code> на 2, если оно неположительное.</p>
    <pre><code>
<span class="line-number">1</span>x = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">2</span><span class="statement">if</span> x &lt;= <span class="number">0</span>:
<span class="line-number">3</span><span class="tab1">x += </span><span class="number">2</span>
<span class="line-number">4</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>x<span class="function">}</span><span class="string">"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>0
<span class="line-number">>>></span>2
<span class="line-number">>>></span>
<span class="line-number">>>></span>5
<span class="line-number">>>></span>5</code></pre>
    <a href="https://official.contest.yandex.ru/contest/46059/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
    <h2 class="title section my-4" data-section="alternative-execution" id="alternative-execution">Альтернативное
      выполнение</h2>
    <p>Вторая форма инструкции <code class="statement">if</code> — <span class="font-semibold">
      "альтернативное выполнение"</span>, в котором есть две возможности, и условие определяет, какая из них
      выполняется.
      Синтаксис выглядит так:
    </p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> x % <span class="number">2</span> == <span
        class="number">0</span>:
<span class="line-number">2</span><span class="function tab1">print</span>(<span
        class="string">f"x - чётное число"</span>)
<span class="line-number">3</span><span class="statement">else</span>:
<span class="line-number">4</span><span class="function tab1">print</span>(<span
        class="string">f"x - нечётное число"</span>)</code></pre>
    <p>Если остаток от деления <code>x</code> на <code>2</code> равен <code>0</code>, то мы знаем, что <code>x</code> —
      четное число, и программа отображает соответствующее сообщение. Если условие ложно, выполняется второй набор
      инструкций. Поскольку условие может быть либо истинным, либо ложным, будет выполнена ровно одна из альтернатив.
      Альтернативы называются <span class="font-semibold">ветвями</span>, потому что это и есть ветви в потоке
      выполнения.</p>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Выведите YES в том случае, если <code>a + b = c</code> и выведите NO в противном случае.</p>
    <pre><code>
<span class="line-number">1</span>a, b, c = <span class="function">map</span>(<span class="function">int</span>, <span
        class="function">input</span>().<span class="method">split</span>())
<span class="line-number">2</span><span class="statement">if</span> a + b == c:
<span class="line-number">3</span><span class="function tab1">print</span>(<span class="string">f"YES"</span>)
<span class="line-number">4</span><span class="statement">else</span>:
<span class="line-number">5</span><span class="function tab1">print</span>(<span
        class="string">f"NO"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>1 2 3
<span class="line-number">>>></span>YES
<span class="line-number">>>></span>
<span class="line-number">>>></span>2 5 8
<span class="line-number">>>></span>NO</code></pre>
    <a href="https://official.contest.yandex.ru/contest/46125/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
    <h2 class="title section my-4" data-section="сhained-conditionals" id="сhained-conditionals">Связанные условия</h2>
    <p>Иногда существует более двух возможностей и требуется более двух ветвей. Один из способов выразить подобное
      вычисление — использовать <span class="font-semibold">связанные условия</span>:
    </p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> x &lt; y:
<span class="line-number">2</span><span class="function tab1">print</span>(<span
        class="string">f"x меньше, чем y"</span>)
<span class="line-number">3</span><span class="statement">elif</span> x > y:
<span class="line-number">4</span><span class="function tab1">print</span>(<span
        class="string">f"x больше, чем y"</span>)
<span class="line-number">5</span><span class="statement">else</span>:
<span class="line-number">6</span><span class="function tab1">print</span>(<span
        class="string">f"x и y равны"</span>)</code></pre>
    <p><code class="statement">elif</code> — это аббревиатура для "<code class="statement">else if</code>". Выполняться
      будет только одна ветвь. Ограничений на количество инструкций <code class="statement">elif</code> нет.
      Инструкция <code class="statement">else</code> должна быть указана в конце.</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> month == <span class="number">1</span>:
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"January"</span>)
<span class="line-number">3</span><span class="statement">elif</span> month == <span class="number">2</span>:
<span class="line-number">4</span><span class="function tab1">print</span>(<span class="string">f"February"</span>)
<span class="line-number">5</span><span class="statement">elif</span> month == <span class="number">3</span>:
<span class="line-number">6</span><span class="function tab1">print</span>(<span class="string">f"March"</span>)</code></pre>
    <p>Каждое условие проверяется по порядку. Если первое ложно, проверяется следующее, и так далее. Если одно из них
      истинно, выполняется соответствующая ветвь, и инструкция заканчивает свою работу. Даже если истинно более чем
      одно условие, выполняется только <span class="font-semibold">первая</span> истинная ветвь.</p>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Известны результаты каждого из двух таймов футбольного матча. Выведите номер выигравшей команды, в случае ничьей
      следует вывести «DRAW».</p>
    <pre><code>
<span class="line-number">1</span>a1, b1 = <span class="function">map</span>(<span class="function">int</span>, <span
        class="function">input</span>().<span class="method">split</span>())
<span class="line-number">2</span>a2, b2 = <span class="function">map</span>(<span class="function">int</span>, <span
        class="function">input</span>().<span class="method">split</span>())
<span class="line-number">3</span>a = a1 + a2
<span class="line-number">4</span>b = b1 + b2
<span class="line-number">5</span><span class="statement">if</span> a > b:
<span class="line-number">6</span><span class="function tab1">print</span>(<span class="string">f"1"</span>)
<span class="line-number">7</span><span class="statement">elif</span> a &lt; b:
<span class="line-number">8</span><span class="function tab1">print</span>(<span class="string">f"2"</span>)
<span class="line-number">9</span><span class="statement">else</span>:
<span class="line-number">10</span><span class="function tab1">print</span>(<span class="string">f"DRAW"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>1 1
<span class="line-number">>>></span>2 1
<span class="line-number">>>></span>1
<span class="line-number">>>></span>
<span class="line-number">>>></span>1 3
<span class="line-number">>>></span>1 0
<span class="line-number">>>></span>2
<span class="line-number">>>></span>
<span class="line-number">>>></span>0 0
<span class="line-number">>>></span>1 1
<span class="line-number">>>></span>DRAW</code></pre>
    <a href="https://official.contest.yandex.ru/contest/46126/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
    <h2 class="title section my-4" data-section="nested-conditionals" id="nested-conditionals">Вложенные условия</h2>
    <p>Одно условие также может быть вложено в другое. Мы могли бы переписать пример из предыдущего раздела
      следующим образом:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> x == y:
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"x и y равны"</span>)
<span class="line-number">3</span><span class="statement">else</span>:
<span class="line-number">4</span><span class="statement tab1">if</span> x &lt; y:
<span class="line-number">5</span><span class="function tab2">print</span>(<span
        class="string">f"x меньше, чем y"</span>)
<span class="line-number">6</span><span class="statement tab1">else</span>:
<span class="line-number">7</span><span class="function tab2">print</span>(<span
        class="string">f"x больше, чем y"</span>)</code></pre>
    <p>Внешняя условная инструкция содержит две ветви. Первая ветвь содержит обычную инструкцию. Вторая ветвь содержит
      еще одну инструкцию <code class="statement">if</code>, у которой две собственные ветви. Эти две ветви — простые
      инструкции. Разумеется, они могли бы быть так же и условными операторами.</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> <span class="number">0</span> &lt; x:
<span class="line-number">2</span><span class="statement tab1">if</span> x &lt; <span class="number">10</span>:
<span class="line-number">3</span><span class="function tab2">print</span>(<span class="string">f"x - положительное однозначное число"</span>)</code></pre>
    <p>Несмотря на то что отступы инструкций позволяют разглядеть структуру, <span class="font-semibold">
      вложенные условные инструкции</span> очень трудно прочитать с ходу. Поэтому рекомендуется их избегать.</p>
    <h2 class="title section my-4" data-section="logical-operators" id="logical-operators">Логические операторы</h2>
    <p>Существует три <span class="font-semibold">логических оператора</span>: <code>not</code>, <code>and</code> и
      <code>or</code>. Значение этих операторов аналогично значению этих слов в английском языке.</p>
    <p class="mt-4">Например, <code>x > 0 and x &lt; 10</code> истинно, только если <code>x</code> больше <code>0</code>
      и меньше <code>10</code>.</p>
    <p class="mt-4"><code>n % 2 == 0 or n % 3 == 0</code> истинно, если выполняется одно или оба условия, то есть
      если число делится на <code>2</code> или на <code>3</code> без остатка.</p>
    <p class="mt-4">Наконец, оператор <code>not</code> отрицает логическое выражение, поэтому <code>not (x > y)</code>
      истинно, если <code>x > y</code> ложно, то есть если <code>x</code> меньше или равно <code>y</code>.</p>
    <div class="stripped-table my-4">
      <table>
        <thead>
        <tr>
          <th scope="col">Оператор</th>
          <th scope="col">Назначение</th>
          <th scope="col">Выражение</th>
          <th scope="col">Результат</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td><code>not</code></td>
          <td>Логическое <span class="font-semibold italic">НЕ</span></td>
          <td>
            <code>not True</code>
            <br>
            <code>not False</code>
          </td>
          <td>
            <code>False</code>
            <br>
            <code>True</code>
          </td>
        </tr>
        <tr>
          <td><code>and</code></td>
          <td>Логическое <span class="font-semibold italic">И</span></td>
          <td>
            <code>False and False</code>
            <br>
            <code>False and True</code>
            <br>
            <code>True and False</code>
            <br>
            <code>True and True</code>
          </td>
          <td>
            <code>False</code>
            <br>
            <code>False</code>
            <br>
            <code>False</code>
            <br>
            <code>True</code>
          </td>
        </tr>
        <tr>
          <td><code>or</code></td>
          <td>Логическое <span class="font-semibold italic">ИЛИ</span></td>
          <td>
            <code>False or False</code>
            <br>
            <code>False or True</code>
            <br>
            <code>True or False</code>
            <br>
            <code>True or True</code>
          </td>
          <td>
            <code>False</code>
            <br>
            <code>True</code>
            <br>
            <code>True</code>
            <br>
            <code>True</code>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <p>Логические операторы часто предоставляют способ упростить набор вложенных условных инструкций. Например, мы
      можем переписать предыдущий код, используя всего одно условие и логический оператор <code>and</code>:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> x &lt; <span class="number">0</span> <span
        class="statement">and</span> x &lt; <span class="number">10</span>:
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"x - положительное однозначное число"</span>)</code></pre>
    <p>Для такого рода условий <code>Python</code> предоставляет более краткий вариант записи:</p>
    <pre><code>
<span class="line-number">1</span><span class="statement">if</span> <span class="number">0</span> &lt; x &lt; <span
        class="number">10</span>:
<span class="line-number">2</span><span class="function tab1">print</span>(<span class="string">f"x - положительное однозначное число"</span>)</code></pre>
    <p class="font-semibold underline mt-4">Пример</p>
    <p>Даны три целых числа <code>a, b, c</code>. Выведите YES, если среди них есть хотя бы одно четное и хотя бы
      одно нечетное. В противном случае выведите NO.</p>
    <pre><code>
<span class="line-number">1</span>a, b, c = <span class="function">map</span>(<span class="function">int</span>, <span
        class="function">input</span>().<span class="method">split</span>())
<span class="line-number">2</span>a1 = a % <span class="number">2</span>
<span class="line-number">3</span>b1 = b % <span class="number">2</span>
<span class="line-number">4</span>c1 = c % <span class="number">2</span>
<span class="line-number">5</span><span class="statement">if</span> a1 + b1 == <span class="number">1</span> <span
        class="statement">or</span> b1 + c1 == <span class="number">1</span> <span class="statement">or</span> c1 + a1 == <span
        class="number">1</span>:
<span class="line-number">6</span><span class="function tab1">print</span>(<span class="string">f"YES"</span>)
<span class="line-number">7</span><span class="statement">else</span>:
<span class="line-number">8</span><span class="function tab1">print</span>(<span
        class="string">f"NO"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>1 2 3
<span class="line-number">>>></span>YES
<span class="line-number">>>></span>
<span class="line-number">>>></span>2 4 6
<span class="line-number">>>></span>NO</code></pre>
    <a href="https://official.contest.yandex.ru/contest/46127/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
  </main>
  <side-bar :sections="sections"/>
</template>

<script>
import SideBar from "@/components/SideBar.vue";
import IconRightArrow from "@/components/icons/IconRightArrow.vue";

export default {
  name: "ConditionalStatement",
  components: {IconRightArrow, SideBar},
  data() {
    return {
      sections: [
        {id: 1, name: 'Условный оператор', link: 'conditional-operator'},
        {id: 2, name: 'Операторы сравнения', link: 'comparison-operators'},
        {id: 3, name: 'Условное выполнение', link: 'сonditional-execution'},
        {id: 4, name: 'Альтернативное выполнение', link: 'alternative-execution'},
        {id: 5, name: 'Связанные условия', link: 'сhained-conditionals'},
        {id: 6, name: 'Вложенные условия', link: 'nested-conditionals'},
        {id: 7, name: 'Логические операторы', link: 'logical-operators'},
      ]
    }
  }
}
</script>

<style scoped>

</style>