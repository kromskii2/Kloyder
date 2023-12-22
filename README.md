# README.md

## Скрипт для управления программой

Этот скрипт предоставляет простой интерфейс для управления программой. Он включает в себя функции для аутентификации пользователя, управления учетными данными, а также запуска и управления программой.

### Функции скрипта:

1. **get_hwid():**
   - Функция для получения идентификатора оборудования (HWID) на основе информации о системе.

2. **encrypt_password(password):**
   - Функция для шифрования пароля с использованием алгоритма MD5.

3. **save_credentials(login, password):**
   - Функция для сохранения учетных данных (логина и зашифрованного пароля) в файле `config.ini`.

4. **load_credentials():**
   - Функция для загрузки учетных данных из файла `config.ini`.

5. **authenticate_main_password():**
   - Функция для аутентификации основного пароля. Пользователь вводит главный пароль, который сравнивается с сохраненным паролем.

6. **main_menu():**
   - Функция для отображения главного меню с опциями: запустить программу, сменить пароль, сменить пользователя, выйти.

7. **run_software():**
   - Функция для запуска программы. Скачивает файл по указанному URL, сохраняет его во временный файл и запускает процесс.

8. **main():**
   - Основная функция программы, обеспечивающая логику взаимодействия с пользователем. Предоставляет интерфейс для ввода учетных данных, аутентификации, отображения информации об устройстве и основного меню.

### Запуск программы:

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.x).

2. Запустите скрипт из командной строки:

   ```bash
   python script.py
   ```

3. Следуйте инструкциям в консоли для ввода учетных данных, аутентификации и выбора опций из главного меню.

### Примечание:

- Перед использованием замените фиктивные значения (например, URL для загрузки файла и основной пароль) на фактические ваши данные.
- Убедитесь, что файл `config.ini` находится в том же каталоге, что и скрипт, и имеет правильные разрешения для записи.
