def display_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print()

    for student in students:

        print(student)
