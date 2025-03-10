# i =100
# while i>=1:
#     print(i)
#     i -= 1

# n = int(input("enter the number:"))
# i=1
# while i <= 10:
#     print(n*i)
#     i+=1

# num  = [1,4,9,16,25,36,49,64,81,100]
# idx =0

# while idx < len(num):
#     print(num[idx])
#     idx += 1

# nums = [1,4,9,16,25,36,49,64,81,100]

# x = 25
# i =0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx",i)
#     i += 1



# nums = [1,4,9,16,25,36,49,64,81,100]

# for i in nums:
#     print(i)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("enter the number:"))
# idx =0
# for i in nums:
#     if i == x:
#         print("found at",idx)
#     idx += 1

# for  i in range(0,101):
#     print (i)

# for i in range(100,0,-1):
#     print(i)

# n = int(input("enter the number :"))

# for i in range(1,11):
#     print(n*i)

# n = 5 
# sum = 0 
# for i in range(1,n+1):
#     sum += i
# print("total sum =",sum)

# n = int(input("enter the number:"))
# sum = 0
# i = 1
# while i<=n:
#     sum += i 
#     i += 1
# print("total=",sum)  

# n = int(input("enter the number:"))
# fact = 1

# for i in range(1,n+1):
#     fact *= i
# print("factorial :",fact)

# def cal_sum(a,b):
#     sum = a + b
#     print(sum)
#     return(sum)
# cal_sum(6,9)

# def cal_avg(a,b,c):
#     sum = a + b + c
#     avg = sum/3
#     print(avg)
#     return avg 
# cal_avg(86,98,87)
# nums =["ajay","nani","As"]
# def len_list(nums):
#     print(len(nums))

# len_list(nums)

    
# cities = ["hyd","london","us","india"]
# def element_list(list):
#     for i in list:
#         print(i, end="")
# element_list(cities)
# print()


# def fact_num(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac *= i
#     print(fac)
# fact_num(5)
# fact_num(10)


# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val,"USD=",inr_val,"INR" )
# converter(100)


# def input(n):
#     if (n%2 == 0):
#         print("Even")
#     else:
#         print("Odd")
# input(18)


# def show(n):
#     if n ==0:
#         return
#     print(n)
#     show(n-1)
# show(5)



# def fac(n):
#     if n ==0 or n==1:
#         return 1
#     return fac(n-1)*n

# print(fac(5))      

# def cal_sum(n):

#     if n == 0:
#         return 0
#     return cal_sum(n-1) + n 

# res = cal_sum(5)
# print(res)


# def print_list(list,idx=0):
#     if idx ==len(list):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# fruits = ["apple","banna","stra","berry"]

# print(print_list(fruits))



# with open ("practise.txt","r") as f:
#      data = f.read ()
#      print(data)
#      newdata = data.replace("python","java")

#      print(newdata)


# with open ("practise.txt","r") as f :
#     data = f.read()
#     print(data)

#     num = data.split(",")
#     for i in range(len(data)):
#         if data[i]== ",":
#             print(int(num))
#         else:
#             num += data[i]

# class Car:
#     Brand = "LandRover" 
#     def __init__(self,model,year):
#         self.model = model
#         self.year  = year 

# mod = Car("Discovery",2020)
# print(mod.Brand,mod.model,mod.year)


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hello",self.name,"your avgscore is :", sum/3)

# s1 = Student("shark", [90,76,68])
# s1.get_avg()
# s1.name = "bigman"
# s1.get_avg()

# s2 = Student("tony",[78,98,89])
# s2.get_avg()


# class Account:

#     def __init__(self,bal,accountno):
#         self.balance = bal
#         self.accountno = accountno
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("total balance =",self.get_balance())
        
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("total balance =",self.get_balance())


#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000,34567)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(50000)
# acc1.debit(15000)


# class Car:

#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutuch = False

#     def start(self):
#         self.clutuch = True
#         self.acc = True
#         print("Car has been started..")
#     def brand(self,model,type,year):
#         self.mod = model 
#         self.type = type
#         self.year = year

# Car1 = Car()
# Car1.start()
# Car1.brand("landrover","fuel",2020)

# class Person:
#     __name = "annonymous" 

#     def __hello(self):
#         print("hello")
#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())

# class Car:

