def add(num1,num2):
    res = (num1 + num2)
    return res
def sub(num1,num2):
    res = (num1 - num2)
    return res
if __name__ == '__main__':
    number1 = int(input("enter first number: "))
    number2 = int(input("enter second number: "))
    res = add(number1,number2)
    print(res)
    res2 = sub(res,number2)
    print(res2)

