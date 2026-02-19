from random import randint

class train:
      def __init__(self,trainNo):
          self.trainNo = trainNo
      
      def book(self , fro , to):
          print(f"your ticket is booked from {fro} to {to} on the train number {self.trainNo}")
          
      def getstatus(self):
          print(f"train no : {self.trainNo} is on the time")
          
      def cancelticket(self , ticketno):
          print(f"your ticket no {ticketno} is cancelled on train no {self.trainNo}")
          
      def getfare(self,fro,to,seattype):
          
          print(f"your seat type is {seattype} on train no {self.trainNo}")
          if (seattype == "sleeper"):
              print(f" the fare for train no {self.trainNo} from {fro} to {to} the fare for sleeper seat is {randint(500 , 1500)}")
          elif  (seattype == "AC"):
             print(f" the fare for train no {self.trainNo} from {fro} to {to} the fare for AC seat is {randint(2000, 5000)}")
                
          
t = train(19045)
t.book("delhi" , "mumbai")
t.getstatus()
t.getfare("delhi" , "mumbai","AC")
       
             
    
        