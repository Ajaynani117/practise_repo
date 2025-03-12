# class Computer:
    
#     Brand = 'Dell'

#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram 

#     def config(self):
#         print("config is",self.cpu,self.ram)
#     @classmethod
#     def model(cls):
#         print('model is 2024')

    

# com1 = Computer('i5',14)
# com2 = Computer('i7',24)
# print(Computer.Brand)
# print(Computer.model())
# com1.config()
# com2.config()


# class Student:

#     College = 'SVIT'
#     print("college name",College)
#     def __init__(self,name,rollno):
#         self.name = name 
#         self.rollno = rollno

#     def branch(self):
#         self.branch = 'CSE'
#         print(self.branch)
#     def section(self):
#         self.section = 'B'
#         print(self.section)

#     def show(self):
#         print(self.name,self.rollno)

# s1 = Student('aj',12345)
# s2 = Student('sriram',9876)
# s1.show()

# flag = False
# number = int(input("enter the number:"))

# if number < 0 and number == 0:
#     print('Number is not prime')
# elif number > 1:

#     for num in range(2,number):
#         if  number % num ==0 :
#             flag = True
#             break
# if flag:
#     print(flag)
#     print('Number is not prime')
# else:
#     print(flag)
#     print('Number is prime')


# number = int(input("enter the number:"))

# fact = 1

# if number <0:
#     print("Enter the rightfully number")
# elif number ==0:
#     print("Factorial of 0 is 1")
# else:
#     for num in range(1,number+1):
#         fact = fact*num
#     print("Factorial of given number",number,'is',fact)


#Fib0nacci sloution 
# num =int(input("Enter the number:"))

# n1,n2 = 0,1
# count = 0

# if num <=0:
#     print("Enter the postive number:")
# elif num ==1:
#     print("Fibonacci sequence of",num,':')
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < num :
#             print (n1) 
#             nth = n1 + n2
#         #update the value
#             n1 = n2
#             n2 = nth
#             count += 1

# num = int(input("Enter the number:"))

# sum = 0

# temp = num 

# while temp > 0:
#     digit = temp%10
#     sum += digit**3
#     temp //=10
# if num == sum:
#     print("Its a Armstrong number")
# else:
#     print("Its not a Armstrong number")

# def sum_of_digits(n):

#     digit = str(n)
#     sum = 0
#     for num in digit:
#         for i in num:
#             sum += int(num)
#     print("sum of total:",sum)
             
# sum_of_digits(12345)



# lower = 10
# upper = 200

# for num in range(lower,upper+1):
#     order = len(str(num))
#     sum = 0 
#     temp  = num 
#     while temp >0:
#         digit = temp%10
#         sum += digit **order
#         temp//=10
#     if num ==sum :
#         print(num)


# def sum_of_naturals(n):
#     sum = n*(n+1)/2
#     print(sum)
# sum_of_naturals(10)

# num = int(input("enter the number:"))

# if num <0 :
#     print("Enter the rightfull number")
# else:
#     sum = 0
#     while num > 0:
#         sum+= num
#         num -= 1
#     print("sum is",sum)



# import itertools,random

# deck = list(itertools.product(range(1,14),['spade','Heart','Diamond','Club']))

# random.shuffle(deck)

# print("you got :")

# for i in range(5):
#     print(deck[i][0],'of',deck[i][1])

# import calendar
# yy = 2024
# mm = 11
# print(calendar.month(yy,mm))


# def recur_finbo(n):
#     if n<=1:
#         return n
#     else:
#         return(recur_finbo(n-1)+recur_finbo(n-2))
# nterms = 10
# if nterms<=0:
#     print("Enter the postive integers")
# else:
#     print("Fibonacci sequence")
# for i in range(nterms):
#     print(recur_finbo(i))


# signal = input("Signal colour:")

# if signal == 'Red':
#     print("Stop")
# elif signal == 'Green':
#     print("Go")
# elif signal == 'Yellow':
#     print("Look")
# else:
#     print('Light is broken')


# marks = int(input("marks:"))

# if marks >= 90:
#     print("A")
# elif marks >= 80 and marks < 90:
#     print("B")
# elif marks >=70 and marks < 80:
#     print("C")
# else:
#     print("D")


# food = input("Enter the food :")

# print("Sweet") if food == "cake" or food =='jalebi' else print("notSweet")

# age = int(input("Enter your age:"))
# vote = ("yes","no")[age <=18]
# print(vote)


# Entry = input("Enter the :")
# Code = "IN"
# gate = ("yes","no")[Entry != Code]
# print(gate)


# side = int(input("Enter the side:"))

# area = side * side

# print("area:",area)


# num1 = float(input("Enter the num1:"))
# num2 = float(input("Enter the num2:"))

# avg = (num1+num2)/2
# print(avg)


# a = int(input("Enter the number:"))
# b = int(input("Enter the number2:"))

# print(a >= b)

# first_name = input("Enter the name:")
# print(len(first_name))

# str ="StringS"
# print(str.count("S"))



# num = int(input("enter the number:"))

# if num %2 ==1 :
#     print("odd")
# else:
#     print("even")

# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))
# num3 = int(input("Enter the num3:"))

# if num1 >= num2 and num1 >= num3:
#     print("greater is:",num1)
# elif num2 >= num3:
#     print("Greateris:",num2)
# else:
#     print("Greater is:",num3)



# num = int(input("Enter the number:"))

# if num % 7 ==0:
#     print("Its multiple  ")
# else:
#     print("Its not multiple of 7")


# movies=[]
# movies.append(input("Enter the fav movie name:"))
# movies.append (input("Enter the fav movie name:"))
# movies.append(input("Enter the fav movie name:"))

# print(movies)


# num1 = int(input("Enter gatecode:"))
# gatecode =1422
# entry = ("Invalid gatecode","Entry access")[num1 == gatecode]
# print(entry)



# lst1 = [1,2,1]
# lst2 =[1,2,3]
# copy_lst1 = lst1.copy()
# copy_lst1.reverse()

# if copy_lst1 == lst1:
#     print("palindrome")
# else:
#     print("not palindrome")



# lst1 = [1,2,1]
# lst2 =[1,2,3]
# copy_lst1 = lst1.copy()
# copy_lst1.reverse()
# check = ("not palindrome","palindrome")[lst1 == copy_lst1]
# print(check)



# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))

# lst = ["C","D","A","A","B","B","A"]
# lst.sort()
# print(lst)



# dict = {
#     "Name":"Ajay",
#     "Surname":"Sriram",
#     "age":30,
#     "Location":{2017:"India",2018:"UK",2023:"US"}
    
# }
# dict.update({'lang':'eng'})
# dict.popitem()
# print(dict)


# collection = {1,2,3,4,5,6}
# collec = {1,9,5,4,3,8}
# collection.discard(7)
# print(collection.union(collec))
# print(collection.intersection(collec))
# collection.difference(collec)
# print(collection.intersection(collec))
# print(collec)




# names = {
#     "table":["a piece of furniture","list of facts and figures"],
#     "cat":"a small animal"
# }
# print(names)


# subject = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# student_class = len(subject)
# print("Classroom needed by all students are:",student_class)



# subject ={}
# x = int(input("Enter marks:"))
# subject.update({'phys':x})
# x = int(input("Enter marks:"))
# subject.update({'chem':x})
# x = int(input("Enter marks:"))
# subject.update({"math":x})
# print([subject])


# val = {("float",9.0),("int",9)}
# print((val))

# count = 100

# while count >=1:
#     print(count)
#     count-=1


# count = 1
# cha = 2
# while count <= 10:
#     print("2","*",count,"=",count*2)
#     count += 1

# lst = [1,4,9,16,25,36,49,64,81,100]

# idx = 0 
 
# while idx < len(lst):
#     print(lst[idx])
#     idx += 1


# tup = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("Search the given number:"))

# y = len(tup)
# for i in tup:
#     if x == i:
#         print("Given number is found",x)
#         break
# else:
#     print("Invalid entry ,Please try again")


# nums = (1,4,9,16,25,36,49,64,81,100)


# x = int(input("Enter the number:"))

# i = 0 

# while i < len(nums):
#     if nums[i] == x:
#         print("found at index",i)
#         break
#     i+=1
# else:
#     print("Invalid entry,Please try again")






# nums =[1,4,9,16,25,36,49,64,81,100]

# for i in nums:
#     print(i)

# tup =(1,4,9,16,25,36,49,64,81,100)

# x = int(input("Search the number:"))

# idx = 0 
# for i in tup:
#     if i==x:
#         print("Found the number at idx",idx)
#         break
#     idx +=1
# else:
#     print("Invalid entry")


# n = int(input("Enter the number:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
    



# n = int(input("Enter the number:"))

# sum = 0 
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# num = int(input("Enter the number :"))

# sum = 0 

# i = 1
# while i <=num:
#     sum+=i
#     i+=1
# print(sum)



# n = int(input("Enter the number:"))

# fact = 1

# for i in range(1,n+1):
#     fact *= i
# print(fact)



# givennumber =129475
# num = str(givennumber)
# sum =0
# for i in num:
#      sum += 1
# print(sum)



# giving ="madam"

# copylst = ""

# for i in giving:
#     copylst = i+copylst
# if giving == copylst:
#     print("Its palindrome")
# else:
#     print("Its not palindrome")




# given_string =input("Enter the string:")

# reverse_string = ""

# for i in given_string:
#     reverse_string = i+reverse_string
# print(reverse_string)




# month = ["January","April","November"]

# for i in month:
#     if i== "Februray":
#         print("Feb month as 28 days")
#     elif i in ("April","June","September","November"):
#         print("Month of",i,"as 30 days")
#     elif i in ("January","March","May","July","August","octaber","December"):
#         print("Month of",i,"as 31days")
#     else:
#         print("Invalid entry")
        

# password = input("Enter the password:")

# had_length_password = False
# had_upper_case = False
# had_lower_case = False
# had_Special_charcater =False
# had_digits = False

# if len(password)>=5 and len(password)<=16:
#     had_length_password = True

