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
        cur.execute("INSERT OR REPLACE INTO student(sid, name, code_meli) VALUES(102, 'mohsen', 456625452);")
        cur.execute("INSERT OR REPLACE INTO student(sid, name, code_meli) VALUES(104, 'sara', 7854521252);")
        cur.execute("INSERT OR REPLACE INTO student(sid, name, code_meli) VALUES(106, 'reza', 5421000253);")

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

    def insert_data_into_student_course(self):
        cur.execute("INSERT OR REPLACE INTO student_course(sid, cid) VALUES(102,2000);")
        cur.execute("INSERT OR REPLACE INTO student_course(sid, cid) VALUES(104,3000);")
        cur.execute("INSERT OR REPLACE INTO student_course(sid, cid) VALUES(104,4000);")
        cur.execute("INSERT OR REPLACE INTO student_course(sid, cid) VALUES(106,7000);")
        cur.execute("INSERT OR REPLACE INTO student_course(sid, cid) VALUES(106,5000);")
        con.commit()

    def display_student_course_data(self):
        cur.execute("SELECT sid,cid FROM student_course;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("++ Show student_course successfully")




    def insert_data_into_table_course(self):
        course_data = [
                        [1000,'C++',2022],
                        [2000,'PHP',2020],
                        [3000,'Python',2023],
                        [4000,'C#',2018],
                        [5000,'ASP.NET',2020],
                        [6000,'C',2010],
                        [7000,'Ruby',2020]
                    ]
        insert_q = []

        for cou_data in course_data:
             cid = cou_data[0]
             course_name = cou_data[1]
             year = cou_data[2]
             q=f"INSERT OR REPLACE INTO course VALUES ('{cid}','{course_name}','{year}');"
             insert_q.append(q)

        for q in insert_q:
             cur.execute(q)

        con.commit()
        print("++ Insert data into table_course successfully")


    def display_courses_in_table_course(self):
        cur.execute("SELECT course_name FROM course;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("++ Show courses in table_course successfully")


    def display_inner_join(self):
        cur.execute("SELECT student.sid,student.name,student_course.cid FROM student inner join student_course on student.sid=student_course.sid ;")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def display_outer_join(self):
        cur.execute("SELECT student.sid,student.name,student_course.cid FROM student left join student_course on student.sid=student_course.sid ;")
        rows = cur.fetchall()
        for row in rows:
            print(row)



    def delete_data_into_table_course(self):
        cur.execute("DELETE FROM course WHERE year = 2020;")
        con.commit()
        print("-- delete data year = 2020 from table course successfully")


    #create view for select
    def create_view_for_select(self):
        cur.execute("CREATE VIEW [Course year] AS SELECT course_name FROM course WHERE year = 2020;")
        con.commit()
        print("++ create view for select successfully")



    #Procedure with INPUT Parameters
    """
    def procedure_insert_data_into_table_student(self):
        cur.execute("CREATE PROCEDURE insertStudent @sid int, @name VARCHAR(50), @code_meli int
                    AS INSERT OR REPLACE INTO student(sid, name, code_meli) VALUES(@sid, @name, @code_meli);")
        cur.execute("EXEC insertStudent @sid = 200, @name = 'Majid', @code_meli = 9401682915;")
        con.commit()


    #Procedure without Parameters
    def procedure_display_data_into_table_student(self):
        cur.execute("CREATE PROCEDURE displayStudent
                    AS SELECT * FROM student;")
        cur.execute("EXEC displayStudent;")
        con.commit()


    #Procedure include INPUT and OUTPUT Parameters
    def procedure_display_max_sid(self):
        cur.execute("CREATE PROCEDURE maxsid @id int, @n VARCHAR(50) output
                    AS SELECT @n=name FROM student WHERE sid=@id;")
        cur.execute("DECLARE @x char(10) EXEC maxsid 100, @x output print @x")
        con.commit()
    """






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
tm.sleep(1)


#insert data into table course
db.insert_data_into_table_course()
tm.sleep(1)

print("** Display courses: ")
db.display_courses_in_table_course()
tm.sleep(1)

db.delete_data_into_table_course()
tm.sleep(1)

print("** Insert data to student_course and display : ")
db.insert_data_into_student_course()
tm.sleep(1)

db.display_student_course_data()
tm.sleep(1)

db.create_view_for_select()
tm.sleep(1)

print("** display INNER jopin student and cource: ")
db.display_inner_join()

print("** display OUTER jopin student and cource: ")
db.display_outer_join()


# todo : add data to tables & add some function for SQL commands like SELECT INSERT UPDATE and ...
