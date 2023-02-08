import math

class calculator():
    
    def addition(self,num1,num2):
        print("addition of numbers: {0}".format(num1+num2))
                
    def subtraction(self,num1,num2):
        print("substraction of numbers: {0}".format(num1-num2))

    def multiplication(self,num1,num2):
        print("multiplication of numbers: {0}".format(num1*num2))  
                
    def division(self,num1,num2):
        print("division of numbers: {0:0.2f}".format(num1/num2))
    
    def remainder(self,num1,num2):
        print("Remainder of numbers: {0}".format(num1%num2))
    
    def floor_division(self,num1,num2):
        floor = num1//num2
        res1 = round(floor,2)
        res2 = math.floor(res1)
        print("round and floor of numbers is matching: {0},{1}".format(res1,res2))
        
    def square(self,num1):
        print("Square of number: {0}".format(num1**2))
                    
    def square_root(self,num1):
        print("Square Root of number: {0}".format(math.sqrt(num1)))
        
    def cube(self,num1):
        print("Cube of number: {0}".format(num1**3))
        
    def cuberoot(self,num1):
        print("Cuberoot of number: {0:0.2f}".format(num1**(1/3)))
    
    def nth_degree(self,num1,n):
        print("Nth Degree of number: {0}".format(num1**(n)))

    def nth_root(self,num1,n):
        print("Nth root of number: {0:0.2f}".format(num1**(1/n)))
        
    def currency_conversion(self,cur1):
        usd = cur1*0.012
        ind = cur1*82.16
        print("Indian to US Dollar {0},US Dollar to Indian {1}".format(usd,ind))
    
    def area_of_triangle(self,base,height):
        print("Area of triangle: {0}".format((base*height)/2))
        
    def split_bill(self,amount,candidate):
        print("Split of bill: {0}".format(amount/candidate))
        
'''    def percentage(self,amount):
        print("Percentage: {0}".format(amount/)'''
        
        

    #list_of_operations = ['addition','subtraction','multiplication','division','remainder','floor_division','square','square_root','cube','cube_root','nth_degree','nth_root']


token = True
while token:
    print(['1: addition','2: subtraction','3: multiplication','4: division','5: remainder','6:floor_division',
                          '7: square','8: square_root','9: cube','10: cube_root','11: nth_degree','12: nth_root',
                            '13:currency_conversion','14:area_of_triangle','15:split_bill'])
    
    choice = int(input("Enter the number as you want to calculate as per list : "))
    #num1 = int(input("Enter a number1 you want to calculate : "))
    #num2 = int(input("Enter a number you want to calculate : "))
    if choice == 11 or choice == 12:
        num1 = int(input("Enter a number1 you want to calculate : "))
        n = int(input("Enter a number you want as a nth root of : "))
    elif choice == 13:
        cur1 = int(input("Enter a amountyou want to change into Indian to US Dollar or US Dollar to Indian : "))
        #cur2 = int(input("Enter a amountyou want to change into US Dollar to Indian : "))
    elif choice == 14:
        base = int(input("Enter a base value you want to calculate the area of triangle : "))
        height = int(input("Enter a height value you want to calculate the area of triangle : "))
    elif choice == 15:
        amount = int(input("Enter a amount wnat to split : "))
        candidate = int(input("Enter a candidate number you want to split by : "))
    # elif choice != 0 or choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5 or choice != 6 or choice != 7 or choice != 8 or choice != 9 or choice != 10 or choice != 11 or choice != 12 or choice != 13 or choice != 14 or choice != 15:
    #     print('unknown_choice')
    elif choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
        num1 = int(input("Enter a number1 you want to calculate : "))
        num2 = int(input("Enter a number2 you want to calculate : "))
    elif choice == 7 or choice == 8 or choice == 9 or choice == 10: 
        num1 = int(input("Enter a number1 you want to calculate : "))

         
    obj = calculator()

    #for i in list_of_operation:
    if choice == 1:
        obj.addition(num1,num2)
    elif choice == 2:
        obj.subtraction(num1,num2)
    elif choice == 3:
        obj.multiplication(num1,num2)
    elif choice == 4:
        obj.division(num1,num2)
    elif choice == 5:
        obj.remainder(num1,num2)   
    elif choice == 6:
        obj.floor_division(num1,num2)
    elif choice == 7:
        obj.square(num1)
    elif choice == 8:
        obj.square_root(num1)
    elif choice == 9:
        obj.cube(num1)
    elif choice == 10:
        obj.cuberoot(num1)
    elif choice == 11:
        obj.nth_degree(num1,n)
    elif choice == 12:
        obj.nth_root(num1,n)
    elif choice == 13:
        obj.currency_conversion(cur1)
    elif choice == 14:
        obj.area_of_triangle(base,height)
    elif choice == 15:
        obj.split_bill(amount,candidate)
    
    repeat = input('\n Want to calculate again yes or no : ')
    if repeat =='no':
        token = False

    
