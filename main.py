import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS command (
    title TEXT,
    point BIGINT
)""")

db.commit()

command_name = input("Название команды: ")
command_point = input("Количество баллов: ")

sql.execute("SELECT title FROM command")
if sql.fetchone() is None:
    sql.execute("INSERT INTO command VALUES (?, ?)", (command_name, command_point))
else:
    print('Команда уже зарегистрирована')


