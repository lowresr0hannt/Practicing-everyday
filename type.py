class dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner


    def bark(self):
        print("woof woof")
        
class Owner:
    def __init__(self,name,address,contact_number):
        self.name= name
        self.address= address
        self.phone = contact_number
    

owner1=Owner("Danny","Delhi","999-009090808")
dog1 = dog("hell","street",owner1)
print(dog1.owner.name)


owner2=Owner("Rohan","Gr Noida","8897676388")
dog2 = dog("nah","pug",owner2)
print(dog2.owner.name)
