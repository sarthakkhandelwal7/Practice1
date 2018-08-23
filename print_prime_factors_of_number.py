#Have the user enter a number and find all Prime Factors (if there are any) and display them.

class Factors:
    def __init__(self,number):
        self.number=number
        self.count = 0
        self.prime_factors_list = []
    def check_factors(self):
        for i in range(1,self.number):
            if(number%i==0):
                prime=self.prime_factors(i)
                if (prime!= None):
                    self.prime_factors_list.append(prime)
                
    def prime_factors(self,factor):
        
        if(factor%2!=0):
            for y in range(2,factor):
                if factor%y==0:
                    self.count+=1
                    break
            if self.count==0:
                return factor
                
        elif(factor==2):
            return factor
another = True
while another:
    number=int(input("Please enter a number:"))
    factors=Factors(number)
    factors.check_factors()
    print(f'Prime factors are {factors.prime_factors_list}')
    another=input("Do you wanna check another number press y or n:")
    if another[0].lower()=='y':
        another = True
    else:
        another = False
        