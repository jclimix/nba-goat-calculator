import sqlite3

def insert_data():
    try:
        connection = sqlite3.connect(r'C:\Users\jezei\Downloads\sqlite-tools-win-x64-3450100\test.db')
        cursor = connection.cursor()

        data_to_insert = [
            (1, 'John'),
            (2, 'Alice'),
            (3, 'Bob')
        ]

        cursor.executemany("INSERT INTO test_tb (id, name) VALUES (?, ?)", data_to_insert)

        connection.commit()
        connection.close()

        print("Data successfully inserted into the table.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    insert_data()
