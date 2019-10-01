from SQL.query import Query
from tkinter import *
import sqlite3 as sql

conn = sql.connect('students.db')  # record (id integer, name text, score integer)
cursor = conn.cursor()


class GuiApp(Frame, Query):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.insert_frm = Frame(self)
        self.insert_frm.grid(row=0)

        self.name = Label(self.insert_frm, text="Name")
        self.name.grid(row=0, column=0)

        self.name_entry = Entry(self.insert_frm)
        self.name_entry.grid(row=1, column=0)

        self.score_label = Label(self.insert_frm, text="Score")
        self.score_label.grid(row=0, column=1)

        self.score_entry = Entry(self.insert_frm)
        self.score_entry.grid(row=1, column=1)

        self.insert_btn = Button(self.insert_frm, text="Insert", command=self.insert_student)
        self.insert_btn.grid(row=1, column=2)

        self.show_all_btn = Button(self.insert_frm, text="Show All", command=self.show_all)
        self.show_all_btn.grid(row=2, column=1)

        self.delete_all_btn = Button(self.insert_frm, text="Delete All", command=self.delete_all)
        self.delete_all_btn.grid(row=2, column=0)

        self.update_frm = Frame(self)
        self.update_frm.grid(row=1)

        self.old_label = Label(self.update_frm, text="OLD")
        self.old_label.grid(row=0, column=1)

        self.new_label = Label(self.update_frm, text="NEW")
        self.new_label.grid(row=0, column=2)

        self.update_id_label = Label(self.update_frm, text="ID")
        self.update_id_label.grid(row=1, column=0)

        self.id_entry = Entry(self.update_frm)
        self.id_entry.grid(row=1, column=1)

        self.old_name_label = Label(self.update_frm, text="Name")
        self.old_name_label.grid(row=2, column=0)

        self.old_name_entry = Entry(self.update_frm)
        self.old_name_entry.grid(row=2, column=1)

        self.new_name_entry = Entry(self.update_frm)
        self.new_name_entry.grid(row=2, column=2)

        self.old_score_label = Label(self.update_frm, text="Score")
        self.old_score_label.grid(row=3, column=0)

        self.old_score_entry = Entry(self.update_frm)
        self.old_score_entry.grid(row=3, column=1)

        self.new_score_entry = Entry(self.update_frm)
        self.new_score_entry.grid(row=3, column=2)

        self.update_btn = Button(self.update_frm, text="Update", command=self.update_values)
        self.update_btn.grid(row=4, column=1, columnspan=2)
    
    def update_values(self):
        old_name = self.old_name_entry.get()
        new_name = self.new_name_entry.get()
        old_score = self.old_score_entry.get()
        new_score = self.new_score_entry.get()
        std_id = self.id_entry.get()
        query = "UPDATE record SET {} = '{}' WHERE {} = '{}'"
        if std_id:
            if new_name:
                with conn:
                    cursor.execute(query.format('name', new_name, 'id', std_id))
            if new_score:
                with conn:
                    cursor.execute(query.format('score', new_score, 'id', std_id))

        if old_name and new_name:
            with conn:
                cursor.execute(query.format('name', new_name, 'name', old_name))
        if old_score and new_score:
            with conn:
                cursor.execute(query.format('score', new_score, 'score', old_score))
        self.clear_all()

    def clear_all(self):
        self.id_entry.delete(0, 'end')
        self.new_name_entry.delete(0, 'end')
        self.old_name_entry.delete(0, 'end')
        self.new_score_entry.delete(0, 'end')
        self.old_score_entry.delete(0, 'end')

    def insert_student(self):
        name = self.name_entry.get()
        score = self.score_entry.get()
        std_id = self.get_last_id()
        query = "INSERT INTO record VALUES (:id, :name, :score)"
        payload = {'id': std_id + 1, 'name': name, 'score': int(score)}
        print(query, payload)
        with conn:
            cursor.execute(query, payload)
            conn.commit()
        self.name_entry.delete(0, 'end')
        self.score_entry.delete(0, 'end')

    def get_last_id(self):
        with conn:
            cursor.execute("SELECT id FROM record")
            std_id = cursor.fetchall()
            if not std_id:
                return 0
            else:
                return std_id[-1][0]

    def show_all(self):
        with conn:
            cursor.execute("SELECT * FROM record")
            print(cursor.fetchall())

    def delete_all(self):
        with conn:
            cursor.execute("DELETE FROM record")
            print(cursor.rowcount, "rows deleted")


if __name__ == '__main__':
    root = Tk(className="Students")
    GuiApp(root).pack(fill='both', expand=True)
    root.mainloop()
