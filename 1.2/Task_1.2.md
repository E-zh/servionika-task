### Задание 1.2
* Написал сервис API, модифицировав предыдущий файл.
* Установил на сервере `flask` и дополнительный модуль `flaskRESTful`.
* Файл `storage.py` переименовал в [app.py](/1.2/source/app.py), чтобы не настраивать `flask`.
* Запустил `flask` командой `flask run --host=0.0.0.0`:  
    ![](/1.2/image/2-5.jpg)  
* Проверяем с помощью cUrl:  
    ![](/1.2/image/2-4.jpg)  
* Проверяем через браузер, видим что все работает:  
    - главная страница:  
    ![](/1.2/image/2-1.jpg)  
    - получаем все данные:  
    ![](/1.2/image/2-2.jpg) 
    - получаем элемент по ключу:  
    ![](/1.2/image/2-3.jpg)  
* Файлы прилагаю:
    - [app.py](/1.2/source/app.py)
    - [storage.data](/1.2/source/storage.data)
* Создал из сервиса Docker контейнер:
    ```dockerfile
    FROM python:3.6
    
    WORKDIR /app
    
    COPY app.py .
    COPY requirements.txt .
    
    RUN pip install -r requirements.txt
    
    EXPOSE 5000
    
    CMD ["flask", "run", "--host=0.0.0.0"]
    ```
* Выполнил сборку, запустив `docker build -t my-task-1.2 .`, лог довольно большой, привожу частично:  
    ![](/1.2/image/2-6.jpg)  
* Выполняем `docker image list`, видим наш контейнер:  
    ![](/1.2/image/2-7.jpg)   
* Запускаем `docker run -d -p 5000:5000 my-task-1.2`, и проверим запустив `docker ps`:  
    ![](/1.2/image/2-8.jpg)  
* Как видим контейнер запущен. Проверяем через cUrl:  
    ![](/1.2/image/2-9.jpg)  
* Проверяем через web:  
    - получаем все данные:  
    ![](/1.2/image/2-11.jpg)  
    - получаем данные по ключу:  
    ![](/1.2/image/2-10.jpg)  
* Заходим в контейнер, выполнив `docker exec -it 04be6364afe7 sh` (заранее посмотрев ID контейнера), и посмотрим содержимое файла `storage.data`:  
    ![](/1.2/image/2-12.jpg) 
* Как видим файл создался, данные находятся в нем. При перезапуске они не сохранятся.
* Файлы прилагаю:
    - [app.py](/1.2/source/app.py)
    - [storage.data](/1.2/source/storage.data)
    - [Dockerfile](/1.2/source/Dockerfile)
    - [requirements.txt](/1.2/source/requirements.txt)
