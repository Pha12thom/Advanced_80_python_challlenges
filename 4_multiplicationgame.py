multiples = int(input("challenging number: "))
for i in range(1, multiples):
    print("you chose multiples of ", multiples)
    answers = i * multiples
    user_answer = int(input(f"{i} x {multiples} = "))
    if user_answer == answers:

        print("current score  ", i)
        continue
    else:
        print("nope, The answer was ", answers)

        break

print("\nyour total score is ", i, "out of ", multiples)
