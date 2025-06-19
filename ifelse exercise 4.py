tamil=int(input("Enter your mark in Tamil:"))
english=int(input("Enter your mark in English:"))
maths=int(input("Enter your mark in Maths:"))
science=int(input("Enter your mark in Science:"))
social=int(input("Enter your mark in Social:"))
total=(tamil+english+maths+science+social)
average=(total/5)
print("Your average score is",average)
if(average<35):
    print("Additional class is required")
else:
    print("You are good to go, Keep it up!")
    
