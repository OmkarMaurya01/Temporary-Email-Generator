from mailtm import Email
from time import sleep

class TempMail():
    
    target_test = None
    Perm = False 
    verification_link = None
    
    def get_email(self):
        while True:
            try:
                test = Email()
                test.register()
                self.target_test = test
                break
            except Exception as e:
                print(e)
                continue
        return test.address
    
    # def get_response(self,message):
        
    
    def get_response(self):
        self.target_test.start(self.listener)
        while not self.Perm:sleep(1)
        self.target_test.stop()
        return self.verification_link 
            
    
    def listener(self,message):
        list_ = message['text'] if message['text'] else message['html']
        self.verification_link = list_
        self.Perm = True
        
       
        
    
if __name__ == '__main__':
    tmepmail = TempMail()
    email = tmepmail.get_email()
    print(email)
    print("Waiting for verification link")
    verification_link = tmepmail.get_response()
    print(verification_link)
    # input()

    