"""basics_python."""

# ### Использование Spyder IDE ###
# ### Использование Jupyter Notebook ###
# ### Мы будем работать в Visual Studio Code ###
# **"Hello World"**</p>
# **1. Числа**</p>
# <p>Арифметические операторы: +, -, *, /.</p>
# <p>Круглые скобки используются для группировки ().</p>
# <p>Целые числа имеют тип int.</p>
# <p>Числа с дробной частью имеют тип float.</p>
# <p>Оператор деления / всегда возвращает тип float</p>
# <p>Что бы выполнить целочисленное деление, отбросив дробную часть над использовать оператор //.</p>
# <p>Что бы вычислить остаток используем оператор %.</p>
# <p>Для вычисления степени можно использовать оператор **.</p>
# <p>Знак равенства используется для присвоения значения переменной. После присвоения результат не отображается.</p>
#

print("Hello World!")

2 + 2

50 - 5 * 6

(50 - 5 * 6) / 4

8 / 5  # результат деления всегда с плавающей точкой

17 / 3  # обычное деление с плавающей точкой

17 // 3  # целочисленное деление

17 % 3  # остаток от деления

5 * 3 + 2  # проверка: результат * делитель + остаток

5**2  # 5 в квадрате

2**7  # 2 в степени 7

width = 20
height = 5 * 9
# мы присвоили значение двум переменным, этот код ничего не возвращает

# **2. Строки**</p>
# <p>Помимо чисел Python может также работать со строками, которые можно задавать несколькими способами.</p>
# <p>Они могут быть заключены в одинарные '...' кавычки или двойные "..." кавычки.</p>
# <p>Для экранирования кавычек используйте символ обратной косой черты\.</p>
# <p>Функция print () позволяет получить более читаемый вывод, опустить кавычки и вывести экранированные и специальные символы.</p>
# <p>Управляющие символы: \t - табуляция внутри строки, \n - перенос следующего за ним текста на следующую строку, r - перед первой кавычкой  - прочтение управляющих символов как обычные знаки и буквы.</p>
#

print("does\n't")

print("now \tdoesn't")

print(r"doesn't\t")

# <p>Строки можно объединять с помощь оператора + КОНКАТЕНАЦИЯ.</p>
# <p>Строки можно повторять с помощью оператора * ПОВТОРЕНИЕ.</p>
# <p>Две и более строки заключенные в кавычки расположенные рядом друг с другом автоматически объединяются.</p>

"How", "are you", "?"

print("How are" + " you?")

print(" very good!" * 5)

# <p>Строки можно индексировать (обращаться к элементам строки по индексу), при этом первый символ имеет индекс 0. Отдельного типа для данных символов не существует, т.к. символ - это просто строка длиной в один символ.</p>
# <p>Индексы могут быть положительными и отрицательными. Для отрицательных индексов отсчет ведется справа.</p>
#

# |P|Y|T|H|O|N|
# |-|-|-|-|-|-|
# |0|1|2|3|4|5|
# |-6|-5|-4|-3|-2|-1|

# <p>Помимо индексирования строк также поддерживаются срезы. Если индексирование используется для извлечения отдельных символов, то срез возвращает подстроку. </p>
# <p>Начальный индекс всегда включается, а конечный всегда исключается.</p>
# <p>По умолчанию первый индекс равен нулю, опущенный второй индекс всегда равен длине строки.</p>
# <p>Строки Python нельзя изменить - они не изменяемы. Следовательно. Присвоить новое значение символу по определенному индексу нельзя! Если нужна новая строка, нужно ее создать.</p>
# <p>Встроенная функция len()  возвращает длину строки.</p>

word = "Python"
word[0:2]  # с позиции 0 (включительно) до 2 (не включая его)

len(word)

# ### Синтаксис кода Python ###
# **1. Выражения**</p>
# <p>Строки, написанные в исходном коде для выполнения, называются ВЫРАЖЕНИЯМИ которые могут состоять из ОПЕРАТОРОВ разных типов, таких как оператор присваивания, условный оператор, оператор цикла и т.д. </p>
# <p>Выражения могут быть однострочными и многострочными. Многострочные выражения можно переносить на другие строки с помощью круглых скобок(), фигурных скобок {} , квадратных скобок [] , обратной косой черты \ .</p>
# <p>В Python  конец строки означает конец выражения. Выражения можно написать в нескольких строках. Можно завершать выражение с помощью точки с запятой ;. За счет этого можно размещать несколько выражений в одной строке.</p>

# |Переменная|Оператор присваивания|Операнд|Оператор конкатенации|Операнд|
# |:-:|:-:|:-:|:-:|:-:|
# |X|=|2|+|3|

number = 20  # это выражение с оператором присваивания

small = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
small

super_p = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
super_p

