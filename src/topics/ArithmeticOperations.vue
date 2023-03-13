<template>
  <main>
    <h2 class="title section" data-section="operations" id="operations">Арифметические операции</h2>
    <p>В языке <span class="font-semibold italic">Python</span> есть операторы, которые выглядят как специальные
      символы, предоставляющие вычисления, такие как сложение, умножение и др.
    </p>
    <div class="stripped-table my-4">
      <table>
        <thead>
        <tr>
          <th scope="col">Оператор в математике</th>
          <th scope="col">Оператор в Python</th>
          <th scope="col">Описание</th>
          <th scope="col">Приоритет</th>
          <th scope="col">Пример</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td>+</td>
          <td>+</td>
          <td>Сложение</td>
          <td>3</td>
          <td class="whitespace-nowrap">9 + 2 = 11</td>
        </tr>
        <tr>
          <td>-</td>
          <td>-</td>
          <td>Вычитание</td>
          <td>3</td>
          <td class="whitespace-nowrap">9 - 2 = 7</td>
        </tr>
        <tr>
          <td>∙</td>
          <td>*</td>
          <td>Умножение</td>
          <td>2</td>
          <td class="whitespace-nowrap">9 * 2 = 18</td>
        </tr>
        <tr>
          <td>:</td>
          <td>/</td>
          <td>Деление</td>
          <td>2</td>
          <td class="whitespace-nowrap">9 / 2 = 4.5</td>
        </tr>
        <tr>
          <td><img class="w-32 mx-auto h-auto rounded-lg" src="/src/assets/topics/div.webp" alt="Целочисленное деление"></td>
          <td>//</td>
          <td>Целочисленное деление (деление, при котором возвращается целая часть)</td>
          <td>2</td>
          <td class="whitespace-nowrap">465 // 5 = 93</td>
        </tr>
        <tr>
          <td><img class="w-32 mx-auto h-auto rounded-lg" src="/src/assets/topics/mod.webp" alt="Деление по модулю"></td>
          <td>%</td>
          <td>Делению по модулю (нахождение остатка)</td>
          <td>2</td>
          <td class="whitespace-nowrap">465 % 5 = 0</td>
        </tr>
        <tr>
          <td><img class="w-32 mx-auto h-auto rounded-lg" src="/src/assets/topics/power.webp" alt="Возведение в степень"></td>
          <td>**</td>
          <td>Возведение в степень</td>
          <td>1</td>
          <td class="whitespace-nowrap">5 ** 3 = 125</td>
        </tr>
        </tbody>
      </table>
    </div>
    <p>При последовательном использовании нескольких арифметических операций их выполнение производится в соответствии
      с приоритетом. В начале выполняются операции с большим приоритетом. Если необходимо изменить приоритет
      операции, то используются скобки:</p>
    <pre><code>
<span class="line-number">>>></span>3 * 2 ** 3
<span class="line-number">>>></span>24
<span class="line-number">>>></span>(3 * 2) ** 3
<span class="line-number">>>></span>729</code></pre>
    <p class="font-semibold underline">Пример</p>
    <p>Требуется сложить два целых числа <code>a</code> и <code>b</code>, записанных в столбик.</p>
    <pre><code>
<span class="line-number">1</span>a = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">2</span>b = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">3</span>c = a + b
<span class="line-number">4</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>c<span class="function">}</span><span class="string">"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>3
<span class="line-number">>>></span>5
<span class="line-number">>>></span>8</code></pre>
    <a href="https://official.contest.yandex.ru/contest/45720/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
    <h2 class="title section" data-section="compound-operations" id="compound-operations">
      Составные арифметические операции с присваиванием
    </h2>
    <p>В языке <span class="font-semibold italic">Python</span> имеются специальные операции, которые являются
      объединением арифметической операции с операцией присваивания.
    </p>
    <p class="mt-4">Операторы вроде показанного ниже в программах встречаются достаточно часто:</p>
    <pre><code>
<span class="line-number">>>></span>а = а + 4</code></pre>
    <p>В языке <span class="font-semibold italic">Python</span> этот оператор можно записать следующим образом:</p>
    <pre><code>
