import sqlite3
#===DATABASE QUERIES===#
def create_db():
    con = sqlite3.connect("sgs.db")
    cur = con.cursor()
    
    # Create course table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course(
            cid INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            duration TEXT, 
            charges TEXT, 
            description TEXT
        )
    """)
    con.commit()

    # Create student table 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            studentID INTEGER PRIMARY KEY, 
            name TEXT, 
            email TEXT, 
            gender TEXT, 
            dob TEXT, 
            contact TEXT, 
            admission TEXT, 
            city TEXT, 
            province TEXT, 
            region TEXT, 
            address TEXT
        )
    """)
    con.commit()

    # Create result table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result(
            sid INTEGER PRIMARY KEY AUTOINCREMENT, 
            studentID TEXT, 
            name TEXT, 
            course TEXT, 
            marks_ob TEXT, 
            full_grades TEXT, 
            per TEXT
        )
    """)
    con.commit()

    # Create student-course relationship table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student_course (
            sc_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            studentID INTEGER NOT NULL, 
            cid INTEGER NOT NULL, 
            FOREIGN KEY (studentID) REFERENCES student(studentID), 
            FOREIGN KEY (cid) REFERENCES course(cid)
        )
    """)
    con.commit()

    cur.execute("SELECT * FROM result")

   
    rows = cur.fetchall()
    columns = [description[0] for description in cur.description]
    print("Columns:", columns)
    for row in rows:
        print(row)
    
    con.close()

create_db()
