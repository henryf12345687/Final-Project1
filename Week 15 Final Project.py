import sqlite3

def main():
    #Connect to database
    conn = sqlite3.connect('student_database.db')

    #Generate Cursor
    cur = conn.cursor()

    #If no Database Generate it here
    create_table(cur)
    #Acts as the menu
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
        add_entry(cur)
    if question == 3:
        change_entry(cur)
    if question == 4:
        delete_entry(cur)
    if question == 5:
        exit(0)

    #Save Changes
    conn.commit()
    #Close Connection
    conn.close()


def create_table(cur):

    cur.execute("""Create table IF NOT EXISTS Students(
    Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name Text, 
    Last_Name Text,
    Major Text,
    GPA Real,
    Credits_Earned Integer,
    Email Text,
    Enrollment_Status Text)""")



def view_entries(cur):
    cur.execute('SELECT * FROM Students')

    rows = cur.fetchall()

    print("-----------Entries-----------")
    for row in rows:
        print(f"Student_ID: {row[0]},"
              f"First_Name: {row[1]},"
              f"Last_Name: {row[2]},"
              f"Major: {row[3]},"
              f"GPA: {row[4]},"
              f"Credits_Earned: {row[5]},"
              f"Email: {row[6]},"
              f"Enrollment_Status: {row[7]}")
def add_entry(cur):
    more = 'y'
    while more.lower() == 'y':
        first_name = input('Enter First_Name: ')
        last_name = input('Enter Last_Name: ')
        major = input('Enter Major: ')
        GPA = input('Enter GPA: ')
        credits_earned = input('Enter Credits_Earned: ')
        email = input('Enter Email: ')
        enrollment_status = input('Enter Enrollment Status: ')

        cur.execute("INSERT INTO Entries (First_Name, Last_Name, Major,"
                    "GPA, Credits_Earned, Email, Enrollment_Status ) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name,
                                                   last_name, major,
                                                   GPA, credits_earned,
                                                   email, enrollment_status))

        more = input('Do you want to add another entry? y/n')

