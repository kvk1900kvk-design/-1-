import sqlite3

conn = sqlite3.connect("FruitBasket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    color TEXT
)
""")

cursor.execute("DELETE FROM Fruits")

cursor.execute("INSERT INTO Fruits (name, color) VALUES (?, ?)", ("Яблуко", "Червоне"))
cursor.execute("INSERT INTO Fruits (name, color) VALUES (?, ?)", ("Банан", "Жовтий"))
cursor.execute("INSERT INTO Fruits (name, color) VALUES (?, ?)", ("Апельсин", "Помаранчевий"))

cursor.execute(
    "UPDATE Fruits SET color = ? WHERE name = ?",
    ("Зелене", "Яблуко")
)

print("Жовті фрукти:")
cursor.execute("SELECT * FROM Fruits WHERE color = 'Жовтий'")
yellow_fruits = cursor.fetchall()
for fruit in yellow_fruits:
    print(fruit)

print("\nУсі фрукти:")
cursor.execute("SELECT * FROM Fruits")
all_fruits = cursor.fetchall()
for fruit in all_fruits:
    print(fruit)

conn.commit()
conn.close()