#     @staticmethod
#     def start():
#         print("started")
#     @staticmethod
#     def stop():
#         print("stop")

# class Landrover(Car):

#     def __init__(self,name):
#         self.name = name 

# car1 = Landrover("discovery")
# car2 = Landrover("defender")
# car1.start()
# car2.stop()

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 22/7*self.radius**2
#     def perimeter(self):
#         return 2*22/7*self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def show_deatils(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)
# class Enginner(Employee):
#     def __init__(self, name,age):
#         self.name = name 
#         self.age = age
#         super().__init__("engineer","tech","90,000")


# emp1 = Enginner("mask",45)
# emp1.show_deatils()

# class Order:
#     def __init__(self,item,price):
#         self.item = item 
#         self.price = price 

#     def __gt__(self,od2):
#         return self.price>od2.price

# od1 = Order("chips",30)
# od2 = Order("mixture",60)

# print(od1>od2)






# def armstrong_num(num):
#     nums = str(num)
#     n = len(nums)
#     sum = 0 
#     for digit in nums: 
#         sum += int(digit) ** n
#     if num == sum:
#         print(num,"is an a armstrongnumber")
#     else:
#         print(num,"is not a armstrong number")


# armstrong_num(15)




# def is_prime_num(n):
      
#     for i in range (2,n):
#         if n % i == 0:
#               print(n,"its not a prime number")
#               break
#     else:
#         print(n,"its a prime number")

# is_prime_num(151)


# def odd_even(n):
        
#         if n % 2 == 1 :
#             print(n,"its odd")
            
#         else:
#          print(n,"its even")

# odd_even(9)

# def my_function(*kids):
#     print("my name is",kids[1])

# my_function("ajay","sriram","aj","nani")


# def count(i,j):

#     if i >6 and j >6:
#         return print("Given value is more than the limit !!")
#     while i <=4:
#         print("*")
#         while j<=5:
#             print("*,*")
#             break
#         i += 1
#         j += 1
        
# count(1,1)

# def armstrong_num(num):
#     n = str(num)
 
#     x = len(n)
#     sum = 0
#     for i in n :
#         sum  += int(i)**x
#         if sum == num :
#             print("its armstrong number")
#             break
#     else:
#         print("its not a armstrong number")    

# armstrong_num(372)
    



# def squrt(num):

#     min = 0
#     max = str(num) 
#     for i in max:
#         sqt = (min+int(max))/2
#         root = sqt**2
#         if root == num:
#             break

#     print("given squareroot of",num,"=",sqt)
# squrt(9)

# def area_tran(l,b,w):

#     s = (l + b + w) / 2
#     area = (s*(s-l)*(s-b)*(s-w))**0.5
#     print('The area of the triangle is %0.2f'%area)

# area_tran(5,6,7)



# def swap(x,y):

#     temp = x
#     x = y 
#     y = temp
#     print('the value of x after swapping : {}'.format(x))
#     print('the value of y after swapping : {}'.format(y))

# swap(8,10)

# import random

# print(random.randint(10,19))


# def converter(val):
#     miles = val/1.609
#     print(miles)
# converter(5)

# def conv_celsius(val):
#     F = val*(9/5)+32
#     print(F)
# conv_celsius(40)

# def conv_fahr(fah):
#     celsius = (fah-32)/1.8
#     print(celsius)
# conv_fahr(108)


# def check_number(num):

#     if num >0:
#         print(num,"postive number")
#     elif num ==0:
#         print(num,"Zero value")
#     else:
#         print(num," negtive number")

# check_number(8)
# check_number(0)
# check_number(-2)


# def check_even_odd(num):

#     if num/2 == 0:
#         print(num,"its even number")
#     else:
#         print(num,"its odd number")

# check_even_odd(6)

# def check_leapyear(n):

#     if n/4 == 0 and  n/400 == 0 :
#         if n/100 !=0:
#             print(n,"its leap year")
#     elif n/4 !=0:
#         print(n,"not a leap year")

# check_leapyear(2012)

# def find_largest(x,y,z):
    
#     if x>=y and x>=z:
#         print(x,"its largest among the number")
#     elif y>=z:
#           print(y,"its largest among the number")
#     else:
#            print(z,"its largest among the number")

# find_largest(776,777,778)

# def check_primenum(num):

#     flag = False

