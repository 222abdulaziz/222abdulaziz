import random 


# STRINGS
# s = "python"
# n_str = str(123456)
# print(type(n_str))  # str
# print(len(s))  # 6
# print(type(len(s)))  # int


# """""" >> doc string


# def test():
    # """This is simple function"""
    # return True


# print(test.__doc__)  # This is simple function

# long_str = """\tTo create a link, \n enclose the link text in brackets \
#     (e.g., [Duck Duck Go])\U0001f600  and then follow it \
#     immediately with the URL in \U0001f600 parentheses (e.g.,\
#         \U0001f600 (https://duckduckgo.com))."""
# print(long_str)

# s = "python"  # index range [0,5]
# print(s[0])  # p
# print(s[10])  # IndexError: string index out of range
# String Slice [start:end]
# a = s[2:]  # 2 index dan to oxiriga qadar qirqish | thon
# a = s[:2]  # 2 index dan to oxiriga qadar qirqish | py
# c = s[1:-2]  # yth
# b = s[-4:-1]  # tho
# z = s[-5::]  # nohtyp
# print(a)
# Formatting strings

# a = input("soz kirit >>")
# for i in range(len(a)):
#     if a[i] == "a":
#         print(a[::-1])
#     else:
#         print("a harfi bor soz kirit")
   



# s = input()
# for i in range(len(s)):
#     if s[i] == "a":
#         print("OK")
# for i in range(10):
#     print(-i**2, end="")
# else:
#     print(" !!! For tugadi")

# 
# s = "Python is %s pl" % "slow"
# print(s)  # Python is slow pl
# s2 = "Python is {} pl".format("fast")
# print(s2)  # Python is fast pl
# super_fast = "super fast"
# s3 = f"Python is {super_fast} pl"
# print(s3)  # Python is super fast pl

#  STRING METHODS
# s = " Python "
# print(len(s))  # 8
# strip - qator boshida va oxiridagi probellarni ochiradi
# print(len(s.strip()))  # 6
# print(len(s.rstrip()))  # 7
# print(len(s.lstrip()))  # 7

# split - siz korsatgan belgi boyicha str ni elementlarga ajratadi (massiv qiladi)
# long_str = "python*js*cpp*html"
# print(long_str.split("*"))  # ['python', 'js', 'cpp', 'html']
# print(long_str.rsplit("*"))  # ['python', 'js', 'cpp', 'html']

# long_str = "python ok \n js ok \n cpp ok"
# splitlines - str ni qatorlar boyicha ajratadi
# print(long_str.splitlines())  # ['python ok ', ' js ok ', ' cpp ok']

# join - massivni str qiladi
# print("".join(long_str.splitlines()).split("\n"))
# ['python ok js ok cpp ok']

# s = "python"
# print("python is better".title())  # Python Is Better
# print(s.upper())  # PYTHON
# print(s.lower())  # python
# print("python is better".capitalize())  # Python is better

# print(chr(1))  # bu raqam qabul qiladi va ascii boyicha belgini qaytaradi
# print(ord("a"))  # bu belgini qabul qiladi va ascii boyicha tartib raqamini qaytaradi
# s = "python"
# long_str = "split - siz korsatgan belgi boyicha str ni elementlarga ajratadi"
# # siz korsatgan matnni boshlanish index ini qaytaradi
# print(long_str.find("siz"))  # 8
# print(long_str.find("text"))  # -1
# print(long_str.rfind("str"))  # 36
# print(s.index("h"))  # 3
# print(s.rindex("l"))  # ValueError
# aks holda -1 qayataradi


# s = "A byte of python"
# ru_text = "???????????? ?????????? ?????? ???????????? ?????????????????? ??????????????????????."
# ['bg', 'el', 'hy', 'ka', 'l1', 'mk', 'mn', 'ru', 'sr', 'uk']

# print(translit(s, "ru"))  # ?? ???????? ???? ????????????
# print(translit(ru_text, "mn"))  # ?? ???????? ???? ????????????
# print(s.count("o"))  # 2 | elementni str dagi sonini qaytaradi

# print(s.startswith("A"))  # True
# print(s.startswith("a"))  # False
# print(s.startswith("a".lower()))  # Every OK

