tamil=int(input("Enter your mark in tamil:"))
english=int(input("Enter your mark in English:"))
maths=int(input("Enter your mark in Maths:"))
science=int(input("Enter your mark in Science:"))
social=int(input("Enter your mark in Social:"))
f=(tamil+english+maths+science+social)
g=(f/5)
print("Your average score is",g)
if(g<35):
    print("Additional class is required")
else:
    print("You are good to go, Keep it up!")
    
