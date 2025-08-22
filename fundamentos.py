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

'''
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

'''

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

  #ignorar parte decimal

  division_result = a //b
  print(f"a / b = {division_result}")

  # obter o resto da divisão

  modulo_result = a % b
  print(f"a % b = {modulo_result}")

basic_op(5, 3)

'''
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

'''

#collection valores
def collections():
   print('_'*30)
   
#list - coleção de objetos ordenados (ordered)

   fruits_list = ['apple', 'banana', 'orange', 'grape']
   print(fruits_list)

#list function - funções básicas da lista
#lenght - compirmento

   print(len(fruits_list))

#index - índice

   print(fruits_list[-3])

 #append, inserte, delete (para deletar)

   fruits_list.append('melon')
   fruits_list.insert(0, 'lemon')
   del fruits_list[1]
   print(fruits_list)

 #ordenar a lista: sorted 

   fruits_list.sort()
   print(fruits_list)

#Valor mínimo e valor máximo

   list_num = [2, 5, 3, 9, 5]
   print(f'min: {min(fruits_list)} - max {(fruits_list)}')

#tuple - tupla, é uma lista que não pode ser modificada

   tuple = ('aluno', 'professor', 'diretor', 'coordenador')
   print(tuple)

#set - conjunto de items não repetidos e não ordenados

   animals = set(['rabbit', 'dog', 'cat', 'dog'])
   print(animals)
   animals.add('lion')
   animals.remove('rabbit')
   print(animals)

collections()


