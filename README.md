# Automatizacao-envio-relatorio-email
Projeto desenvolvido em Python para automatizar envio de relatório por e-mail.

## Algoritmo da automação

1. Entrar no sistema da empresa (onde está o arquivo com os dados);

2. Navegar no sistema e encontrar a base de vendas;

3. Fazer o download da base de vendas;

4. Importar a base de vendas pro Python;

5. Calcular os indicadores da empresa: faturamento e quantidade de produtos vendidos;

6. Enviar um e-mail para a diretoria com os indicadores de venda;

- Bibliotecas: **Pandas** e **Pyautogui**

- Comandos importantes:
  
  - `pyautogui.click` -> clicar
  
  - `pyautogui.press` -> apertar 1 tecla
  
  - `pyautogui.hotkey`-> conjunto de teclas (atalho)
  
  - `pyautogui.write` -> escreve um texto

## Instalando o Pyautogui

```python
!pip install pyautogui
```

## Importar o Pyautogui e pyperclip

```python
import pyautogui
import pyperclip
import time
# o time é para pausas
```

## Adicionando pausa de 1s

```python
pyautogui.PAUSE = 1
```

## Construindo o algoritmo:

- Entrar no sistema da empresa (no nosso caso é o link do drive)

```python
pyautogui.hotkey("ctrl", "t")
```

- Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar) 

```python
pyautogui.copy("link")
pyautogui.hotkey("crtl", "v")
pyautogui.press("enter")

time.sleep(5)
```

- Fazer o download da base de vendas
  
  - Encontrar o position para saber onde clicar:

```python
# espera 5 segundos
pyautogui.time(5)
pyautogui.position()
#colocar o mouse onde o mouse deve cliclar para capturar a posição
#copiar o resultado da posição (x,y)
```

- procedimento para abrir a pasta onde está o arquivo para download:

```python
pyautogui.click(x=000, y=000, clicks=2) # posição da pasta onde está o arquivo
time.sleep(2)
pyautogui.click(x=000, y=000, clicks=2) # clicar no arquivo
pyautogui.click(x=000, y=000, clicks=2) # clicar nos 3 pontinhos
pyautogui.click(x=000, y=000, clicks=2) # clccar no fazer download
time.sleep(5) #esperar o donwload acabar
```

- Importar a base dde vendas pro Python
  
  ```python
  import pandas as pd
  tabela = pd.read_excel(r"C://caminhodoarquivo/nomedoarquivo.formato")
  # sempre que colocar o caminho de um arquivo, coloca o R
  # R deixa o texto cru
  display(tabela) # exibi a tabela de forma mais bonita, só funciona no jupyter.
  ```
* Calcular os indicadores da empresa - Faturamento e a Quantidade de Produtos Vendidos

```python
faturamento = tabela["Nome da Coluna"].sum() # somar a coluna descrita
print(faturamento) # mostra o valor 
quantidade = table["Nome da coluna"].sum() # somar a coluna descrita
print(quantidade) # mostra o valor
```

* Enviar um e-mail para a diretoria com os indicadores de venda
  
  1. abrir a aba
     
     ```python
     pyautogui.hotkey("ctrl", "t")
     ```
  
  2. entrar no link do e-mail - https://link do e-mail
     
     ```python
     pyautogui.copy("link do e-mail")
     pyautogui.hotkey("ctrl", "v")
     pyautogui.press("enter")
     time.sleep(5)
     ```
  
  3. clicar no botão escrever
     
     ```python
     pyautogui.click(x=000, y=000)
     ```
  
  4. preencher as informações do e-mail
     
     ```python
     pyautogui.write("endereço do e-mail")
     pyautogui.press("tab") # para preencher o endereço
     
     
     ```

     ```
    
     pyautogui.press("tab") #pular pro campo de assunto
     pyautogui.copy("Relatório de Vendas")
     pyautogui.hotkey("ctrl", "v")
    
     pyautogui.press("tab") # pular para a mensagem do e-mail
    
     texto = f"""
     Prezados,
    
     Segue relatório de vendas.
     Faturamento: {faturamento:,.2f}
     Quantidade de produtos vendidos: {quantidade:,}
    
     Qualquer dúvida estou à disposição.
     Att.,
     Ronaldo.
     """
     pyperclip.copy(texto)
     pyautogui.hotkey("ctrl", "v")
     # o F é para formatar o texto
     # da pra colocar a variável entre chaves no texto
     ```

5. enviar o e-mail
   
   ```python
   pyautogui.hotkey("ctrl", "enter")
   ```
