class emp:
    def __init__ (self, fname, lname):

        self.fname= fname
        self.lname = lname

    def __str__(self):
        
        return f"{self.fname} {self.lname}"
    

class empmanager:
    def __init__ (self):
        self.edict = {}

    def add(self, eid, e):

        try :
            self.edict [eid] = e
        except:
            print(f"this id ({eid}) has been already added")
    
    def show(self):
        try:
            print("employees: ")
            for i in sorted(self.edict.key()):
                print(f"employee's id: {i}, emplyee: {self.edict[i]}")

        except:
            print("your employee list is empty ")



class main():

    

    choice= int(input("1 for add 2 for show "))

    if choice == 1:
        fid = 0
        a = input("please enter employees first name: ")
        b = input("please enter employees last name: ")
        employee = emp(a , b)
        empmanager.add(fid , employee , fid)
        fid =+ 1
        
    elif choice == 2:
        empmanager.show()


main()

    