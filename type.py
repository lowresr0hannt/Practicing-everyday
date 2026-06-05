from datetime import datetime
class User:
    def __init__(self,username,email,password):
        self.username=username
        self._email=email
        self.password=password
        
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self,new_email):
        self._email=new_email
    
        
        
user1 =User("Rohan","rohan@mail.com","rohanyes1")

print(user1.get_email())

user1.set_email("rohan@hotlook.com")

print(user1.get_email())