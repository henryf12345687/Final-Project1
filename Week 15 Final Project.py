import sqlite3

def main():
    #Connect to database
    conn = sqlite3.connect('student_database.db')

    #Generate Cursor
    cur = conn.cursor()

    #If no Database Generate it here
    create_table(cur)
    add_initial_entries(cur, conn)
    #Add entries
    #Acts as the menu
    while True:
        try:
            question = int(input("Type 1 view all entries"
                         "\nType 2 to add an entry"
                         "\nType 3 to change an entry"
                         "\nType 4 to delete an entry"
                         "\nType 5 to exit"
                         "\n--------------\n"))
        except ValueError:
            print("Invalid input. Please try again.")
        if question == 1:
            view_entries(cur)
        if question == 2:
            add_entry(cur, conn)
        if question == 3:
            change_entry(cur, conn)
        if question == 4:
            delete_entry(cur, conn)
        if question == 5:
            exit(0)

    #Save Changes
    conn.commit()
    #Close Connection
    conn.close()


def create_table(cur):

    cur.execute("""Create table IF NOT EXISTS Students(
    Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT,
    Last_Name TEXT,
    Major TEXT,
    GPA REAL,
    Credits_Earned INTEGER,
    Email TEXT,
    Enrollment_Status TEXT)""")



def view_entries(cur):
    cur.execute('SELECT * FROM Students')

    rows = cur.fetchall()

    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Major':<20} {'GPA':<5} {'Credits':<8} {'Email':<25} {'Status':<12}")
    print("-" * 110)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<20} {row[4]:<5} {row[5]:<8} {row[6]:<25} {row[7]:<12}")
def add_entry(cur, conn):
    more = 'y'
    while more.lower() == 'y':
        first_name = input('Enter First_Name: ')
        last_name = input('Enter Last_Name: ')
        major = input('Enter Major: ')
        GPA = input('Enter GPA: ')
        credits_earned = input('Enter Credits_Earned: ')
        email = input('Enter Email: ')
        enrollment_status = input('Enter Enrollment Status: ')

        cur.execute("INSERT INTO Students (First_Name, Last_Name, Major,"
                    "GPA, Credits_Earned, Email, Enrollment_Status ) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name,
                                                   last_name, major,
                                                   GPA, credits_earned,
                                                   email, enrollment_status))

        more = input('Do you want to add another entry? y/n')
def add_initial_entries(cur, conn):
    cur.execute('SELECT COUNT(*) FROM Students')
    count = cur.fetchone()[0]

    if count > 0:
        return
    students = [
        ("Henry", "Forst","Sports Analytics", 3.9, 30, "hankforst@gmail.com", "Part-Time"),
        ("Braden", "Phetsarath", "Buisness", 4.0, 35, "bp@gmail.com", "Full-Time"),
        ("Mike", "Johnson", "Computer Science", 3.7, 35, "mikejohn@yahoo.com", "Full-Time"),
        ("Sarah", "James", "Chemistry", 4.0, 40, "sjames@hotmail.com", "Graduated"),
        ("Michelle", "Adams", "Statistics", 3.6, 33, "michelleadams@gmail.com", "Part-Time"),
        ("Brian", "Shaw", "Nursing", 3.9, 38, "bshaw@yahoo.com", "Full-Time"),
        ("Logan", "True", "Engineering", 3.2, 30, "logtru@gmail.com", "Graduated"),
    ]
    cur.executemany("""
        INSERT INTO Students
        (First_Name, Last_Name, Major, GPA, Credits_Earned, Email, Enrollment_Status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,students)
    conn.commit()

def change_entry(cur, conn):
    student_id = input("Enter Student_ID to edit: ")
    cur.execute("SELECT * FROM Students WHERE Student_ID=?", (student_id,))
    row = cur.fetchone()

    if row is None:
        print('Student not found.')
        return
    print("Leave blank to keep current entry.")

    new_first = input(f"First Name ({row[1]}): ") or row[1]
    new_last = input(f"Last Name ({row[2]}): ") or row[2]
    new_major = input(f"Major ({row[3]}): ") or row[3]
    new_gpa = input(f"GPA ({row[4]}): ") or row[4]
    new_credits = input(f"Credits Earned ({row[5]}): ") or row[5]
    new_email = input(f"Email ({row[6]}): ") or row[6]
    new_status = input(f"Enrollment Status ({row[7]}): ") or row[7]
    
    cur.execute("""
        UPDATE Students
        SET First_Name=?, Last_Name=?, Major=?, GPA=?, Credits_Earned=?, Email=?, Enrollment_Status=?
        WHERE Student_ID=?
        """,(new_first, new_last, new_major, new_gpa, new_credits, new_email, new_status, student_id ))
    conn.commit()
    print("Entry updated successfully.")
def delete_entry(cur, conn):
    student_id = input("Enter Student_ID to delete: ")
    cur.execute("DELETE FROM Students WHERE Student_ID=?", (student_id,))
    conn.commit()
    print("Entry Deleted.")


if __name__ == "__main__":
    main()