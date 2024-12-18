import sqlite3
#===DATABASE QUERIES===#
def create_db():
    con = sqlite3.connect("sgs.db")
    cur = con.cursor()
    
   
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subject (
        subjectID INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        duration TEXT, 
        units TEXT, 
        description TEXT
    );
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

    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS result (
        sid INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentID TEXT, 
        name TEXT, 
        subject TEXT, 
        marks_ob TEXT, 
        full_grades TEXT, 
        per TEXT,
        status TEXT,
        quarter TEXT
    );
    """)
    con.commit()

    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        username TEXT PRIMARY KEY, 
        password TEXT
    );
    """)
    con.commit()

    print("Database TEACHER created or already exist.")
    

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student_subject (
        ss_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        studentID INTEGER NOT NULL, 
        subjectID INTEGER NOT NULL, 
        FOREIGN KEY (studentID) REFERENCES student(studentID), 
        FOREIGN KEY (subjectID) REFERENCES subject(subjectID)
    );
    """)
    con.commit()

    print("Data transferred successfully.")

    cur.execute("SELECT * FROM result")

   
    rows = cur.fetchall()
    columns = [description[0] for description in cur.description]
    print("Columns:", columns)
    for row in rows:
        print(row)
    
    con.close()

create_db()
