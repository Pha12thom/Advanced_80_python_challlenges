counter = 0
pay = 1000
interest = 5
for counter in range(11):
    counter += 1
    topay = pay * interest / 100
    pay += topay
    print(f"Year {counter} is {round(pay,2)}")
