Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений. 


Входной текст на языке **yaml** принимается из стандартного ввода. Выходной текст на **учебном конфигурационном языке** попадает в стандартный вывод. 
Многострочные комментарии: 
|# 
Это многострочный 
комментарий 
#| 
Массивы: 
{ значение. значение. значение. ... } 
Словари: 
dict( 
имя = значение, 
имя = значение, 
имя = значение, 
... 
) 
Имена: 
[_A-Z][_a-zA-Z0-9]* 
Значения: 
• Числа. 
• Строки.
• Массивы. 
• Словари. 
Строки: 
[[Это строка]] 
Объявление константы на этапе трансляции: 
def имя = значение; 
Вычисление константного выражения на этапе трансляции (постфиксная 
форма), пример: 
$имя 1 +$ 
Результатом вычисления константного выражения является значение. 
Для константных вычислений определены операции и функции: 
1. Сложение. 
2. len(). 
3. min(). 
Все конструкции учебного конфигурационного языка (с учетом их 
возможной вложенности) должны быть покрыты тестами. Необходимо показать 2 
примера описания конфигураций из разных предметных областей.

**ЗАПУСК**

Перед запуском необходимо установить дополнительную библиотеку для работы программы:
**pip install pyyaml**

Для запуска программы перейдите в папку с помощью **cd** и выполните следующее в консоли: **type input.yaml | python transform_tool.py**

Для передачи в программу другого файла: **type input1.yaml | python transform_tool.py**
