import math                                 
dat = input()                               
data = dat.split(" ")                       
k = int(data[0])                            
a = int(data[1])                            
b = int(data[2])                            
sum_ = math.sqrt(a**2 + b**2)               
for i in range(0, k):                       
    my_in = int(input())                    
    if my_in <= sum_:                       
        print("DA")                         
    else:                                   
        print("NE")                         
    i+=1      