##########
# print(s.endswith("on"))  # True
# print(s.endswith("of"))  # False

########
# print(s.replace("python", "javascript"))

########
# print("abc123".isalnum())  # True | harf yoki osnlar
# print("abc123".isalpha())  # False | faqat harflar
# print("123".isdigit())  # True | faqat butun sonlar
# print("123".isdecimal())  # True | faqat  sonlar
# print("123".isnumeric())  # True | faqat butun, kasr, rim , qoldiqli sonlar
# print("str".isupper())  # False
# print("str".islower())  # True
# print("str".istitle())  # True


# task 1
# input: user son kiritadi agar  son - da bolmasa  yoki 0 ga teng bomasa
# sonlarni yigindisini hisoblang
# while orqali toxtovsiz son kiritiladi agar "stop" deb kiritlsa sikl toxtedi va sonlar
# yigindisi ekranga chiqadi

# task 2
# input : userdan str qabul qilinadi | masalan "python"
# output: "pyThON" | random belgilar katta harfda random belgilar kichik
# user = input()
# result = ""
# for i in range(len(user)):
#     r = random.randint(0, len(user) // 2)
#     if r % 2 == 0:
#         result += user[i].upper()
#     else:
#         result += user[i]
# print(result)

# y = s.endswith("-")
# b = 0
# c = True
# while c:
#     a = input("")
#     if a == "0":
#         c = False
#         print("nol bolmasin")
#     elif a == b:
#         c = False
#         print("butun son kirit")
#     elif a == y:
#         c = False
#         print("minus bolmasin")
#     elif a == "stop":
#         c = False
#         print(b)
#     else:
#         b=b+ int(a)

# t = True
# b =0
# while t:
#     a= input("")
#     if a[0] == "-" or a =="0" or a== "stop":
#         print(b)
#         break
#     else:
#         b = b + int(a)

# user =input()
# for i in range(0, random.randint(0, len(user))):
#     print(i)


# user = input()
# result = ""
# for i in range(len(user)):
#     r = random.randint(0, len(user)//2)
#     if r % 2 == 0:
#         result += user[i].upper()
#     else:
#         result += user[i]
# print(result)

# 1
# a=int(input(""))
# b=int(input(""))
# c = 0
# while True:
#     if a >= b:
#         c += 1
#     else: 
#         break
# print(c)

# 2
# a = int(input(" .> "))
# b = int(input(" .> "))
# c = 0
# while True:
#     if a >= b:
#         a-=b
#         c+=1
#     else:
#         break
#     print(c)


# 3
# a=int(input(" "))
# b=int(input(" "))
# d = 0
# c =0
# while True:
#     if a>b:
#         a-=b
#         d+=b
#         c+=1
#     else:
#         break
# print(a)

# 4
# n = int(input("son kirit >> "))
# while True:
#     if n == 18:
#         print("darajasi")
#         break
#     else:     
#         print("darajasi emas !!!")
#         break
 
#  5
# n = 2
# while True: 
#     print(n**2)
#     break
   
# # 6 
# n = 10
# a =n
# b=1
# while True:
#     a = a - 2
#     b=b*a
#     if a == 2 or a==1:
#         print(n*b)
#         break

# # 7
# n =10
# x = 0
# while True:
#     x+=1
#     if x**2>n:
#         print(x)
#         break

# 8
# x = int(input(">> "))
# y = 0 
# while True:
#     y = y + 1
#     if y ** 2 > x:
#         print(y - 1)
#         break

# # 9
# n = 10
# k = 0
# while True :
#     k = k + 1
#     if 3 ** k > n:
#         print(k)
#         break
       
# 10
# n = 28
# k = 0
# while True:
#     k = k + 1
#     if 3 ** k > n:
#         print(k+1)
#         break


# 11
# n = 20
# a = 0
# b = 0
# while True:
#     a = a + 1
#     b = b + a
#     if b >= n:
#         print(f"yigindi {b}  oxirgi {a}")
#         break

# 12
# n = 56
# k = 0
# s = 0
# while n >= s:
#     k += 1
#     s += k
# print(k - 1)






