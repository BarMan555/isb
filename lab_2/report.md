## Отчет о лабороторной работе №2

### Генерация случайных последовательностей 
Были успешно созданы и протестированы генераторы на язык C++(generator.cpp) и Java(RandomBitSequence)

С их помощию были созданы ГСПЧ:

* C++ : 11000111101100011110100000010110111100101000110000010100011101111011101011110000001010101100001101111000000000110110010101011110

* Java :  11111001011101001000000111100110101010011010100110011110100100110100001000011001110110101010000101101001000011011001101110010010

Последовательны были записаны в sequence.json

### Проведение 3 тестов линейки NIST на сгенерированной последовательности

Во второй части работы были написаны три теста NIST. 

1. Частотный побитовый тест
2. Тест на одинаковые подряд идущие биты
3. Тест на самую длинную последовательность единиц в блоке

Условие случайности последовательности: $P_{value}> 0.01$

__Результаты тестов:__

Для С++ последовательности
1. Частотный побитовый тест - 0.8596837951986662
2. Тест на одинаковые подряд идущие биты - 0.37813571020101566
3. Тест на самую длинную последовательность единиц в блоке - 0.718013202470707

Для Java последовательности
1. Частотный побитовый тест - 0.7236736098317631
2. Тест на одинаковые подряд идущие биты - 0.21140702817801685
3. Тест на самую длинную последовательность единиц в блоке - 0.344312071738815

### Вывод
Были написыны 2 ГСПЧ с помощью генераторов на языках C++ и Java. После прохождения тестов, можно сделать вывод, что обе последовательноси _являются случайными_