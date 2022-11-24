Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = 1
while num <= 10:
    print(num , end="")
    num += 1

    
12345678910
for i in range(1,6):
    for j in range(1,i+1):
        print(j , end=" ")
    print()

    
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
num = int(input("Enter any number : "))
Enter any number : 
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    num = int(input("Enter any number : "))
ValueError: invalid literal for int() with base 10: ''
num = int(input("Enter any number : "))
Enter any number : 0
ans = 0
for i  in range(1,num+1):
    ans += i

    
print(ans)
0






num = int(input("Enter ant number : "))
Enter ant number : 0
for i in range(1,11):
    print(num,"*",i,"=",num*1)

    
0 * 1 = 0
0 * 2 = 0
0 * 3 = 0
0 * 4 = 0
0 * 5 = 0
0 * 6 = 0
0 * 7 = 0
0 * 8 = 0
0 * 9 = 0
0 * 10 = 0
num = [10,45,78,502,352,121,251]
for i in num:
    if i%5==0:
        if i>500:
            break
        elif i>150:
            continue
        else:
            print(i)

            
10
45
num = int(input("enter any number : "))
enter any number : 
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    num = int(input("enter any number : "))
ValueError: invalid literal for int() with base 10: ''
num = int(input("enter any number : "))
enter any number : 0
chk = 0
while num>0:
    num = int(num/10)
    chk += 1

    
print(chk)
0
num = int(input("enter any number : "))
enter any number : 0
chk = 0
while num>0:
    num = int(num/10)
    chk += 1


print(chk)
SyntaxError: multiple statements found while compiling a single statement

















































for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
        print()

        
5
4
3
2
1
4
3
2
1
3
2
1
2
1
1
lst = [10,20,30,40,50,]

for i in  range(5,0,-1):
    print(lst[i-1])

    
50
40
30
20
10
for i in range(-10,0):
    print(i)

    
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
for i in range(1,4):
    print(i)
    else:
        
SyntaxError: invalid syntax
for i in range(1,4):
    print(i)
else:
    print("done")

    
1
2
3
done
for i in range(4,5)
SyntaxError: expected ':'
for i in range(4,5):
    print(i)

    
4
start = int(input("Enter starting value : "))
Enter starting value : 0
end = int(input("enter ending value : "))
enter ending value : 0
for n in range(start,end+1):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            print(n)

            


start = int(input("Enter starting value : "))
Enter starting value : 
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    start = int(input("Enter starting value : "))
ValueError: invalid literal for int() with base 10: ''


f = 0
s = 1

for i in range(1,11):
    print(f,end=" ")
    ans = f + s
    f = s
    s = ans

    
0 1 1 2 3 5 8 13 21 34 
num = int(input("Enter Number : "))
Enter Number : 
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    num = int(input("Enter Number : "))
ValueError: invalid literal for int() with base 10: ''

num = int(input("Enter Number : "))
Enter Number : 0
ans = 1
for i in range(num,0,-1):
    ans *= i
else:
    print("Factorial of",num,"is",ans)

    
Factorial of 0 is 1
num = int(import("enter number : "))
SyntaxError: invalid syntax
num = int(input("enter number : "))
enter number : 1
ans = 0
while num>0:
    1 = int(num%10)
    
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
num = int(input("enter number : "))
enter number : 1
ans = 0:
    
SyntaxError: invalid syntax
num = int(input("enter number : "))
enter number : 1
ans = 0
while num>0:
    l = int(num%10)
    num = int(num/10)
    ans = (ans*10) + 1

    
print(ans)
1
while num>0:
    l = int(num%10)
    num = int(num/10)
    ans = (ans*10) + 1

    




my_list = [10,20,30,40,50,60,70,80,90,100]

fo i in range(1,11):
    
SyntaxError: invalid syntax
my_list = [10,20,30,40,50,60,70,80,90,100]

for i in range(1,11):
    
SyntaxError: multiple statements found while compiling a single statement
my_list = [10,20,30,40,50,60,70,80,90,100]

for i in range(1,11):
    if i%2==0:
        print(my_list[i-1],end=" ")

        
20 40 60 80 100 
num =int(input("Enter Number : "))
Enter Number : 
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    num =int(input("Enter Number : "))
ValueError: invalid literal for int() with base 10: ''
num =int(input("Enter Number : "))
Enter Number : 1
for i in range(1,num+1):
    print(i*i*i,end=" ")
    