name = ["Zakieva" + " Ekaterina"]
name

first_name = "Ekaterina"
surname = " Zakieva"
first_name + surname

# **2. Переменные**</p>
# <p>Переменная - это некоторое имя, связанное со значением. Переменная ссылается на значение, но не тождественна ему.Когда переменной присваивается другое значение, старое сразу становится недействительным. </p>
# <p>Для переменных следует выбирать имена со смыслом, которые что-то говорят о хранимых данных. Это важно для читабельности кода. </p>
# <p>Компактные, содержательные имена важны для удобочитаемости вашей программы.</p>
#
# **Схемы регистра имен**</p>
# <p>Так как в идентификаторах Python различается регистр символов и они не могут содержать пробельные символы, программисты используют несколько схем в идентификаторах, состоящих из нескольких слов.</p>
# <p>Змеиный регистр (snake_case) разделяет слова символом подчеркивания, который напоминает ползущую между словами змею. В этом случае все буквы записываются в нижнем регистре, а константы часто записываются в верхнем змеином регистре (UPPER_SNAKE_CASE).</p>
# <p>Верблюжий регистр (camelCase) — слова записываются в нижнем регистре, но второе и следующие слова начинаются с заглавной. Эта схема в большинстве случаев подразумевает, что первое слово начинается с буквы нижнего регистра. Буквы верхнего регистра напоминают верблюжьи горбы.</p>
# <p>Схема Pascal (PascalCase) — названа так, потому что применяется в языке программирования Pascal; аналогична схеме верблюжьего регистра, но первое слово в ней тоже начинается с заглавной.</p>
#
# **Соглашения об именах PEP 8**</p>
# __В документе PEP 8 (глава 3) приведены некоторые правила формирования имен в Python.__
# 1. Все буквы должны быть буквами ASCII — то есть латинскими буквами верхнего и нижнего регистров без диакритических знаков.
# 2. Имена модулей должны быть короткими и состоять только из букв нижнего регистра.
# 3. Имена классов необходимо записывать в схеме Pascal.
# 4. Имена констант следует записывать в верхнем змеином регистре.
# 5. Имена функций, методов и переменных записывают в нижнем змеином регистре.
# 6. Первый аргумент методов всегда должен называться self в нижнем регистре.
# 7. Первый аргумент методов классов всегда должен называться cls в нижнем регистре.
# 8. Приватные атрибуты классов всегда начинают с символа подчеркивания ( _ ).
# 9. Публичные атрибуты классов никогда не начинают с символа подчеркивания ( _ )
# <p>PEP 8 содержит напоминание о том, что программист не обязан неуклонно следовать PEP 8. Важнейший фактор удобочитаемости — не выбор схемы, а последовательность в применении этой схемы.</p>

# __Длина имен__
# <p>Очевидно, имена не должны быть слишком короткими или слишком длинными. Длинные имена переменных утомительно вводить, а короткие могут быть непонятными или дезинформирующими. Но так как код читают чаще, чем пишут, лучше все-таки задавать более длинные имена переменных.</p>

# <p>В отдельных случаях короткие имена переменных вполне допустимы. Например, имя i часто используется с переменными циклов for, перебирающих диапазоны чисел или индексов списка, а j и k (следующие за i в алфавитном порядке) ис-
# пользуются с вложенными циклами:</p>
# <p>>>> for i in range(10):</p>
# <p>... for j in range(3):</p>
# <p>... print(i, j)</p>
#
# <p>Еще одно исключение — использование x и y для декартовых координат. В большинстве других случаев НЕЛЬЗЯ применять однобуквенные имена переменных.</p>

# __Обратите внимание также на следующие моменты:__
# <p>Слишком длинные имена.</p>
# <p>Префиксы в именах.</p>
# <p>Последовательные числовые суффиксы в именах.</p>
# <p>Выбирайте имена, пригодные для поиска.</p>
# <p>Избегайте шуток, каламбуров и культурных отсылок.</p>

# __Не заменяйте встроенные имена__
# <p>Никогда не используйте встроенные имена Python для своих переменных. Например, присвоив переменной имя list или set, вы заместите функции Python list() и set(), что позднее может привести к появлению ошибок. Функция list() создает объекты списков, но ее замена может вызвать ошибку.</p>
#
#

