msg = "Hi"
user = "jao"
def greeting(msg, user):
  '''
  function to say hi to the user
  msg: message to be printed.
  use: user's name
  '''
  #concatenation -  concatenação
  print(msg +  ', ' + user + '!') 
  #f-string
  print(f'Welcome to the mato, {user}!')
  #repeating
  print('Bye '*3)
greeting(msg, user)


def basic_op(a, b):
  #addition - adição
  sum_result = a + b
  #subtraction - subtração
  diference_result = a - b
  #multiplication - multiplicação
  multiplication_result = a * b
  #division - divisão
  division_result = a / b
  
  print(f' a + b = {sum_result}')
  print(f' a - b = {diference_result}')
  print(f' a * b = {multiplication_result}')
  print(f' a / b = {division_result}')

basic_op(5, 3)







