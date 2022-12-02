import sqlite3
import time as tm


con = sqlite3.connect("DB_mahdi_amir.db")
cur = con.cursor()


class modify_database:
    def create_table_student(self):
        cur.execute("CREATE TABLE if not exists student(sid int PRIMARY KEY ,name VARCHAR(50), code_meli int) ;")
        print("++ Table student created successfully")

    def create_table_course(self):
        cur.execute("CREATE TABLE if not exists course(cid int PRIMARY KEY ,course_name VARCHAR(50), year int) ;")
        print("++ Table course created successfully")

    def create_table_student_courses(self):
        # create table student_courses with foreign key sid & cid from student and courses tables
        cur.execute(
            "CREATE TABLE if not exists student_course(sid int ,cid int ,"
            "CONSTRAINT fk_sid "
            "FOREIGN KEY(sid) "
            "REFERENCES student(sid)"
            ",CONSTRAINT fk_cid "
            "FOREIGN KEY(cid) "
            "REFERENCES course(cid));")
        print("++ Table student_course created successfully")

    def insert_data_into_table_student(self):
        cur.execute("INSERT OR REPLACE INTO student(sid, name, code_meli) VALUES(100, 'Ali', 1250678912);")
        con.commit()
        print("++ Insert data into table_student successfully")

    def display_data_into_table_student(self):
        cur.execute("SELECT * FROM STUDENT;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("++ Show data into table_student successfully")

    def update_data_into_table_student(self):
        cur.execute("UPDATE student set name = 'Mahdi' WHERE sid = 100;")
        con.commit()
        print("++ Update data into table_student successfully")


# ---------------------------------------------------------------------------------------
# create object from class
db = modify_database()

db.create_table_student()
tm.sleep(1)

db.create_table_course()
tm.sleep(1)

db.create_table_student_courses()
tm.sleep(1)

db.insert_data_into_table_student()
tm.sleep(1)

print("** Display student table information: ")
db.display_data_into_table_student()
tm.sleep(1)

db.update_data_into_table_student()


# todo : add data to tables & add some function for SQL commands like SELECT INSERT UPDATE and ...
