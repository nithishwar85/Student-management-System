def search_student():

    roll = int(input("Enter Roll Number : "))

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:

        print(student)

    else:

        print("Student Not Found")
