# Bercut test assignment

## Tasks

1) Тест дизайн для формы:
https://docs.google.com/document/d/1xE4vC8l0VhuhKLYJuz7AUMBRTtOIvLShneQoLzTULJo/edit?usp=sharing

2) Develop RestApi calculator service

### Specification
Support 4 resources with same signature for call. For full information check swagger file
```
/v1/add
/v1/diff
/v1/multi
/v1/div
```

### Environment:
0) Use Unix like OS
1) Install docker
2) Install docker-compose

### How to use
1) Build service
    ```
    docker-compose build
    ```
2) Start service (add `-d` if want to start service in background )
    ```
    docker-compose up
    ```
3) Execute tests
    ```
    docker-compose run api test
    ```

#### P.S.
Какие недочеты не убирал и какие мысли появились.
1) Можно расширить логирование для тестов
2) Добавить описание к параметрам тестов, через ids. Так будет более наглядно понятно, 
почему были выбраны определенные значения
3) Писать пояснения к ассертам в конкретных случаях не вижу смысла. При выводе в репорт или консоль значение справа `ожидаемое`.
4) Возможно для тестов во втором задании было бы лучше просто назначить классы эквивалентности
[x.x, 0.x, -x.x, -0.x, 0.00000x, 0, x, -x, -0.00000x, x.00000x, -x.00000x] и просто их перемножить, 
тем самым получив большинство возможных случаем, но тогда получается гораздо блольше тестов.... 
В общем это больше 
вопрос для дискуссии, интересно ваше мнение)
5) Как же я не завидую разработчикам, которые работают с форматированным выводом чисел)
