import sqlite3

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


# ---------------------------------------------------------------------------------------
# create object from class
db = modify_database()

db.create_table_student()
db.create_table_course()
db.create_table_student_courses()

# todo : add data to tables & add some function for SQL commands like SELECT INSERT UPDATE and ...
