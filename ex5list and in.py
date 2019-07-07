pass_grade= ['A','B','C','D']
faile= "F"

grade=input("Please enter your grade")

if grade.upper() in pass_grade or grade.lower() in pass_grade:
    print("congratulation")
elif grade.upper() == faile or grade.lower() == faile:
    print("failed")
else:
    print("Please enter correct input")