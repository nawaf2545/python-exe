import re
pattern = ["python","java","c+"]
text = "i love python"
for lang in pattern:
    if re.search(lang,text):
        print("text match")
    else:
        print("text not match")
#pattern = "^[a-zA-Z]*$"
#name = input("Please enter your name")
#if re.match(pattern,name):

    #print("text match")
#else:
  #  print("text not match")
