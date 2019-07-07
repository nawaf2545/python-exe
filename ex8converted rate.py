dollar_list = []
ryal_list = []
for item in range(1,101):
    dollar_list.append(item)
converted_rate = float(input("Enter rate"))
while True:
    if converted_rate > 0 and converted_rate < 10:
        for item in dollar_list:
            ryal_list = item * converted_rate
            #ryal_list.append(ryal_value)

            print("The ryal list is \n",item,"dollar" "=",ryal_list,"ryal")
        break
    else:

        converted_rate = float(input("Rate should be greater than 0 and less than 10: "))

print("The dollar list is \n",dollar_list)

