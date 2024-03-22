counter = 0
while True:
    blank = input("Never going to ______ you up.")
    counter += 1
    if blank == "give":
        break
    else:
        print("Nope, Try again")
        continue
print("well done! It only took you", counter, "attempt")
