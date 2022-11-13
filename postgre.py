import psycopg2
from psycopg2 import Error


try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="psqlar",
                                  # пароль, который указали при установке PostgreSQL
                                  password="Hgft667rD454w4e",
                                  host="172.20.19.48",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO lpwan.mquery(topic, payload)
                                       VALUES (%s,%s)"""
    record_to_insert = ('Incotex/TEST', '{"Steve":"Jobs"}')
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print (count, "Запись успешно добавлена ​​в таблицу mobile")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")