# __Итоги__
# <p>Выбор имен не имеет никакого отношения к алгоритмам или компьютерной теории, и все же это важнейший фактор написания удобочитаемого кода. В конечном счете выбор имен, используемых в вашем коде, остается на ваше усмотрение, но вы должны учитывать существующие рекомендации.</p>
# <p>В PEP 8 вы найдете несколько соглашений о выборе имен — например, имена в нижнем регистре для модулей и имена в схеме Pascal для классов. Имена не должны быть слишком короткими или слишком длинными. Однако часто лучше сделать имя избыточным, чем недостаточно содержательным.</p>
# <p>Имя должно быть лаконичным, но информативным. Оно должно легко находиться функцией поиска Ctrl-F. То, насколько просто можно найти выбранное имя, свидетельствует о его уникальности. </p>
# <p>Также задумайтесь, будет ли понятно это имя программисту, который недостаточно хорошо владеет английским языком; избегайте шуток, каламбуров и культурных отсылок в своих именах; вместо этого выбирайте имена прямолинейные, традиционные и без отсылок к хохмам. </p>
# <p>Избегайте имен, уже используемых стандартной библиотекой Python, — таких как all, any, date, email, file, format, hash, id, input, list, min, max, object, open, random, set, str, sum, test и type. Их применение может создать трудноуловимые ошибки в вашем коде.</p>
# <p>Для компьютера неважно, какие имена вы выбрали, содержательные или общие. Имена упрощают чтение кода людьми, а не выполнение его компьютерами. Если ваш код хорошо читается, он будет понятным. Если он понятен, его легко изменить. А если его легко изменить, вам будет проще исправить ошибки или добавить новые возможности. Использование понятных имен — основополагающий фактор разработки качественного программного обеспечения.</p>

# **3. Выполнение выражений**</p>
# <p>Выражение - это совокупность значений, переменных и операторов. Когда вы вводите в командной строке выражение, интерпретатор вычисляет его и выводит результат.</p>
# <p>In [ 3 7 ] : 2 + 3</p>
# <p>Out [ 3 7 ] : 5</p>
# <p>Выражения могут содержать значения, переменные и операторы, но не обязательно все их сразу. Само по себе значение тоже считается выражением, как и отдельно взятая переменная.</p>
# <p>In [ 38 ] : 1 5</p>
# <p>Out [3 8 ] : 1 5</p>
# <p>I n [39] : а</p>
# <p>Out [39] : 5</p>
# <p>Вычислить выражение - это не то же самое, что вывести его значение на экран. Покажем это на примере строки.</p>
# <p>In [ 4 0 ] : ' Hello World ! '</p>
# <p>lout [ 4 0 ] : ' Hello World ! '</p>
# <p>In [ 4 1 ] : print ( ' Hello World ! ' )</p>
# <p>1 Hello World !</p>
# <p>Когда интерпретатор Python выводит значение выражения, он использует тот же формат, который вы использовали бы для ввода значения. Для строк это означает, что будут выведены кавычки. Но если вы используете функцию print ( ) , Python
# отображает содержимое строки без кавычек.</p>

# **3.5. Первые шаги в программировании **</p>
# <p> Конечно, мы можем использовать Python для более сложных задач, чем сложение
# двух чисел. Например, можно вычислить начало ряда Фибоначчи Пример 1.

# Пример 1
# Ряд Фибоначчи - сумма двух элементов является следующим элементом ряда.
first = 0  # последовательное многострочное присвоение переменных
second = 1
# верхний предел для первого значения - 10
# Цикл while выполняется до тех пор, пока условие остается истинным (в первом
# варианте это было а < 1 0. В Python истинным является любое ненулевое
# целочисленное значение, ноль считается ложным. Условие также может быть
# строкой или списком и вообще любой последовательностью. При этом все, что
# имеет ненулевую длину, считается истинным, а пустые последовательности -
# ложными.
# Стандартные операторы сравнения записываются привычным образом: < (меньше),
# > (больше), == (равно), <= (меньше или равно), >= (больше или равно) и ! =
# (не равно).
while first < 10:
    # Тело цикла записано с отступом. Отступы - это способ группировки
    # выражений в Python. В интерактивном режиме интерпретатора для задания
    # отступа нужно использовать табуляцию или пробелы. На практике код бывает
    # гораздо более сложным, и у всех специализированных текстовых редакторов
    # есть функция автоматического отступа. Когда составное выражение вводится
    # в интерактивном режиме, за ним должна следовать пустая строка,
    # указывающая на завершение (поскольку синтаксический анализатор не может
    # угадать, когда блок кода закончился). Обратите внимание, что у всех
    # строк в блоке должен быть одинаковый отступ.
    # Функция print ( ) выводит значение переданного аргумента на экран. Ее
    # работа отличается от простого написания выражения в строке, т. к. эта
    # функция по-другому обрабатывает несколько аргументов, числа с плавающей
    # запятой и строки. Строки выводятся без кавычек, а между аргументами
    # вставляется пробел, что позволяет красиво форматировать результаты.
    print(first)
    # The line `first, second = second, first + second` is performing parallel
    # assignment in Python. This means that the values on the right side of
    # he assignment operator (`=`) are evaluated first, and then assigned to
    # he variables on the left side simultaneously.
    # Параллельное присваивание значение переменных, каждый объект ссылается
    # на разные объекты. First  - ссылается на second.  Second - ссылается на
    # сумму двух объектов.
    # Выражения в правой части вычисляются слева направо.
    first, second = second, first + second

