i = 0
pay = 1000
interest = 5
for i in range(11):
    i ++1
    topay = pay * interest / 100
    pay += topay
    print(f"Year {i} is {round(pay,2)}")
