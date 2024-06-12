print("$1+1=?$")
a = input()
if a!="2":
  raise Exception(f"Your answer is wrong! The answer of this question is not {a}")
print("You are correct, then please answer $2+2=?$")
b = input()
if b!="4":
  raise Exception(rf"You are wrong , $2+2 \neq {b}$!")
