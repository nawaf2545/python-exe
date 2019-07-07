amount= float(input("Please enter the amount"))

discout=0
final_amount =0

if amount >0 and amount <1000:
    discout = amount *(5/100)
    final_amount = amount - discout

elif amount >=1000 and amount <=5000:
    discout = amount *(10/100)
    final_amount = amount -discout

elif amount >5000:
    discout = amount *(15/100)
    final_amount = amount -discout
else:
    print("please enter correct number")

print("The disscount amount is", discout)
print("The final amount is",final_amount)
