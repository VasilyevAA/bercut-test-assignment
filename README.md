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
