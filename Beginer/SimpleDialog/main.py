def request(string):
  return input()

def show_result(login, password, name, age):
  print('Your login: {}\n'.format(login))
  print('Your password: {}\n'.format(password))
  print('Your name: {}\n'.format(name))
  print("Your age: {}\n".format(age))

def show_result_title(string, top_char, bottom_char):
  print(str(top_char) * len(string))
  print(string)
  print(str(bottom_char) * len(string))

login = request("Please, enter login:")
password = request("Please, enter password:")
name = request("Please, enter your name:")
age = request("Please, enter your age:")

show_result_title('Personal resume')
show_result(login, password, name, age)
