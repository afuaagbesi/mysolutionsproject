print("-------------------------")
print("STUDENT MANAGEMENT SYSTEM")
print("-------------------------")
print("Welcome! Please select from the following options:")


def inquiry():
    print("Enter 1 to create a new student record")
    print("Enter 2 to access an existing student's record")
    print("Enter 3 to permanently delete a student's record")


inquiry()


class Individual:

    def __init__(self, first, last, studentid, course, level):
        self.first = first
        self.last = last
        self.studentid = studentid
        self.course = course
        self.level = level

    def __str__(self):
        return f"(firstname: {self.first}, lastname: {self.last}, studentid: {self.studentid}," \
               f" course: {self.course}, level: {self.level} )"


st_1 = Individual('Efua', 'Agbesi', 109001, 'Computer Engineering', 200)
st_2 = Individual('Jason', 'Garfield', 109002, 'Information Technology', 400)
st_3 = Individual('Emelia', 'Cruickshank', 109003, 'Sociology', 100)
st_4 = Individual('Andrew', 'Appiah', 109004, 'Business Administration', 300)
st_5 = Individual('Michael', 'Frimpong', 109005, 'Medicine', 100)

record = [st_1, st_2, st_3, st_4, st_5, st_5]


def add_entry():
    entry_first = input("Firstname:")
    entry_last = input("Lastname:")
    entry_id = int(input("ID:"))
    entry_course = input("Course:")
    entry_level = input("Level:")

    new_student = Individual(entry_first, entry_last, entry_id, entry_course, entry_level)
    # print(new_student)
    record.append(new_student)  # add student to list (DB)
    lastindex = len(record) - 1  # get last item's index
    print(record[lastindex])  # print the last item


try:
    entry = int(input("Enter your option:"))

    if entry == 1:
        # one = input("Press enter to add student's details:")
        # print(one)

        add_entry()
        print("Your student information has been successfully recorded. Thank you!")

    if entry == 2:
        two = input("Please enter student's identification number:")
    # print(two)


        def view_entry():
            pass

    if entry == 3:
        three = input("Please enter student's identification number:")
        print(three)
        if three in record:
            print()
            confirmation = input("Are you sure you want to delete the student's record. Press enter to confirm")
            del three

        else:
            print("Student record for that ID does not exist.")

except:
    print("Invalid input.")
