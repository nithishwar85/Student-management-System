def update_student():

    roll = int(input("Enter Roll Number : "))

    cgpa = float(input("Enter New CGPA : "))

    cursor.execute(

        "UPDATE students SET cgpa=? WHERE roll_no=?",

        (cgpa, roll)

    )

    connection.commit()

    print("Student Updated")