#     if num == 0 or num ==1:
#         print(num,"is not aprime number")
#     elif num>1:
#         for i in range(2,num):
#             if num%i == 0:
#                 flag = True
#                 break
#         if flag:
#             print(num,"its not prime number")
#         else:
#             print(num,"its a primenumber") 

# check_primenum(13)   


# def check_prime(lower,upper):

#     for num in range(lower,upper+1):

#         if num >1:
#             for i in range(2,num):
#                 if (num%i) == 0:
#                     break
#             else:
#                 print(num)

# check_prime(90,100)

# def check_fact(num):

#     fact = 1
#     if num < 0:
#         print("factorial doesnt exist for negative number")
#     elif num == 0 :
#         print(" factorial of 0  is 1")
#     else:
#         for i in range(1,num+1):
#             fact = fact*i
#         print("the factorial of ",num,"is",fact)

# check_fact(5)


# def table(num):

#     for i in range(1,11):
#         print(num,"x",i,"=",num*i)

# table(30)




# def fibo(num):
#     n1,n2 = 0,1
#     count = 0 
#     if num<=0:
#        print("enter a postive number")
#     elif num == 1:
#        print("fib series",num,":")
#     else:
#        print("fib series")
#        while count<num:
#           print(n1)
#           nth = n1 + n2
#           n1 = n2
#           n2 = nth
#           count += 1        
# fibo(7)



# def armstrong(num):
#      sum = 0 
#      for i in str(num):
          
# armstrong()


# import random,string

# pass_leng = 8

# charval = string.ascii_letters + string.punctuation + string.digits

# res = "".join([random.choice(charval) for i in range(pass_leng)])

# print("your random password:",res)


# password = ""
# for i in range(pass_leng):
#      password += random.choice(charval)
# print(password)

# lower = 100
# upper = 2000

# for num in range(lower,upper+1):
    
#      order = len(str(num))
#      sum = 0 

#      temp = num 
#      while temp>0:
#           digit = temp %10
#           sum += digit**order
#           temp //= 10
#      if num == sum:
#           print(num)

# num = 16

# if num < 0:
#     print("enter the larger number")
# else:
#     sum = 0
#     while num >0:
#         sum += num 
#         num -= 1
# print("sum of :",sum)     


# num = 5
# factorial = 1

# if num < 0 :
#     print("sorry ,factprial doesnt exist of negtive number")
# elif num == 0 :
#     print("the Zero factorial is 1")
# else:
#     for i in range(1,num +1):
#         factorial = factorial*i
#     print("The factorial of ",num,"is",factorial)




# nterm = int(input("enter the number:"))

# n1,n2 = 0,1
# count = 0
# if nterm <=0:
#     print("please enter the postive number")
# elif nterm ==1:
#     print("Fibonacci sequence upto",nterm,":")
# else:
#     print("fibonacci sequence")
#     while count < nterm:
#         print(n1)
#         nth = n1 +n2
#         n1 = n2
#         n2 = nth
#         count +=1



# def fib_less_than(n):
#     count = 0
#     n1 = 0
#     n2 = 1
#     if n <0:
#         print("sorry ,Enter the postive number")
#     elif n == 1:
#         print("fibo number",n,":")
#     else:
#         les = n-1
#         while count < les:
#             print(n1)
#             nth = n1+n2
#             n1 = n2
#             n2 = nth
#             count += 1

# food_prefernce = {"burger","pizza","prawans"}

# restaurants ={
#     "seafood_cove" : {"prawans","sandwich","fish","crab"},
#     "hungry_jacks" : {"burger","fries","icecream","pizza"},
#     "potting_shed" : {"brocali","carrot","bread","avacado"}
# }

# best_matched_food = set()
# best_matched_restaurants = None

# for restaurants_name ,menu in restaurants.items():
#     commmon_food = food_prefernce.intersection(menu)
#     print(commmon_food)
#     if len(commmon_food) > len(best_matched_food):
#         best_matched_food = commmon_food
#         best_matched_restaurants= restaurants_name
# print(f"The best matched {best_matched_restaurants} with {best_matched_food} matched food ")



# class Monster:

#     def __init__(self,name,hp,attack):
#         self.name = name 
#         self.hp = hp
#         self.attack = attack
#     def fight(self,target):
#         target.hp -= self.attack
#         print(f"{self.name} attached{target.name}for{self.attack}damage!")
#         print(f"{target.name} has {target.hp}HP left")


