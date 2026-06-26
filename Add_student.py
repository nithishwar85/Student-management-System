def add_student():

    roll = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    dept = input("Enter Department : ")
    cgpa = float(input("Enter CGPA : "))

    cursor.execute(
        "INSERT INTO students VALUES(?,?,?,?)",
        (roll, name, dept, cgpa)
    )

    connection.commit()

    print("Student Added Successfully")
