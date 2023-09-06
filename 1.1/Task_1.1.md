### Задание 1.1
* Virtualbox у меня уже был установлен, также была развернута ВМ centOS 8 stream:  
    ![](/1.1/image/1.1-1.png)  
* Написал скрипт, добавил в него еще ключ для получения всех значений `--all` (привожу фрагмент):  
     ```python
    parser.add_argument('--all', action='store_true', help='Get all data from storage file')
    
    args = parser.parse_args()
    
    if args.all:
        all_data = get_all_values()
        for key, value in all_data.items():
            print(f'{key}: {value}')
    ```
* Установил на centOS 8 Python 3.11.4:  
    ![](/1.1/image/1.1-2.png)  
*  И проверил работу скрипта, как видим все работает, как на centOS так и на Windows 10:  
    ![](/1.1/image/1.1-3.png)
* Прилагаю файлы:  
    - [storage.py](/1.1/source/storage.py)
    - [storage.data](/1.1/source/storage.data)