# Пример 1
first = 0
second = 1
while first < 10:
    print(first)
    # Только так надо записывать последовательное присваивание значение
    # переменной, благодаря этому мы видим на какой конечный объект ссылается
    # переменная. First  - ссылается на сумму двух объектов.
    first, second = second, first + second

# Мастер-класс от SENATOROV
# используется параллельное присваивание значения переменных
first, second = 0, 1
while first < 10:
    print(11, first)
    # first = second
    # second = first + second
    # print(22, first, second)
    print(33, first, second)
    first, second = second, first + second

# **4.  Подробнее о функции print()**</p>
# <p>Рассмотрим пару важных понятий на примере функции print ( ) . Поскольку вы будете часто использовать ее, это будет полезно само по себе.
# Мы уже видели, что функция print ( ) выводит любой аргумент, который мы указываем в скобках.</p>
# <p>Фактический синтаксис функции print( ) выглядит так:</p>
#
# **print ( *objects, sep= ' ' , end= ' \n ' , file=sys . stdout, flush=False )**</p>
#
# <p>На примере этого синтаксиса рассмотрим еще две важные концепции программирования
# на Python:</p>
# <p>♦ Позиционные аргументы (иногда обозначаемые словом args);</p>
# <p>♦ Ключевые аргументы (иногда обозначаемые словом kwargs).</p>
#
# <p>Аргументы - это все, что мы передаем в функцию. Например, в функцию print ( ) мы передавали строку или переменную - это и есть аргументы. Если при определении функции вы хотите передавать ей больше одной переменной, но еще не знаете точно, сколько аргументов у вас будет, можно указать специальный синтаксис *args. </p>
# <p>Символ * здесь означает, что мы можем передать функции любое количество переменных, а слово args - это своего рода стандартное соглашение, которое используется для лучшей читаемости кода. Можно использовать и любое другое слово, если оно будет достаточно значимым. Как видите, в синтаксисе функции print ( ) вместо *args используется слово *objects. </p>
# <p>Теперь вы знаете, что это означает, и в функцию print ( ) можно передать несколько аргументов (переменных, строк,
# классов или любых других объектов).</p>
#
# <p>Ключевые аргументы - это аргументы, для которых при передаче в функцию указывается не только значение, но и имя. И здесь давайте остановимся и рассмотрим подробнее это понятие на пример синтаксиса функции print ( ) .</p>
# <p>Вы заметили в заголовке функции слова sep=, end=, file= и flush=? Это именованные аргументы, у них есть имя, а справа от символа = указано присвоенное им значение.</p>
# <p>Значения, указанные в определении функции, являются значениями по умолчанию.</p>
# <p>То есть если вы не назначите такому аргументу другое значение, будет передано значение по умолчанию, и синтаксических ошибок не возникнет.</p>
# <p>Теперь, разобравшись с аргументами и именованными аргументами, давайте разберемся, что означает синтаксис print ( ) и как с ним работать.</p>
#
# <p>Еще раз:</p>
# <p>print (*objects , sep= ' ' , end= ' \n ' , file=sys . stdout, flush=False )</p>
# <p>Параметры функции print ( ) :</p>
# <p>♦ *objects - любое количество любых объектов. Перед выводом все объекты собираются в строку;</p>
# <p>♦ sep= ' ' (необязательный) - задает разделитель объектов, если их несколько. Значение по умолчанию - символ пробела, указанный как ' ' ;</p>
# <p>♦ end= ' \n ' (необязательный) - определяет, что вывести в конце строки. Значение по умолчанию - символ переноса строки ' \n ' ;</p>
# <p>♦ file=sys.stdout (необязательный) - объект с методом write (string) . Если этот параметр не указан, будет использоваться sys.stdout по умолчанию, что означает вывод результатов на экран;</p>
# <p>♦ flush=False (необязательный) - логическое значение, указывающее, будет ли вывод очищен (тrue) или буферизован (False). По умолчанию имеет значение False.</p>
#
# <p>А теперь потренируемся. Обратите внимание на изменения в следующих строках кода. Для лучшего понимания мы будем использовать тот же простой код для ряда Фибоначчи, который мы написали ранее.</p>
#
# <p>а , Ь = О, 1</p>
# <p>while а < 1 5 :</p>
# <p>print (a, end= ' , ' )</p>
# <p>а , Ь = Ь, а + Ь</p>
# <p>1 о, 1 , 1 , 2 , 3, 5 , в, 1 3 ,</p>
# <p>Теперь попробуйте самостоятельно по задавать разные значения именованным аргументам функции print ( ) и посмотреть, что изменится.</p>

