import random
import string
l=int(input("Enter desired length of password(Greater than 1):"))
j=input("1.UpperCase(Y/N) 2.LowerCase(Y/N) 3. Number(Y/N) 4.Symbol(Y/N): (Example:YYYY)")
j.lower()
s=list(j)
a=""
u=[]
if s[0]=="y":
  u.append(random.choice(string.ascii_uppercase))
if s[1]=="y":
  u.append(random.choice(string.ascii_lowercase))
if s[2]=="y":
  u.append(random.choice(string.digits))
if s[3]=="y":
  u.append(random.choice(string.punctuation))
c = string.ascii_uppercase if s[0] == "y" else ""
d = string.ascii_lowercase if s[1] == "y" else ""
r = string.digits if s[2] == "y" else ""
t = string.punctuation if s[3] == "y" else ""

a=c+d+r+t
for i in range(l-4):
  u.append(random.choice(a))
random.shuffle(u)

x=""
for i in u:
  x=x+str(i)
p="".join(x)
print(p)