# centaur = Monster("centaur",100,10)
# goblin = Monster("golbin",80,7)
# centaur.fight(goblin)        
# goblin.fight(centaur)





# course = "python course for beginners"

# print(course.upper())
# print(course.lower())
# print(course.find('c'))
# print(course.replace('python','java'))
# print('python'in course)

# first = 'ajay' 
# last = 'sriram'

# message = f'{first}[{last}] is a develeoper'
# greetings = f'{first}{last} Welcome to the website'

# print(message)
# print(greetings)




# numbers = [222,55,45,6,77,99,2]

# max = numbers[0]

# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# customer = {
#     'name':'aj',
#     'age': 30,
#     'location':{'dallas','london','hyd'},
#     'is_valid': True
# }

# customer['name'] =['sri']
# customer['lastname'] = 'sriram'





# its_hot = True
# its_cold = False

# if its_hot :
#     print(f'hot day' ,[['drink plenty of water']])
# elif its_cold:
#     print(f'its cold day' , [[['drink warm water']]])
# else:
#     print('its normal day')




# i = 5

# while i >= 1 :
#     print('*'* i)
#     i -= 1

# def star_tree():

#     for i in range(5):
#         print(i*'*')  
#     for i in range(5):
#                 print(('*'*(5-i)))

# star_tree()


# class Greet:

#     def greet_user(self,user):
#         print(f'Hello {user} welcome to channel'  )
#         print('Greetings from everyone')
#     def service(self,request):
#         print(f'service on board')
#         print(f'{request} has been placed,required any assistance ring the bell')
    
# wish = Greet()
# wish.greet_user('aj')
# wish.service('coffe')

# numbers = [ 'ajay','aj','sri','aj']

# unique = []

# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique) 


# for i in range(4):
#     for j in range(3):
#         print(f'({i},{j})')




# class lappy:
#     def __init__(self):
#         self.__maxprice =25000
    
#     def sell(self):
#         print(f'selling price of lappy: {self.__maxprice}')

#     def setmaxprice(self,price):
#         self.__maxprice = price

# c = lappy()

# c.__maxprice = 30000
# c.sell()
# c.setmaxprice(30000)
# c.sell()



# class Bulbil:
#     def fly(self):
#         print('Bulbil can fly')
#     def swim(self):
#         print('Bulbil cannot swim')

# class Ostriches:
#     def fly(self):
#         print('ostriches cannot fly')
#     def swim(self):
#         print('ostriches can swim')


# def flying_test(bird):
#     bird.fly()
#     bird.swim()


# bir = Bulbil()

# flying_test(bir)

# ostr = Ostriches()
# flying_test(ostr)



# class Student:
#     def __init__(self,name,lastname):
#         self.name = name 
#         self.lastname = lastname 
#     def show_info(self):
#         print(self.name)
#         print(self.lastname)
#     class Subjects():
#         def __init__(self):
#             pass
#         def subjects(self):
#             self.math = 'math'
#             self.science = 'science'
#             self.social = 'soical'
    
#         def marks(self):
#             self.math_M = 76
#             self.science_M = 78
#             self.social_M = 79
#         def show(self):
#             print(f'subject{self.math} marks{self.math_M}')
#             print(f'subject{self.science} marks{self.science_M}')
#             print(f'subject{self.social} marks{self.social_M}')

# s1 = Student('ajay','s').Subjects()
# s1.show()





# Sec_name = 'aj'
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess_name = input('name:')
#     guess_count += 1
#     if guess_name == Sec_name:
#         print('Correct guess')
#         break
#     else:
#         print('try again')



# command = ""
# started = False

# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started:
#             print("car is already started")
#         else:
#             started = True
#             print("car is started")
#     elif command == "stop":
#         if not started:
#              print("car is alreday been stopped")
#         else:
#             started  = False
#             print("car has been stopped")
#     elif command == "help":
#         print('''start -  start the car
#               stop-to stop the car
#               quit- quite the game ''')
#     elif command == "quit":
#         break
#     else:
#         print('sorry , i dont understand your keywords')


# import random

# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first,second

# dice = Dice()
# print(dice.roll())

# import itertools , random

# deck = list(itertools.product(range(1,14),['spade','heart','diamond','club']))

