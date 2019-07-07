class Students:
    def __init__(self,first_name,last_name,id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.email = first_name + " " + last_name + "@ un.com"
    def getFullname(self):
        return self.first_name + " " + self.last_name
    def getEmail(self):
        return self.email
if __name__ == '__main__':
    student1 = Students("Nawaf","Saleh",545)
    print("The full name is ",student1.getFullname(),"\nThe emil is",student1.getEmail())
    student2 = Students("Ahmed","ahmed",400)
    print("The full name is ",student2.getFullname(),"\nThe emil is",student2.getEmail())

