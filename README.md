# RU
# Сервис расчета стоимости страхования

Докеризованное приложение для расчета стоимости страховки на основе объявленной стоимости и типа груза. Страховка рассчитывается по фактическим тарифам, взятым из json-файла. Используются FastAPI, Tortoise ORM и PostgreSQL.

---

## Описание проекта

Проект включает в себя JSON-файл с актуальными тарифами, расположенный в папке `src`. 

- Тарифы можно загрузить в базу данных PostgreSQL, выполнив запрос `POST /rates/upload`. 

- Обновить тарифы в базе данных можно, выполнив запрос `PATCH /rates/update`.

- Конечная точка `POST insurance/calculate` используется для расчета стоимости страховки. Для этого в качестве параметров запроса необходимо указать тип груза и заявленную стоимость. Стоимость страховки будет округлена до тысячных (0,001). В тестах были рассмотрены запросы на страхование.

---

## Запуск приложения

1. Клонируем репозиторий:

```bash
git clone https://github.com/AlekseyAmp/InsuranceCalculatorAPI
```

2. Создайте файл `.env` и введите в него свои данные в соответствии с форматом, приведенным в файле `.env-example`.

3. Соберите образ Docker:

```bash
docker build . -t insurance_calculator_app:latest
```

4. Соберите контейнеры Docker:

```bash
docker-compose build
```

5. Запустите контейнеры Docker:

```bash
docker-compose up
```

---

## Тестирование приложения

1. Перейдите в каталог ``tests``:

```
cd tests
```

2. Запустите тесты с помощью следующей команды:

```
pytest insurance_tests.py
```

-----

# EN
# Insurance Cost Calculation Service

Dockerized application to calculate insurance cost based on declared value and cargo type. Insurance is calculated by actual tariffs taken from json file. FastAPI, Tortoise ORM and PostgreSQL are used.

---

## Project Description

The project includes a JSON file with up-to-date rates located in the `src` folder. 

- You can upload these rates into the PostgreSQL database using the `POST /rates/upload` endpoint. 

- You can update the rates in the database by sending a `PATCH /rates/update` endpoint.

- Endpoint `insurance/calculate` is used to calculate the insurance price. To do this, you need to provide the cargo type and the declared cost as request parameters. The insurance cost will be rounded to the thousand (0,001). Request for insurance were covered by the tests.

---

## Running the Application

1. Clone the repository:

```bash
git clone https://github.com/AlekseyAmp/InsuranceCalculatorAPI
```

2. Create an `.env` file and enter your data following the format in `.env-example`.

3. Build the Docker image:

```bash
docker build . -t insurance_calculator_app:latest
```

4. Build the Docker containers:

```
docker-compose build
```

5. Start the Docker containers:

```
docker-compose up
```

---

## Test the application

1. Navigate to the `tests` directory:

```
cd tests
```

2. Run the tests using the following command:

```
pytest insurance_tests.py
```