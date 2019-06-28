def Login(grow):
  print(grow)
  frap = input() 
  return frap 

def Pass(fog):
  print(fog)
  pswrd = input()
  return pswrd

def Name(trust):
  print(trust)
  urname = input()
  return urname

def Age(howold):
  print(howold)
  urage = input()
  return urage

def result(log,pas,name,age):
  print("Your Login: " + log)
  print("")
  print("Your Password: " + pas)
  print("")
  print("Your Name: " + name)
  print("")
  print("Your Age: "+ age)

def show_result_title(string):
  print("O" * len(string))
  print(string)
  print("X" * len(string))

Well = Login("Please, enter login:")
print("")
Next = Pass("Please, enter password:")
print("")
Socity = Name("Please, enter your name:")
print("")
Old = Age("Please, enter your age:")
print("\n\n")

show_result_title("="*50 + "YOUR RESULT" + "="*50)

result(Well,Next,Socity,Old)