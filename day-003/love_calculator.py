print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
score1 = 0
score2 = 0
names = name1.lower() + name2.lower()
score1 += names.count("t")
score1 += names.count("r")
score1 += names.count("u")
score1 += names.count("e")
score2 += names.count("l")
score2 += names.count("o")
score2 += names.count("v")
score2 += names.count("e")
love_score = int(str(score1) + str(score2))
if love_score < 10 or love_score > 90:
 print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score <50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
