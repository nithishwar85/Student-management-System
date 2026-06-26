def delete_student():

    roll = int(input("Enter Roll Number : "))

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll,)
    )

    connection.commit()

    print("Student Deleted")
