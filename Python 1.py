i=int(input("Enter your number:"))
if i%3==0 and i%5==0:
    print("Divisible by 3&5")

elif i%3==0:
    print("Divisible by 3")
elif i%5==0:
    print("Divisible by 5")
else:
    print(i)