num1, num2 = 0, 1
while num1 < 15:
    print(num1, end=" WOW\n")
    num1, num2 = num2, num1 + num2

#
# **5.  Форматированный вывод**</p>
# <p> В двух приведенных примерах если вы измените значения переменных, то выходные данные тоже изменятся вместе с ними. Этот инструмент будет весьма полезен вам в следующих главах.</p>

number1 = 2
number2 = 45
number1number2 = number1 * number2
f"when {number1} is multiplied by {number2}, the result i {number1number2}"

# вариант со строками
name_ = "Nilabh"
lastname_ = "Nishchhal"
place = "Mumbai"
f"He {name_} {lastname_} lives in {place}"

# **6.  Простейшая геометрия и print()**</p>
# <p> Мы рассмотрели использование функции print ( ) и ее синтаксис. Теперь нарисуем треугольник, используя только базовый код. Это простейший способ вывода фигур. </p>
#
#

print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /     |")
print("/______|")

# ## 7. ПОИСК ОШИБОК ##
# <p> К поиску ошибок приходится прибегать в случаях, когда наш код не выдает желаемого результата или вообще ничего не выводит. Если код не выдает результат, вероятно, где-то возникла ошибка. Сообщения об ошибке в Python пишутся довольно
# подробно и позволяют точно понять, в чем заключается и где находится ошибка.</p>
# <p>Рассмотрим три основных типа ошибок, которые возникают чаще всего.</p>
# <p>♦ Синтаксическая ошибка - проблемы с языковыми конструкциями.</p>
# <p>♦ Ошибка времени выполнения - проблемы с выполнением кода.</p>
# <p>♦ Семантическая ошибка - неожиданный результат.</p>

# **7.1. Синтаксические ошибки.**
# <p> Эти ошибки обычно вызваны опечатками, но в более широком смысле наличие такой ошибки означает, что возникла проблема со структурой вашей программы. Ошибка возникает, когда вы пишете код, не соблюдая синтаксис Python. Приведенное ниже сообщение об ошибке Python указывает на ошибку в синтаксисе.</p>
#
# <p> File "<ipython-input-4 9-9d0e3bd45f27>" , line 3</p>
# <p> print ( "Hello World ! )</p>
# <p> SyntaxError : EOL while scanning string literal</p>
#
# <p> В сообщении об ошибке сказано, что со строковым литералом что-то не так. Кроме того, ошибка указывает на место, где была найдена проблема.</p>
#
# <p> In ( 5 0 ] : # пропущен оператор между 4 и 5</p>
# <p> х = З+ 4 5</p>
# <p> х</p>
# <p> File "<ipython-input-50-44afЬ4dc20cc>" , line 3</p>
# <p> х = 3+ 4 5</p>
# <p> SyntaxError : invalid syntax</p>
#
# <p> И снова в тексте ошибки указан тип ошибки и место, где найден неверный синтаксис.</p>
# <p>Лучшее решение, чтобы избежать длительного поиска ошибок, - это запускать программу через каждые несколько строк кода. Столкнувшись с ошибкой, вам нужно будет проверить лишь самые последние изменения, и с большой долей вероятности
# ошибка будет именно в них.</p>

# **7.2. Ошибки времени выполнения.**
#
# <p>Ошибки времени выполнения возникают во время работы программы. Поскольку Python является интерпретируемым языком, такие ошибки возникают лишь в тот момент, когда выполнение программы доходит до ошибочной строки.</p>
#
# <p>Частые причины таких ошибок следующие:</p>
# <p>♦ неверно введенное имя переменной или функции;</p>
# <p>♦ использование переменной до ее определения;</p>
# <p>♦ имя должно было быть заключено в кавычки;</p>
# <p>♦ деление на ноль.</p>
#
# <p>Ошибка времени выполнения возникает, когда Python понимает саму команду, но при ее выполнении сталкивается с проблемами. Поэтому эта ошибка и называется «времени выполнения», поскольку возникает только после запуска программы.</p>
#
# <p>In ( 5 1 ) : 5/0</p>
# <p>ZeroDivisionError Traceback (most recent call last)</p>
# <p><ipython-input-51-0106664d39e8> in <module></p>
# <p>----> 1 5/0</p>
# <p>ZeroDivisionError : division Ьу zero</p>
#
# <p>Здесь синтаксис кода правильный, но интерпретатор не умеет делить на О. Следовательно, программа запускается, но выдает ошибку. Это ошибка времени выполнения.</p>

