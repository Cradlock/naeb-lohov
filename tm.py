import psycopg2

# Данные для подключения (из-под суперпользователя)
DB_NAME = "postgres"  # системная база, не путать с рабочей
DB_USER = "postgres"
DB_PASSWORD = "your_admin_password"
DB_HOST = "localhost"  # или IP-адрес сервера

# Данные нового пользователя
NEW_USER = "new_user"
NEW_PASSWORD = "secure_password"
TARGET_DB = "your_db_name"  # Название базы, к которой даем доступ

try:
    # Подключаемся как админ
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    conn.autocommit = True  # Нужно для команд CREATE USER и GRANT

    cursor = conn.cursor()

    # Создаем пользователя
    cursor.execute(f"CREATE USER {NEW_USER} WITH PASSWORD '{NEW_PASSWORD}';")

    # Даем права на базу
    cursor.execute(f"GRANT CONNECT ON DATABASE {TARGET_DB} TO {NEW_USER};")
    cursor.execute(f"GRANT USAGE, CREATE ON SCHEMA public TO {NEW_USER};")
    cursor.execute(f"GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO {NEW_USER};")

    cursor.close()
    conn.close()
    
    print(f"✅ Пользователь {NEW_USER} успешно создан и получил доступ к базе {TARGET_DB}!")

except psycopg2.Error as e:
    print(f"❌ Ошибка при создании пользователя: {e}")
