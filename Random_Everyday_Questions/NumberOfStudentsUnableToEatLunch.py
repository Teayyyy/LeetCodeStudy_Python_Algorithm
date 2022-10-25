class CountStudents:
    def count_students(self, students: [int], sandwiches: [int]) -> int:
        # Students who do not like top sandwiches should go to the end of the queue
        wait_count = 0

        def move_end(students: [int]):
            top = students.pop(0)
            students = students + [top]

        # the number of the students and sandwiches are the same
        for i in range(len(students)):
            if wait_count == len(sandwiches):
                return False
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                move_end(students)
                wait_count += 1
        return True

    def count_student_another_way(self, students: [int], sandwiches: [int]) -> int:
        while students:
            if not students.__contains__(sandwiches[0]):
                return len(students)
            else:
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    top = students.pop(0)
                    students += [top]
        return 0

    def count_student_optimized(self, students: [int], sandwiches: [int]) -> int:
        # you should count the sandwiches, not the damn students
        students_count = [students.count(0), students.count(1)]
        while students:
            if students_count[sandwiches[0]] <= 0:
                return len(students)
            else:
                if students[0] == sandwiches[0]:
                    students_count[students[0]] -= 1
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    top = students.pop(0)
                    students += [top]
        return 0

    def count_goddamn_students_optimize_ultra(self, students: [int], sandwiches: [int]) -> int:
        for i in sandwiches:
            if i in students:
                students.remove(i)
            else:
                break
        return len(students)

c = CountStudents()
# print(c.count_students(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
# print(c.count_student_optimized(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
print(c.count_student_optimized(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
