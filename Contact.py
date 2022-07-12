
class App:

    def __init__(self):
        self.contacts = {}
    

    def create_contact(self):

        name= str(input(" Enter name")).lower()
        number = input("Enter Number")

        self.contacts[name] = {name:name, number:number}

    def find(self, name):
        for user in self.contacts.keys():
            if user == name.lower():
                print( self.contacts[user] )
        print('No user found')

    def delete(self,name):

        name= str(input(" Enter name")).lower()
        del self.contacts[name]
        print("Deleted" , self.contacts)

    def add_field(self):
        username= str(input(" Enter name")).lower()
        field_name= str(input(" Enter field")).lower()
        field_val= str(input(" Enter field value")).lower()

        self.contacts[username][field_name] = field_val
        print(self.contacts[username])

        
        
Server = App()

for i in range(100000000000):
    command = input("Enter your choice")
    if (command=="stop"):
        break
    elif command == "1":
        Server.create_contact()
    elif command == "2":
        Server.delete(input("Enter name to be deleted   :  "))
    elif command=="3":
        Server.find(input("Enter name to be searched   :  "))
    elif command=="4":
        Server.add_field()
    else:
        print("Enter Valid Command")