# **7.3. Семантические ошибки.**
#
# <p>Семантические или логические ошибки - это проблемы с самим построением вашей программы. Обычно такие проблемы не вызывают сообщений об ошибках, но поведение программы оказывается неверным. Ошибки такого типа сложнее всего
# отследить.</p>
#
# <p>Эти ошибки часто бывают вызваны случайным использованием неверных переменных либо просто неправильными вычислениями.</p>
#
# <p>In [52) : # мы хотим вывести "Hello Nilabh"</p>
# <p>name_ = "Nilabh"</p>
# <p>print ( "Hello name " )</p>
# <p>Hello name_</p>
#
# <p>Вы можете заметить, что в этом примере сообщение об ошибке отсутствует. Но и желаемого результата мы не получили. <p>Причина в том, что мы думали, что передаем переменную name и Python выведет ее значение. А Python воспользовался строковым синтаксисом и понял все буквально.</p>
#
# <p>Семантические ошибки - самые сложные в устранении.</p>

# **7.4. Когда никакие средства не помогают ...**
# <p>Вы можете столкнуться с ситуациями, когда найти ошибку, которая приводит к серьезному сбою вашей программы, не удается. </p>
# <p>В этом случае можно предпринять несколько шагов:</p>
# <p>1 . Поиск в Интернете. Лучшее место для поиска ответов - это сайт stackoverflow.com</p>
# <p>2. Избегать таких случаев. Всегда стоит сначала писать несколько строк кода, а затем выполнять программу. Затем добавлять еще несколько строк кода и снова запускать. Столкнувшись с проблемой, вам достаточно будет просмотреть
# несколько последних изменений, которые вы внесли, и проблема найдется быстрее.</p>
# <p>3. Промежуточные версии. Следует сохранять промежуточный прогресс в разработке программы каждый раз, когда вы начинаете писать новую часть. Если вы достигли определенного этапа, сделайте резервную копию. Для этого достаточно
# выбрать пункт меню Save as и назвать свой файл filename2.py, затем filename3.py и т. д. Если вы работаете с filename7.py и столкнулись с нерешаемой проблемой, можно просто вернуться к filename6.py. По окончании работы можно просто убрать все старые файлы в архив и переименовать окончательный файл по своему усмотрению.</p>
# <p>4. Комментарии. Вы можете попытаться закомментировать проблемный участок кода, чтобы посмотреть, сохранится ли проблема. Вы можете использовать возможности среды IDE, чтобы поместить символ комментария перед всеми строками
# выделенного фрагмента кода. Попробуйте изолировать разные участки кода, чтобы сузить область поиска проблемы.</p>
# <p>5. Все сначала. Когда ничего не помогает, вы можете начать писать заново, с нового пустого файла. Затем скопируйте и вставьте небольшие фрагменты кода из старого файла по одному. Каждый раз, добавляя новый раздел, запускайте свою
# программу и проверяйте, не появилась ли проблема.</p>

# **7.5. Резюме.**
# <p>В этой главе мы сперва познакомились с о Spyder IDE и Jupyter Notebook.</p>
# <p>Затем мы начали работу с Python и научились использовать его в качестве калькулятора. </p>
# <p>Мы также проделали несколько манипуляций со строками. </p>
# <p>Затем мы обратились к базовой структуре кода Python и узнали, что такое выражения, операторы и переменные.</p>
# <p>Мы также написали первую многострочную программу и изучили несколько принципов написания кода на Python, таких как множественное присваивание, отступы, цикл и вывод результата. </p>
# <p>Затем мы рассмотрели, как работает функция print ( } , и ее синтаксис помог нам разобраться еще с двумя понятиями, такими как аргументы и именованные аргументы. </p>
# <p>Последней темой, которую мы рассмотрели, был поиск ошибок, и это тоже невероятно важно.</p>

