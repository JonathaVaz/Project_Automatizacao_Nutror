# Importar as Bibliotecas de Automação de Mouse e Teclado, e de Tempo de Execução do Programa. 

import pyautogui
from time import sleep

# Clicar em "Cadastrar Novo Usuario".
pyautogui.click(980,602,duration=2)


# Clicar e Digitar Usuário.
pyautogui.click(987,540,duration=2)
pyautogui.write("Jonatha")


# Clicar e Digitar Senha.
pyautogui.click(989,568,duration=1)
pyautogui.write("allyty5*")


# Clicar em "Registrar Novo Usuario".
pyautogui.click(875,595,duration=1)


# Clicar e Digitar Usuário.
pyautogui.click(987,540,duration=1)
pyautogui.write("Jonatha")


# Clicar e Digitar Senha.
pyautogui.click(989,568,duration=1)
pyautogui.write("allyty5*")


# Clicar em "Entrar".
pyautogui.click(875,595,duration=1)


# Abrir Arquivo, Extrair cada produto e colar no Programa de Registro.

with open('produtos.txt','r') as arquivo:
   for linha in arquivo:
      produto = linha.split(',')[0]
      quantidade = linha.split(',')[1]
      preco = linha.split(',')[2]

      # Clicar e digitar produto.
      pyautogui.click(690,528,duration=2)
      pyautogui.write(produto)

      # Clicar e digitar quantidade.
      pyautogui.click(682,555,duration=2)
      pyautogui.write(quantidade)

      # Clicar e digitar preço.
      pyautogui.click(687,581,duration=2)
      pyautogui.write(preco)

      # Clicar em "Registrar".
      pyautogui.click(597,743,duration=2)
      sleep(2)
