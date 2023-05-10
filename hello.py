# print("Hello world")
# print("Placement course")
# print("Imp to all Btech students")
# print("Venkata")

# a = 100
# b = 200
# c = a + b
# print(c)

# a = 10
# b = 2.3
# c = "KVSR"
# d = True
# e = 3+7j

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# type conversion

# num = '50'
# num1 = int(num)
# print(num1)
# print(type(num1))

# num1 = 50
# num2 = 80

# if num1<num2:
#     print("num1 is less than num2")
# elif num1==num2:
#     print("num1 is equal to num2")
# else:
#     print("num1 is greater than num2")

# L = [1,2.2,"abc",True,3+4j]
# print(L)

# L.append(1)
# print(L)

# L.extend([1,4,7,8])
# print(L)

# L.insert(1,"python")
# print(L)

# print(L.count(1))

# for i in range(1,10):
#     print(i)

# for i in 'KVSR':
#     print(i)

# L = [1,2,3,4,5]

# for i in L:
#     print(i)

# L = [1,2,3,4,5]
# sum = 0

# for i in L:                // sum of 5 numbers by using while-loop
#     sum = sum + i
# print(sum)

# for i in range(1,10,2):
#     print(i)

# mobiles = ['vivo' , 'Iphone' , 'oneplus' , 'mi' , 'realme']

# for i in mobiles:
#     if i=='vivo':
#         print("This is vivo mobile")
#     else:
#         print("This is not vivo mobile")

# while True:
#     print("This is while")

# k = 0
# while k<10:
#     k = k+1
#     print("k value is",k)
# else:
#     print("This is else")

# T = ()
# print(type(T))
# print(T)

# T = (1,2,3,4,5,"KVSR",True)
# print(T)
# print(T[3])

#repeatations
# print(T*2)

#concatenation
# a = (4,10,44,55)
# print(T+a)

#Iterations
# for i in T:
#     print(7 in T)

# b = (1,2,3,4,5)
# print(min(b))
# print(max(b))
# print(sum(b))
# print(sorted(b))
# print(len(b))

# for val in "LAPTOP":
#     if val == "P":
#         break                      // break statement
#     print(val)
# print("The end")

# for val in "LAPTOP":
#     if val == "P":
#         continue                      #continue statement
#     print(val)
# print("The end")


# string
# s = 'KVSR'
# s1 = "python's life"
# s2 = '''
#      This is python
#      This is java
#      '''
# print(s)
# print(s1)
# print(s2)
# print(type(s))

# S = "Unna patha sericha"
# print(S[0])
# h = S.split()
# print(h)
# print(S.upper())
# print(S.lower())
# print(S.split())
# print(S.strip())
# print(S.startswith())
# print(S.endswith())
# print(S.replace())
# print(S.find())
# print(S.count())
# print(S.format())


# sets:

# D = {1,2,3,3,5,6,10,10,100,1000}
# print(type(D))
# print(D)

# s = {1,2.2,3.08,'KVSR'}
# s.add('python')
# s.update([1,2,3,4,5])
# s.remove(1)
# print(len(s))
# print(s)

#operations
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))

# dictionary

# s = {'name':'KVSR' , 'age':[20]}
# print(type(s))
# print(s)
# print(s['name'])
# print(s['age'])

# s.pop('name')
# s.update({'address':'Gurazala'})
# s.clear()
# print(s)

# Functions

# print(s.keys())
# print(s.values())

# Functions

# def KVSR():
#     print("This is function")
# KVSR()

# def add(a,b):
#     return a+b        // we can perform any operations
# print(add(1,2))

# orbertaory parameter

# def s(a):
#     return(a)
# print(s(1))

# def s(*a):
#     return(a)
# print(s(1,2,3,4,5,6,7,8,9,10))

# keyword parameter

# def s(**a):
#     return(a)
# print(s(name='KVSR',age=20))

# def Kvsr(a):
#     for i in a:
#         print(i)
# Kvsr([1,2,3,4,5,6,7,8,9,10])