# random.shuffle(deck)

# print("You got:")

# for i in range(5):
#     print(deck[i][0],"of",deck[i][1])


# import random

# person = ['aj','nani','sriram','ajay']

# guest = random.choice(person)

# print(f'Welcome',{guest})

# from datetime import date

# today = date.today()

# print("current day:",today.day)


# import timeit

# def myfinction():
#     y = 3.1456
#     for x in range(100):
#         y = y ** 0.7
#     return y 

# print(timeit.timeit(myfinction,number=1000000))



# import re

# msz = "The Country is cool"
# x = re.search("is.*cool$",msz)

# if x:
#     print("its matching")
# else:
#     print("not matching")


# number = int(input("Enter the Number:"))
# fact = 1
# if number < 0:
#         print("Enter the larger number")
# elif number == 0:
#         print("Factorial Zero is 1")
# elif number > 0:
#     for i in range(1,number+1):
#         fact = fact*i
#     print("The factorial of",number,"is",fact)


# number = int(input("Enter the number:"))

# for i in range(1,21):
#     fact = i *number
#     print(number,"*",i,"=",fact )



# Msg = "welcome to bank "
# print(Msg)
# start = True

# if start:
#     print("Insert your Debit or Credit card")
#     pin = 1234
#     pincode =input("Enter your pincode:")
#     i = 1
#     while i < 5:
#         if pincode != pin:
#             print("Wrong pincode,try again")
#         elif pincode == pin:
#             print("Choose the amount of money to withdrwal")
# else:
#     print("Hold the debitcard")   


# import time,sys

# user_balance = 100

# trans1 = 'NA'
# trans2 = 'NA'
# trans3 = 'NA'
# trans4 = 'NA'
# trans5 = 'NA'
# trans6 = 'NA'
# trans7 = 'NA'
# trans8 = 'NA'
# trans9 = 'NA'
# trans10 ='NA'

# time.sleep(0.75)
# print('''P.S The code is 1212.
#       Don't use Caps
#       You can only see your previous 10 Transcation ''')
# time.sleep(1)
# print("Welcome to A2Z banking")
# attempts = True

# while attempts == True:
    
#     attempt1 = input("Enter the PIN:")

#     if attempt1 == '1212':

#         print('Correct PIN')
#         time.sleep(1)
#         break
#     else:
#         print("Incorrect PIN")
#         time.sleep(0.75)
#         attempt2 = input('Please enter correct pin:')
#         if attempt2 == '1212':
#             print("correct PIN")
#             break
#         else:
#             print("Incoorect PIN")
#             time.sleep(0.75)
#             print("You have 1 more attempt: " )
#             attempt3 = input("Please enter correct pin")
#             if attempt3 == '1212':
#                 print("Corect PIN")
#                 break
#             else:
#                 print("Incorrect PIN:")
#                 print("wait for 5 mins to try again(or reset code):")
#                 time.sleep(120)
#                 print()

# yes = 0

# valid_option = True
# while valid_option == True:
#     time.sleep(0.75)
#     menu = input('''
# Please Select an option:
# Welcome to A2Z banking.
# 1 - Display  balance
# 2 - withdraw funds
# 3 - Deposite funds
# 4 - Print List of Transcation
# 9 - Return card
                
# ---> : ''')  
#     print()               
#     if menu =="1" :

#         print("Display Balance")
#         print('$',user_balance)
#         print()
#         time.sleep(0.25)
    
#     elif menu == "2":

#         print("Withdraw Funds")
#         time.sleep(0.75)
#         wf = int(input('''
# How Much would you like to withdraw?
# Your option are:
# 10:
# 20:
# 50:
# 100:
# 7 - Other(must be a multiple of 10
# 8 - Return to main menu
# 9- Return card:
# ----> '''))
 
#         if wf == user_balance:
#             print("Congratulation you broke , you now have $0 in your bank account")
#             user_balance = 0
#             never = 'withdraw',wf

#         elif wf > user_balance:
#             print("You dont have much money")
#             never = 0 
#             yes = yes - 1

