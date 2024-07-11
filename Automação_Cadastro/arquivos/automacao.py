import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.3

#acessar o navegador
pyautogui.press("Win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
time.sleep(4)

#acessar o sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")
time.sleep(3)

#Logar com as credenciais no sistema
pyautogui.click(x=604, y=470)
pyautogui.write("qualquer_email.com")
pyautogui.press("Tab")
pyautogui.write("senha_ficticia")
pyautogui.press("Tab")
pyautogui.press("Enter")
time.sleep(2)

#Importar a base de dados
tabela = pd.read_csv("produto.csv")
print(tabela)

#PCadastrar os produtos e repetir esse passo
for linha in tabela.index: 

    #codigo do produto
    pyautogui.click(x=747, y=323)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("Tab")

    #marca do produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("Tab")

    #tipo do produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("Tab")

    #categoria do produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("Tab")

    #preco do produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("Tab")

    #custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("Tab")

    #obs do produto
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
 