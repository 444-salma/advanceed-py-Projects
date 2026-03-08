import math
import random2
def ArthemiticOperations (Fn , Sn , Op):
    
         if Op =="+":
           return int(Fn) + int(Sn)
         elif Op =="-":
           return int(Fn) - int(Sn)
         elif Op =="/":
          return int(Fn) / int(Sn) 
         elif Op =="*":
          return int(Fn) * int(Sn)
         elif Op == "power":
          return math.pow(int(Fn), int(Sn))
         elif Op == "sqr":
          return math.sqrt(int(Fn))
         elif Op == "random":
          return random2.randint(int(Fn) , int(Sn))
         else:
          return "Invalid Operation"  
        
