## Enter any number

n = int(input("What number do you want to test?"))

while n != 1:
    
    if n % 2 == 0:
        n = n/2
        print(round(n))
       
       
    else:
        n = ((n*3) + 1)
        print(round(n))
        
