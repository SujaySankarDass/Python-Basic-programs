#Q1
for i in range(1, 31):
    if i%5==0:
        continue
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")

#Q2

count3=0
count7=0

for i in range(1, 51):
    if i%3==0:
        count3 +=1  
    if i%7==0:
        count7 +=1

print("div by 3",count3)
print("div by 7",count7)


#Q3


i=int(input("Enter num:"))

if i>0:
    print("Num is positive")
elif i<0:
    print("Num is Negative")
else:
    print("Its Zero")


#Q4

n=int(input("Number:"))

for i in range(1, n+1):
    if i%4==0 and i%6==0:
        print(i,"FourSix")
    elif i%4==0:
        print(i,"Four")
    elif i%6==0:
        print(i,"Six")
    


