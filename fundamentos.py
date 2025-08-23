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

    # Ignorar parte decimal

    division_result = a //b
    print(f"a / b = {division_result}")

    # Obter o resto da divisão

    modulo_result = a % b
    print(f"a % b = {modulo_result}")

basic_op(5, 3)

'''
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

'''

#COLLECTION VALUES

def collections():
   print('_'*238)
   
# List - coleção de objetos ordenados (ordered)

   fruits_list = ['apple', 'banana', 'orange', 'grape']
   print(fruits_list)

# List function - funções básicas da lista
# Lenght - compirmento

   print(len(fruits_list))

# Index - índice

   print(fruits_list[-3])
 
# Append, inserte, delete (para deletar)

   fruits_list.append('melon')
   fruits_list.insert(0, 'lemon')
   del fruits_list[1]
   print(fruits_list)

# Ordenar a lista: sorted 

   fruits_list.sort()
   print(fruits_list)

# Valor mínimo e valor máximo

   list_num = [2, 5, 3, 9, 5]
   print(f'min: {min(fruits_list)} - max {(fruits_list)}')

# Tuple - tupla, é uma lista que não pode ser modificada

   tuple = ('aluno', 'professor', 'diretor', 'coordenador')
   print(tuple)

# Set - conjunto de items não repetidos e não ordenados

   animals = set(['rabbit', 'dog', 'cat', 'dog'])
   print(animals)
   animals.add('lion')
   animals.remove('rabbit')
   print(animals)

collections()


'''
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
'''

# CONTORLES DE FLUXO

def flow_control(num):
   # Conditional statement: se condição (A) então verdade, senão (B) falso.

   print('-'* 238)


# Verificar se um número recebido é par ou ímpar

   if num % 2 == 0:
      print(f'{num} is even(par).') #even - par
   if num == 0:
      print(f'{num} is additive identity (neutro).') 
   else:
      print(f'{num} is odd(ímpar).') #odd - ímpar

# Verificar a sensação do clima: quente, frio ou agradável
 
   print('-' * 238)

   tempeture = 25
   if tempeture > 30:
     print(" It's hot outside!")
   elif tempeture > 20: # Senão, se temperatura maior que 20
     print("The weather is poleasant today!") # Está agradável
   elif tempeture >20:
      print("It's cold outside") # Está frio

# Apto para a aposentadoria
   
print('-' * 238)

idade = 59
contribuicao = 20

if idade > 65 and contribuicao > 15:
  print('apto para aposentar')
else:
  print('apto para aposentar')




'''
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
'''

# For - para cada item da lista, faça

students = [ "André", "Bruno", "Carlos", "Derick"]

for name in students:
     print(name)
else:
     print("nenhum aluno restante")  

# Fazer algo enquanto a condição seja falsa (WHile - enquanto)

counter = 0

while (counter <= 15 ):
     print(counter)
     counter += 1 #counter = counter + 1



flow_control(5) 



