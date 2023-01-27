#Q1
score = int(input("Enter your score"))
if score < 25:

   print("F")

elif score >= 25 and score < 45:

   print("E")

elif score >= 45 and score < 50:

   print("D")

elif score >= 50 and score < 60:

   print("C")

elif score >= 60 and score < 80:

   print("B")

else:

   print("A")

#Q2
years=int(input("Enter year"))
if years%400==0:
    leapyear=True
elif years%100==0:
    leapyear=False
elif years%4==0:
    leapyear=True
else:
    leapyear=False
if leapyear is True:
    print('Year', years,'is a leap year')
else:
    print('Year', years,'is not a leap year')

#Q3
import random
x=1
y=0
while x<=10:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    product=num1*num2
    print("Question",x,"%dx%d="%(num1,num2))
    sol=int(input("Solution="))
    if sol==product:
        print("Correct")
        y+=1
    else:
        print("False")
    x+=1
print("Number of correct answers=",y)

#Q4
for i in range(200):
    if i%5==2 and i%6==3 and i%7==2:
        print(i)