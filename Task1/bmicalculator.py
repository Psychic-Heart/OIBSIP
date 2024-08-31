w=float(input("Input your weight in Kg : "))
h=float(input("Input your height in cm : "))
b=w/((h/100)**2)
bmi=round(b,2)
if bmi<18.5:
  print(f"Your BMI value is : {bmi}. You are UnderWeight!")
elif 18.5<=bmi<25:
  print(f"Your BMI value is : {bmi}. You are Healthy!")
elif 25<=bmi<30:
  print(f"Your BMI value is : {bmi}. You are OverWeight!")
else:
  print(f"Your BMI value is : {bmi}. You have obesity!")
