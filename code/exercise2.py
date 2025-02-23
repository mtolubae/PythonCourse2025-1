#16.02.2025 Решаем задачи

#Задача 1

# vozrast = int(input("Введите возраст "))
# bilet = 0
# if(5 <= vozrast <=18):
#     bilet = 2
# elif(18 < vozrast <=60):
#     bilet = 5
# elif(vozrast >60):
#     bilet = 3
# else:
#     bilet =0

# print("Ваш билет стоит ", bilet, "$.")

#Exercise 2
# str = input("Введите membership уровень и сумму товаров ")
# membership, summa = str.split()
# summa = float(summa)
# if(membership == "Gold"):
#     summa = summa*0.8
#     #summa = summa - summa*0.2
# elif(membership == "Silver"):
#     summa = summa*0.9
# elif(membership == "Bronze"):
#     summa *=0.95
# else:
#     print("Sorry. No discount for you")

# print("Summa so skidkoy=",summa)

#Exercise 3
# str = input("Введите свой вес и рост ")
# ves, rost = str.split(",")
# ves = float(ves)
# rost = float(rost)
# bmi = ves/(rost*rost)
# if(0<= bmi < 18.5):
#     print("You are underweight. Go eat some burgers")
# elif(18.5 <= bmi <=24.9):
#     print("You weight is normal.")
# elif (25 <= bmi <=29.9):
#     print("You are overweight")
# else:
#     print("You are obese!!!")

#Exercise 4
# dni = int(input("На сколько дней взяли машину на прокат "))
# if(dni < 7):
#     print("Ваша оплата ",dni*40)
# else:
#     print("Ваша оплата ", dni*40 - 50)


#Exercise 5
# def c2f(celc):
#     f = celc * 1.8 + 32
#     #print(celc,"Celcius = ", f," Farenheit")
#     return f
# f = c2f(30)
# print(f)

# print(c2f(40))

#Exercise 6
# def daysLeftTillNY(day, month):
#     days = (month-1)*30 + day
#     daysLeft = 360 - days
#     return daysLeft

# str = input("Введите день и месяц ")
# den, mesyats = str.split()
# den = int(den)
# mesyats = int(mesyats)
# print(daysLeftTillNY(den, mesyats), " дней осталось до НГ")

#Exercise 7
# def findSmallestandLargest(a,b):
#     if(a<b):
#         print(a, "menshee chislo ")
#         return a,b
#     else:
#         print(b, "menshee chislo ")
#         return b,a

# nums = input("Введите 2 числа ")
# a,b = nums.split()
# a = int(a)
# b = int(b)

# small, large = findSmallestandLargest(a,b)
# print("Naimenshee chislo ",small, ". Naibolshee chislo ",large)

#exercise 8
d = {"emil":50, "eleonora": 18, "iskender":17}
# str = input("Введите имя для поиска ")

# def find(d,str):
#     if(str in d):
#         return d[str]
#     else:
#         print("Netu takogo usera")

#print(find(d,str))
# str = input("Введите нового юзера и возраст ")
# user, vozrast = str.split(",")

def addUser(d,user, vozrast):
    if(user in d):
        print("User exists")
    else:
        d[user]=vozrast
        print("User added")

#addUser(d,user,vozrast)
#print(d)

def changeUser(d, user, vozrast):
    if(user in d):
        d[user] = vozrast

#str = input("Введите юзера, возраст и функцию")
#user, vozrast, task = str.split(",")

user, vozrast, task = input("Введите юзера, возраст и функцию ").split(",")
if(task == "add"):
    addUser(d, user, vozrast)
elif(task == "change"):
    changeUser(d, user, vozrast)
else:
    print("Task not found")

print(d)