# for i in password:
#     if (i.islower()):
#         had_lower_case = True
#     if (i.isupper()):
#         had_upper_case = True
#     if (i.isdigit()):
#         had_digits =True
#     if(i=="@" or i=="$" or i=="_"or i=="#" or i=="^" or i=="&" or i=="*"):
#         had_Special_charcater=True

     
# if (had_length_password==True and had_lower_case ==True and had_upper_case == True and had_digits == True and had_Special_charcater == True):
#     print("Valid Password")
# else:
#     print("Invalid Password")



# def String_output(x):

#     if len(x)%2==0:
#         print("its even string")
#     else:
#         print("Its odd string")

# String_output("ajay")
# String_output("Srirams")





# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):

#     if n==0 or n==1:
#         return 1
#     else:
#         return n *fact(n-1)

# show = fact(5)
# print(show)




# def natural_num(val):
#     sum = 0
#     for i in range(1,val+1):
#         sum += i
#     print(sum)
# natural_num(5)    
# natural_num(10)




# def natural_num(val):
#     if val == 0:
#         return 0
#     return natural_num(val-1) + val



# def recu_num(n):
#     if n == 1:
#         return n
#     else:
#         return n*recu_num(n-1)

# out = recu_num(5)
# print(out)


# def convert_decimal(n):

#     if n > 1 :
#         convert_decimal(n//2)
#         print(n%2,end="")

# convert_decimal(34)


# x = [[12,7,3],
#      [4,5,6],
#      [7,8,9]]
# y = [[5,8,1],
#      [6,7,3],
#      [4,5,9]]

# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
# for r in result:
#     print(r)



# x =[[12,7],
#     [4,5],
#     [3,8]]
# result = [[0,0,0],
#           [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i] = x[i][j]

# for r in result:
#     print(r)



# x = [[12,7,3],
#       [4,5,6],
#       [7,8,9]]
# y = [[5,8,1],
#       [6,7,3],
#       [4,5,9]]

# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] * y[i][j]

# for r in result:
#     print(r)



# x = [[12,7,3],
#      [4,5,6],
#      [7,8,9]]
# y = [[5,8,1,2],
#      [6,7,3,0],
#      [4,5,9,1]]

# result =[[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0],
#          ]

# for i in range(len(x)):
#     for j in range(len(y[0])):
#         for k in range(len(y)):
#             result[i][j] += x[i][k] * y[k][j]

# for r in result:
#     print(r)


# val = "dad"
# val = val.casefold()
# rev_val = reversed(val)

# if list(val)==list(rev_val):
#     print("The string palindrome")
# else:
#     print("The string not palindrome")


# punctuations = '''!P()-[]{};:'"\,<>./?@~#$%'''

# mystring = "Hello!!!, he said --- and went."


# no_punctuations = ""

# for char in mystring:
#     if char  not in punctuations:
#         no_punctuations = no_punctuations + char
# print(no_punctuations)

# my_string = input("Enter the string:")

# words = [word.lower()for word in my_string.split()]

# words.sort()
# print("Sorted words are:")

# for word in words:
#     print(word)

# E = {0,2,4,6,8}
# N = {1,2,3,4,5}

# print("Union of E and N is",E|N)
# print("Intersection of E and N is",E&N)
# print("Difference of E and N is",E-N)
# print("Symmetric difference of E and N is,",E^N)





# vowels ="aeious"
# ip_str = 'Hello ,have you tried our tutorial section yet'

# ip_str = ip_str.casefold()

# count = {}.fromkeys(vowels,0)

# for char in ip_str:
#     if char in count:
#         count[char] +=1
# print(count)


# my_list =[ [1],[2,3],[4,5,6,7],[8,9,10,11]]

# flat_list = [num for sublist in my_list for num in sublist]
# print(flat_list)

# my_list = [1,2,3,4,5]
# print(my_list[:-1])



# fruits ={
#     "apple":"red",
#     "grapes":"green"
# }
# for keys,value in fruits.items():
#         print(keys,value)


# cities = {"us":"dallas","india":"Delhi","Uk":"London"}

# sorted_val = {key: value for key,value in sorted(cities.items(),key = lambda item:item[1])}

# print(sorted_val)





# punctuations = '''!%&*()-{}[]'#\/@~?$£'''

# my_string = "Hello Aj!!!!, your ----- welcome "
# no_punctuations = ""

# for char in my_string:
#     if char not in punctuations:
#         no_punctuations = no_punctuations+char
# print(no_punctuations)



# if __name__ == '__main__':

#     x = int(input("Enter the val:"))
#     y = int(input("Enter the val:"))
#     z = int(input("Enter the val:"))
#     N = int(input("Enter the val:"))

#     print(list([[i,j,k]for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)  if x+y+z !=N]))

    

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))





# if __name__ == '__main__':
#     n = int(input())
#     list1 = []
#     list2 = []        

#     for i in range(0,n):
#         name = input()
#         score = float(input())
#         list1.append([name,score])
#         list2.append(score)
# list1.sort()
# list2.sort()
# m = min(list2)
# list2.remove(m)
# m2 = min(list2)

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if list1[i][j] == m2:
#             print(list1[i][0])




























































