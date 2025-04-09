import pyautogui as py
import pandas as pd

# Passo 1: Entrar no sistema da empresa - https://sitedaempresa.com
py.PAUSE = 0.8 # Tempo de espera entre os comandos

#abrir o navegador
py.press('win')
py.write('edge')
# escreve o nome do navegador
py.press('enter')

# digitar o site
py.sleep(2) # espera 2 segundos para o navegador abrir
py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')

# espera 3 segundos para o site carregar
py.sleep(3)

# Passo 2 : Fazer login 
py.click(x=664, y=564) # clica no local específico da tela do seu computador
py.write('email.com.br')

# indo para o campo da senha
py.press('tab')
py.write('senha123')

# indo para o botão de login
py.press('tab')
py.press('enter')
py.sleep(3) # espera 3 segundos para o site carregar

# Passo 3 : Importar a base de dados
pd.read_csv(r'C:\Users\matheusborges\Desktop\Projetos\Automacao_01\src\produtos.csv') #Le o arquivo, caso não esteja no mesmo diretório, colocar o caminho completo do arquivo
tabela = pd.read_csv(r'C:\Users\matheusborges\Desktop\Projetos\Automacao_01\src\produtos.csv') # Cria a tabela com os dados do arquivo CSV
print(tabela) # Mostra a tabela no console

# Passo 4 : Cadastrar 1 produto
for linha in tabela.index: # Para cada linha da tabela
    py.click(x=560, y=363) # clica no botão de cadastrar produto

    codigo = tabela.loc[linha, 'codigo'] # pega o código do produto da linha 0
    py.write(codigo) # escreve o código do produto
    py.press('tab') # vai para o próximo campo

    marca = tabela.loc[linha, 'marca'] 
    py.write(marca) 
    py.press('tab')

    tipo = tabela.loc[linha, 'tipo'] 
    py.write(tipo)
    py.press('tab') 

    categoria = str(tabela.loc[linha, 'categoria']) # pega a categoria do produto da linha 0 e transforma em string
    py.write(categoria) 
    py.press('tab') 

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    py.write(preco_unitario) 
    py.press('tab') 

    custo = str(tabela.loc[linha, 'custo']) 
    py.write(custo) 
    py.press('tab') 

    obs = str(tabela.loc[linha, 'obs'])  
    if obs != "nan":
        py.write(obs) # escreve a observação do produto

    py.press('tab') 
    py.press('enter') # clica no botão de salvar

    py.scroll(10000) # rola a tela para cima, os 10 mil pixels são para garantir que a tela suba o suficiente

# Passo 5 : Repetir para todos os produtos



