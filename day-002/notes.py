import datetime

# math
print(2 ** 3) # exponent :: 8

# py follows pemdas, left to right

print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

# round numbers

print(8/3) # 2.6666666666666665
print(round(8/3)) # rounds it to a whole number, from 2.66..... now to 3

print(round(8/3, 2)) # round it to 2 decimal places: 2.67

# shorthand

score = 11
score += 1 # equal to: score = score + 1
score /= 2 #  equal to: score = score / 1

# printing
print("your score is ", score)

# f-string's 
# setup
score = 0
height = 1.8
# f-string in action, just add character f in front of the string, put variable inside curly braces and now when it prints, we dont need to convert anything
print(f"your score is {score}, height is {height}")
# it's a more readable way of printing especially for complex cases, available for python 3.6+

# great for things like:  nested variables
username = "Bob"
domain = "example.com"

# f-string's great for more complex combinations like nested varaibles:
print(f"{username}'s email is {username.lower()}@{domain}")

# or complex formatting like with dates:
today = datetime.date.today()
print(f"Today's date is {today:%B %d, %Y}.") 

# or doing inline expressions like using f-strings here to calculate area within the string
width = 10
height = 5
print(f"The area of the rectangle is {width * height} square units.")
