try:
fi_obje = open("indix.txt","r")

data = fi_opje.read()
print(data)
fi_opje.close()
except FileNotFoundError:
    print("The file not found")
except Exception as e:
    print(e)
else:
    print(10*10)