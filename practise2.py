# term = int(input("Enter the term ?:"))
# result = list(map(lambda x: 2**x,range(term)))
# print("The total terms are:",term)
# for i in range(term):
#     print("2raised to power",i,'is',result[i])

# mylist = [12, 65, 54, 39, 102, 339, 221]

# result = list(filter(lambda x : (x %13==0),mylist))
# print("The number divided by 13 are:",result)

# def is_divisible_by_five(n):
#         divi = False
#         if n% 5 == 0:
#             divi =True
#             print(divi)
#         else:
#               print(divi)
# is_divisible_by_five(30)

# dex =34
# print(bin(dec),"binary val")
# print(oct(dec),"oct val")
# print(hex(dec),"hex decimal")

# C = 'p'
# print("The ASIC value of ",C,'is',ord(C))
# print(type(ord(C)))




# def computer_hcf(x,y):

#     if x > y :
#         smaller = y 
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if((x % i == 0)) and ((y % i == 0)):
#             hcf = i 
#     return hcf

# num1 = 54
# num2 = 24

# print("The Hcf is",computer_hcf(num1,num2))



# def lcm(x,y):

#     if x > y :
#         greater = x
#     else:
#         greater = y 

#     while True:
#             if ((greater % x ==0)) and ((greater % y ==0)):
#                 lcm = greater 
#                 break
#             greater += 1
#     return lcm 
    
# num1 = 34
# num2 = 24
# print("The Lcm value is ",lcm(num1,num2))

# def prime_factor(x):
#     print("The factor of ",x,"are:")
#     for i in range(1,x+1):
#         if x % i ==0:
#             print(i)
# num =180
# prime_factor(num)



# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def mul(x,y):
#     return x*y

# def div(x,y):
#     return x/y

# print("Enter your choice:")
# print("1.Add")
# print("2.sub")
# print("3.Multiplication")
# print("4.Divide")

# while True:

#     choice = input("Enter the choice(1/2/3/4):")

#     if choice in ('1','2','3','4'):
#         try:
#             num1 = float(input("Enter first number:"))
#             num2= float(input("Enter second number:"))
#         except ValueError:
#             print("Invalid input,Enter the choice")
#             continue
            
#         if choice =='1':
#             print(num1,'+',num2,'=',add(num1,num2))
#         elif choice == '2':
#             print(num1,'-',num2,sub(num1,num2))
#         elif choice == '3':
#             print(num1,'*',num2,'=',mul(num1,num2))
#         elif choice == '4':
#             print(num1,'/',num2,'=',div(num1,num2))

#         Next_calculation = input("Lets do next calculation (yes/no): ")
#         if Next_calculation == 'no':
#             break
#     else:
#         print('Invalid input')























