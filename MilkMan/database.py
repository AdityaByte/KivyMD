import sqlite3

class DataBase:
    
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.curser = self.con.cursor()
        self.create_task_table()
    
    def create_task_table(self):
        self.curser.execute("CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT , Person , Milk , Address , Price , Starting_date , Ending_date)")
        self.con.commit()
    
    def create_task(self , Person , Milk , Address , Price , Starting_date , Ending_date):
        self.curser.execute("INSERT INTO tasks(Person , Milk , Address , Price , Starting_date , Ending_date) VALUES(? , ? , ? , ? , ? , ?)", (Person , Milk , Address , Price , Starting_date , Ending_date))
        self.con.commit()

        created_task = self.curser.execute("SELECT id , Person , Milk , Address , Price , Starting_date , Ending_date FROM tasks WHERE Person = ? ", (Person,)).fetchall()
        return created_task[-1]
    
    def get_tasks(self):
        tasks = self.curser.execute("SELECT id, Person , Milk , Address , Price , Starting_date , Ending_date FROM tasks ").fetchall()
        return tasks
    
    def close_db_connection(self):
        self.con.close()