#         elif wf == 10:
#             print("Successful withdrawn $10,you have",user_balance-10)
#             user_balance  = user_balance-wf
#             never = 'withdraw',wf
#         elif wf == 20:
#              print("Successful withdrawn $20,you have",user_balance-20)
#              user_balance = user_balance-wf
#              never = 'withdraw',wf
#         elif wf == 50:
#             print("Successful withdrawn $50,you have",user_balance-50)
#             user_balance = user_balance-wf
#             never = 'withdraw',wf
#         elif wf == 100:
#             print("Successful withdrawn $100,you have",user_balance-100)
#             user_balance = user_balance-wf
#             never = 'withdraw',wf
#         elif wf == 7:
#             print("Other amount")
#             ea = int(input("How much would like to withdraw ?:"))

#             if ea == user_balance:
#                 print("Congratulations you broke, you now have $0 in your bank account")
#                 user_balance = 0
#                 never = 'withdraw',ea
#             elif ea > user_balance:
#                 print("you don't have that much amount")
#                 never = never
#                 yes = yes - 1
        
#             elif ea %10 == 0 :
#                 print("Succesfully withdrawn $",ea,"you now have $",user_balance)
#                 user_balance = user_balance-ea
#                 never = 'withdraw',ea
#         elif wf == 8:
#             print()
#             never = never
#             yes = yes -1 
#         elif wf == 9:
#             print('Thank you for Banking at A2Z')
#         else:
#             print("Invalid")
#             yes = yes - 1
#             yes = yes + 1

#             if yes >10:
#                 trans1 = trans2
#                 trans2 = trans3
#                 trans3 = trans4
#                 trans4 = trans5
#                 trans5 = trans6
#                 trans6 = trans7
#                 trans7 = trans8
#                 trans8 = trans9
#                 trans9 = trans10
#                 trans10 = never

#             elif yes == 1:
#                 trans1 = never
#             elif yes == 2: 
#                 trans2 = never
#             elif yes == 3:
#                 trans3 = never
#             elif yes == 4:
#                 trans4 = never
#             elif yes == 5: 
#                 trans5 = never
#             elif yes == 6:
#                 trans6 = never
#             elif yes == 7:
#                 trans7 = never
#             elif yes == 8: 
#                 trans8 = never
#             elif yes == 9:
#                 trans9 = never
#             elif yes == 10:
#                 trans10 = never 

#     elif menu == 3 :        
#         print("Deposite Funds")
#         EA = int(input('''                  
# Chose an option:
# 1 - Deposite
# 2 - Return to main menu
# 9 - Return card 
        
# ---> '''))

#         if EA == 1 :
#             dp = int(input("how much would you like to deposite?:"))
#             if dp > 0:
#                 print("Successfully Deposited",dp,"you now have $",user_balance)
#                 user_balance = user_balance + dp
#                 never = 'Deposted',dp
#             elif dp < 0 :
#                 print("you can't use negative number")
#                 never = never
#                 yes = yes - 1
#         elif EA == 2 :
#             print()
#             never = never 
#             yes = yes -1
#         elif EA == 9 :
#             print("Thank you for using A2Z banking:")
#             sys.exit()
        
#             yes = yes+1
#             if yes >10:
#                 trans1 = trans2
#                 trans2 = trans3
#                 trans3 = trans4
#                 trans4 = trans5
#                 trans5 = trans6
#                 trans6 = trans7
#                 trans7 = trans8
#                 trans8 = trans9
#                 trans9 = trans10
#                 trans10 = never
#             elif yes == 1:
#                 trans1 = never
#             elif yes == 2:
#                 trans2 = never
#             elif yes == 3:
#                 trans3 = never
#             elif yes == 4:
#                 trans4 = never
#             elif yes == 5:
#                 trans5 = never
#             elif yes == 6:
#                 trans6= never
#             elif yes == 7:
#                 trans7 = never
#             elif yes == 8:
#                 trans8 = never
#             elif yes == 9:
#                 trans9 = never
#             elif yes == 10:
#                 trans10 = never
#     elif menu == "4":
#         print("Print list of transaction")
#         time.sleep(0.75)
#         print()
#         print(trans1) 
#         print(trans2) 
#         print(trans3) 
#         print(trans4) 
#         print(trans5) 
#         print(trans6) 
#         print(trans7) 
#         print(trans8) 
#         print(trans9)
#         print(trans10)
#     elif menu == "9":
#         print("Thank you for using A2Z banking:")  
#         sys.exit()
#     else:
#         print("Please choose a valid option")