<span class="line-number">>>></span>а += 4</code></pre>
    <p>В этой версии оператора использована составная операция присваивания <code>+=</code>. Оба оператора выполняют
      одно и то же действие: они увеличивают значение переменной <code>a</code> на 4.</p>
    <div class="stripped-table my-4">
      <table>
        <thead>
        <tr>
          <th scope="col">Оператор</th>
          <th scope="col">Полная запись</th>
          <th scope="col">Короткая запись</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td><code>+=</code></td>
          <td><code>a = a + 4</code></td>
          <td><code>a += 4</code></td>
        </tr>
        <tr>
          <td><code>-=</code></td>
          <td><code>a = a - 3</code></td>
          <td><code>a -= 3</code></td>
        </tr>
        <tr>
          <td><code>*=</code></td>
          <td><code>a = a * 2</code></td>
          <td><code>a *= 2</code></td>
        </tr>
        <tr>
          <td><code>/=</code></td>
          <td><code>a = a / 6</code></td>
          <td><code>a /= 6</code></td>
        </tr>
        <tr>
          <td><code>//=</code></td>
          <td><code>a = a // 8</code></td>
          <td><code>a //= 8</code></td>
        </tr>
        <tr>
          <td><code>%=</code></td>
          <td><code>a = a % 10</code></td>
          <td><code>a %= 10</code></td>
        </tr>
        <tr>
          <td><code>**=</code></td>
          <td><code>a = a ** 0.5</code></td>
          <td><code>a **= 0.5</code></td>
        </tr>
        </tbody>
      </table>
    </div>
    <h2 class="title section" data-section="numbers" id="numbers">Обработка цифр числа</h2>
    <p>Одной из часто используемых задач является нахождение цифр числа. Для того чтобы найти все цифры
      <span class="underline">целого положительного числа</span>, нужно использовать две арифметические
      операции.
    </p>
    <ol class="my-4">
      <li>
        <span class="font-semibold">Нахождение последней цифры числа.</span>
        <p>Для нахождения последней цифры числа нужно исходное число поделить на 10 и найти остаток от деления:</p>
        <pre><code>
<span class="line-number">>>></span>1 % 10
<span class="line-number">>>></span>1
<span class="line-number">>>></span>23 % 10
<span class="line-number">>>></span>3
<span class="line-number">>>></span>123456 % 10
<span class="line-number">>>></span>6</code></pre>
      </li>
      <li>
        <span class="font-semibold">Удаление цифр числа справа.</span>
        <p>Для удаления определенного количества цифр с конца числа нужно использовать целочисленное деление:</p>
        <pre><code>
<span class="line-number">>>></span>23 // 10
<span class="line-number">>>></span>2
<span class="line-number">>>></span>123456 // 100
<span class="line-number">>>></span>1234
<span class="line-number">>>></span>123456 // 10000
<span class="line-number">>>></span>12</code></pre>
        <p>Обратите внимание, что, например, если мы хотим удалить в числе <span class="underline">4</span> цифры
          справа, то нам нужно исходное число поделить на 1<span class="underline">0000</span> (простыми словами:
          <span class="underline">количество нулей совпадает с количеством цифр, которые мы хотим удалить</span>).</p>
      </li>
    </ol>
    <p>Комбинируя эти операции, можно находить любую цифру любого целого положительного числа:</p>
    <pre><code>
<span class="line-number">>>></span>1234 % 10
<span class="line-number">>>></span>4
<span class="line-number">>>></span>1234 // 10 % 10
<span class="line-number">>>></span>3
<span class="line-number">>>></span>1234 // 100 % 10
<span class="line-number">>>></span>2
<span class="line-number">>>></span>1234 // 1000
<span class="line-number">>>></span>1</code></pre>
    <p class="font-semibold underline">Пример</p>
    <p>Требуется найти сумму цифр положительного трёхзначного числа <code>x</code>.</p>
    <pre><code>
<span class="line-number">1</span>x = <span class="function">int</span>(<span class="function">input</span>())
<span class="line-number">2</span>a = x // <span class="number">100</span>
<span class="line-number">3</span>b = x // <span class="number">10</span> % <span class="number">10</span>
<span class="line-number">4</span>c = x % <span class="number">10</span>
<span class="line-number">5</span>d = a + b + c
<span class="line-number">6</span><span class="function">print</span>(<span class="string">f"</span><span
        class="function">{</span>d<span class="function">}</span><span class="string">"</span>)</code></pre>
    <pre><code>
<span class="line-number">>>></span>123
<span class="line-number">>>></span>6</code></pre>
    <a href="https://official.contest.yandex.ru/contest/45855/enter" class="block-link" target="_blank">
      <span class="w-full">Практические задания</span>
      <icon-right-arrow class="ml-4"/>
    </a>
  </main>
  <side-bar :sections="sections"/>
</template>

<script>
import IconRightArrow from "@/components/icons/IconRightArrow.vue";
import SideBar from "@/components/SideBar.vue";

export default {
  name: "ArithmeticOperations",
  components: {SideBar, IconRightArrow},
  data () {
    return {
      sections: [
        {id: 1, name: 'Арифметические операции', link: 'operations'},
        {id: 2, name: 'Составные арифметические операции с присваиванием', link: 'compound-operations'},
        {id: 3, name: 'Обработка цифр числа', link: 'numbers'},
      ]
    }
  }
}
</script>

<style scoped>

</style>