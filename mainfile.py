import operations
import student
import teachers

print(operations.add_numbers(9,3))
print(operations.sub_numbers(9,3))
print(operations.mult_numbers(9,3))
print(operations.div_numbers(9,3))

new_student = student("Keith","Cycling","2003")
student.greet_student()


new_teacher = teachers("Mr.Koomedy",str(39905071),"Mathematics",str(50,000))
student.greet_teacher()