# ## УПРАЖНЕНИЯ
# ### Ответьте на вопросы.
#
# <p>1 . В чем преимущества редактора Spyder IDE по сравнению с простым текстовым редактором?</p>
# <p>Интегрированная Среда Разработки (с английского Integrated Development Environment) - это инструмент для разработки программного обеспечения, совмещающий в себе качества текстового редактора и компилятора. Таким образом, IDE - это более продвинутый инструмент, чем текстовый редактор. Однако, VS code - прекрасный текстовый редактор, который на основе расширений и плагинов соперничает с IDE при этом оставаясь легче и быстрее.</p>
#
# <p>2. Программирование — это:</p>
# <p>1. Написание правил, оговоренных в спецификации ЯП. </p>
# <p>2. Тестирование написанных правил.</p>
# <p>Программирование — это процесс написания лексических, синтаксических и семантических правил, оговоренных в спецификации языка программирования (ЯП), с последующим его тестированием и получением удовлетворительного конечного результата.</p>
#
# <p>3. Как в Python пишутся операторы сложения, вычитания, умножения и деления?</p>
# <p>+, -, *, /</p>
#
# <p>4. В чем разница между операторами * и **? Что они означают в Python?</p>
# <p>* - умножение, ** - возведение в степень.</p>
#
# <p>5.Что такое выражения в Python? Зачем они нужны? </p>
# <p>Выражение - это совокупность значений, переменных и операторов. Когда вы вводите в командной строке выражение, интерпретатор вычисляет его и выводит результат.</p>
#
# <p>6. Что такое переменная? Как присвоить переменной какое-либо значение?</p>
# <p>Переменная - это некоторое имя, связанное со значением. Переменная ссылается на значение, но не тождественна ему.Когда переменной присваивается другое значение, старое сразу становится недействительным.  Для присвоения переменной какого-либо значения используется оператор =. </p>
#
# <p>7. Можно ли в Python дать переменной имя import? Обоснуйте ответ.</p>
# <p> Имя переменной не должно совпадать ни с каким из зарезервированных в Python ключевых слов. Вот их список: and, as, assert, async, await, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield. В Python ключевое слово import применяется для того, чтобы сделать код в одном модуле доступным для работы в другом.</p>
#
# <p>8. В Python имена maths, maths эквивалентны MATHS. Так ли это на самом деле? Обоснуйте свой ответ.</p>
# <p>Имена переменных в Python чувствительны к регистру (БОЛЬШИЕ или маленькие буквы). Это значит, что если в имени переменной мы использовали только буквы нижнего регистра (например, abc), то воспользоваться значением, сохраненном в переменной, мы можем, только указав имя переменной в точно таком же виде, в том же регистре.
# В документе PEP 8 (глава 3) приведены некоторые правила формирования имен в Python. Первый пункт гласит: Все буквы должны быть буквами ASCII — то есть латинскими буквами верхнего и нижнего регистров без диакритических знаков.
# Вместе с тем, Python (начиная с версии 3) строки хранятся в кодировке Unicode. Это позволяет использовать в них в том числе буквы национальных алфавитов: от русских до китайских иероглифов. НО! Программа на языке Python (начиная с версии 3) должна сохраняться в кодировке utf-8. Тогда в ней можно использовать русские буквы, как в строковых литералах, так и в именах переменных и функций, но последнее является очень плохим стилем — никогда так не делайте.</p>
#
# <p>9. Каким образом можно группировать выражения в Python?</p>
# <p>Круглые скобки используются для группировки (). Отступы - это способ группировки выражений в Python.</p>
#
# <p>10. В чем разница между синтаксической ошибкой и семантической ошибкой?</p>
# <p>Синтаксические ошибки обычно вызваны опечатками, но в более широком смысле наличие такой ошибки означает, что возникла проблема со структурой программы. Ошибка возникает, код пишется без соблюдения синтаксиса Python. Семантические или логические ошибки - это проблемы с самим построением вашей программы. Обычно такие проблемы не вызывают сообщений об ошибках, но поведение программы оказывается неверным. </p>
#
# <p>11. Каково значение по умолчанию именованных аргументов sep и end в синтаксисе функции print()?</p>
# <p>♦ sep= ' ' (необязательный) - задает разделитель объектов, если их несколько. Значение по умолчанию - символ пробела, указанный как ' ' ;</p>
# <p>♦ end= '\n' (необязательный) - определяет, что вывести в конце строки. Значение по умолчанию - символ переноса строки '\n'.</p>
#
# ## Правда или ложь.
# <p>1 . Простое деление четного числа на 2 вернет объект типа int (целое число).</p>
# <p>Ложь.</p>
# <p>Оператор деления / всегда возвращает тип float</p>
# <p>IN type(5/2)</p>
# <p>OUT float</p>
#
# <p>2. Положительный индекс строки начинается с О, а отрицательный индекс начинается с - 1 .</p>
# <p>Истина.</p>
#
# |P|Y|T|H|O|N|
# |-|-|-|-|-|-|
# |0|1|2|3|4|5|
# |-6|-5|-4|-3|-2|-1|
#
# <p>3. Строки Python можно изменять, или, другими словами, они изменяемы.</p>
# <p>Ложь.</p>
# <p>Строки в Python являются “неизменяемыми”, что означает, что их нельзя изменить после их создания. </p>
#
# <p>4. Dream team - это допустимое имя переменной в Python.</p>
# <p>Ложь.</p>
# <p>Имена переменных не могут содержать пробелов.</p>
#
# <p>5. В Python можно дать переменной имя lambda.</p>
# <p>Ложь.</p>
# <p>Имя переменной не должно совпадать ни с каким из зарезервированных в Python ключевых слов. Вот их список: and, as, assert, async, await, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield. </p>
#
# <p>6. Выражения в Python завершаются точкой ( . ).</p>
# <p>Ложь.</p>
# <p>В Python  конец строки означает конец выражения. Выражения можно написать в нескольких строках. Можно завершать выражение с помощью точки с запятой ;.</p>
#
# <p>7. Выражения а = 25 и а == 25 в Python эквивалентны.</p>
# <p>Ложь.</p>
# <p>'=' - это оператор присваивания, '==' - это оператор сравнения.</p>
#
# <p>8. Вывод выражения с использованием функции print ( ) - это не то же самое, что вычисление этого выражения.</p>
# <p>Истина.</p>
#
# <p>9. Семантические ошибки являются подвидом синтаксических ошибок.</p>
# <p>Ложь.</p>
#
# <p>10. Деление на ноль вызывает ошибку времени выполнения.</p>
# <p>Истина.</p>

