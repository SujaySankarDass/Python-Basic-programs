for i in range(1,101):
    if i%9==0 and i != 9:
        break
    elif i%4==0:
        continue
    else:
        print(i)
