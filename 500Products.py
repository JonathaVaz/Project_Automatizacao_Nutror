''' 
Relatório : 

Para Resolver essa Tarefa vamos entrar no Site (  https://cadastroprodutos-devaprender.netlify.app/   ), após entrar no Site, vamos abrir a planilha,
após ter aberto a planilha devemos copiar o Dado que está dentro do campo produto e colar no seu campo respectivo dentro do sistema web,
copiar o dado que está dentro do campo fornecedor e colar em seu campo respectivo, copiar o dado que está dentro do campo categoria e depois...
ao finalizar a primeira entrada, ir para a próxima até finalizar a entrada de todos os dados.

'''

# Passos Descritivos :

# 1 - Acessar o Site (   https://cadastroprodutos-devaprender.netlify.app/   )

# 2 - Abrir a Planilha. 

# 3 - Copiar o Dado que está dentro do campo "produto" e colar no seu campo respectivo dentro do Sistema Web.

# 4 - Repetir o mesmo Processo para as outras colunas.

# 5 - Repetir até chegar ao último cadastro da planilha com os 500 cadastros.


# Codigo 

import pyautogui  # Biblioteca de Automação de Mouse e Teclado
import openpyxl   # Biblioteca para Abertura e Leitura de Arquivos xlsx


workbook = openpyxl.load_workbook(r'C:\Users\Pichau\Desktop\Nutror Projetos\produtos.xlsx')    # Criação de Variável e Recurso de Entrada no Arquivo xlsx

sheet_produtos = workbook['produtos']     # Criação de Variável para Acessar a Variável "workbook" correspondente ao Arquivo na Area de "Produtos"

for linha in sheet_produtos.iter_rows(min_row=2,max_row=501):      # Criando um Laço de Repetição com as Tabelas Correspondentes do Arquivo
    
    produto = linha[0].value
    fornecedor = linha[1].value
    categoria = linha[2].value
    quantidade = linha[3].value
    valor_unitario = linha[4].value
    notificar_venda = linha[5].value
    
    # Colando Dados no Campo "Produto"
    pyautogui.click(1235,411,duration=2)
    pyautogui.write(produto)
    
    # Colando Dados no Campo "Fornecedor"
    pyautogui.click(1486,412,duration=2)
    pyautogui.write(fornecedor)
    
    # Colando Dados no Campo "Categoria"
    pyautogui.click(1181,508,duration=2)
    pyautogui.write(categoria)
    
    # Colando Dados no Campo "Valor Unitario"
    pyautogui.click(1514,505,duration=2)
    pyautogui.write(valor_unitario)
    
    # Criando uma Condição Booleana
    # Se "Notificar Venda" for igual a "Sim", marcar "Sim"
    # Se "Notificar Venda" for igual a "Não", marcar "Não"
    
    if notificar_venda == "Sim":
        pyautogui.click(1153,594,duration=2)
    elif notificar_venda == "Não":
        pyautogui.click(1259,596,duration=2)
    
    # Clicar em "Registrar Produto"
    pyautogui.click(1210,661,duration=2)
    
    # Clicar em "Ok", na mensagem de "Cadastro com Sucesso" 
    pyautogui.click(1592,210,duration=2)
    


# Obs:

# - Opção "Categoria" e "Valor Unitario" escrito corretamente. 
# - Importar o pyperclip.
# - Colagem de Dados seria em "Categoria" e "Valor Unitario".
# - Invés de "pyautogui.write" usaria "pyperclip.copy(categoria)" + "pyautogui.hotkey('ctrl','v')     campo = (Categoria)
# - Invés de "pyautogui.write" usaria "pyperclip.copy(valor_unitario)" + "pyautogui.hotkey('ctrl','v')     campo = (Valor Unitario)
