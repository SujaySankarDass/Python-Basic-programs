#while loop learning

#1
i = 1
while i <= 10:
    print(i)
    i += 1

#2
i = 10
while i >= 1:
    print(i)
    i -= 1

#3    
i = 1
while i <= 10:
    
    if i%2==0:
        print(i)
    i += 1

#4
i=10
while(i<=200):
    print(i,end=",")
    i=i+10

#5
n = int(input("Enter number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print(total)