# ## Практические задания.

# 1 . Напишите программу, в которой бы соединялись ваши имя и фамилия.
# Между ними должен быть пробел.
my_name_ = "Ekaterina"
my_lastname_ = "Zakieva"
f"{my_name_} {my_lastname_}"

# 2. Прямоугольник имеет длину l и высоту h.
# Напишите код для вычисления площади прямоугольника с высотой 8 и длиной 23.
# В коде должно быть присвоение значений переменным l и h,
# чтобы один и тот же код можно было использовать повторно.
# Для вычисления площади прямоугольника нужно его длину умножить на высоту.
length = 8
height = 23
the_area_of_the_rectangle = length * height
the_area_of_the_rectangle

# 3. Чему равен квадрат числа 32 и куб числа 27?
# Напишите оператор, который ответит на этот вопрос.
32**2, 27**3

# 4. Напишите приведенное ниже уравнение на Python.
# Присвойте числовые значения переменным и вычислите результат.
# ( а + Ь )2 = a2 + b2 + 2ab
letter_a = 2
letter_b = 2
check_bool_1 = (
    letter_a + letter_b
) ** 2 == letter_a**2 + 2 * letter_a * letter_b + letter_b**2
power_second_number = (letter_a + letter_b) ** 2
expression = letter_a**2 + 2 * letter_a * letter_b + letter_b**2
tuple((check_bool_1, power_second_number, expression))

# 5. Найдите длину своего имени, написав однострочный код на Python.
len("Ekaterina")

# 6. Нарисуйте прямоугольник, используя функцию print ( ).
print(" _______")
print("|       |")
print("|       |")
print("|       |")
print("|       |")
print("|       |")
print("|_______|")

# 7. Нарисуйте букву «Р» с помощью простейшей геометрии и функции print ( ).
print(" _______")
print("|       |")
print("|       |")
print("|_______|")
print("|")
print("|")
print("|")

# 8. Создайте переменную Name и присвойте ей свое имя.
# Переменной Age присвойте свой возраст.
# Затем напишите оператор print ( ) ,
# который выведет текст «меня зовут Name, а мой возраст - Age»,
# с подставленными значениями ваших переменных.
# Значения Name и Age должны быть строкой и числом соответственно.
Name = " Ekaterina"
Age = 46
print("Меня зовут", Name, ", мой возраст - ", Age, " лет.", sep="")
"Меня зовут", Name, ", мой возраст - ", Age, " лет."
# tuple(("Меня зовут", Name, ", мой возраст - ", Age, " лет."))
# в предыдущей строчке закоментила очевидный повтор верхней строки
# так работает VS CODE автоматически

# 9. Исправьте синтаксическую ошибку в следующих строках кода:
# words = [cat, window, defenestrate]
# for w in words :
# print (w, len(w))
words = ["cat", "window", "defenestrate"]
for w_ in words:
    print(w_, len(w_))

# 1О. Исправьте синтаксическую ошибку в следующих строках кода:
# а, Ь = О, 1
# while а < 1 5 :
# print (a, end= ' , ' )
# а , Ь = Ь, а + Ь
a_, b_ = 0, 1
while a_ < 15:
    print(a_, end=", ")
    a_, b_ = b_, a_ + b_

# ## Изучите самостоятельно##

# <p> 1 . Запишите свое имя на бумаге. Под именем напишите положительные и отрицательные индексы строки.</p>
#
# |E|K|A|T|E|R|I|N|A|
# |-|-|-|-|-|-|-|-|-|
# |0|1|2|3|4|5|6|7|8|
# |-9|-7|-7|-6|-5|-4|-3|-2|-1|

# <p>2. Постепенно начните в качестве калькулятора использовать Spyder IDE или Jupyter Notebook.</p>

0, 6 * 0, 8 * 0, 2 * 0, 4

# <p>3 . Зайдите на сайт stackoverflow.com. Он станет вашим лучшим помощником, когда вы начнете учиться на своих ошибках.</p>
