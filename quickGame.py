import random
print("Random Math Question Generator")
playing = True
score = 0

while playing:
    num1 = round((random.random() * 1000), 0)
    num2 = round((random.random() * 1000), 0)
    ans = num1 + num2

    print(str(num1) + " + " + str(num2))
    userAns = input()

    if userAns == str(ans):
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        playing = False

print("Your streak was " + str(score) + "!")





