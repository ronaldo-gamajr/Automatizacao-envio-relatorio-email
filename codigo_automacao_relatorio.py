#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Biblotecas:

import pyautogui
import time
import pyperclip
import pandas as pd
pyautogui.PAUSE = 1


# In[ ]:


# Download da base de dados 

pyautogui.alert("Iniciando tarefa, aperte OK para continuar. Aguarde a tarefa ser executada.")

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://######")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(2885, 365, clicks=2)
time.sleep(2)
pyautogui.click(2886, 481, clicks=1)
pyautogui.click(3846, 240, clicks=1)
pyautogui.click(3585, 773, clicks=1)
time.sleep(5)


# In[6]:


# Importar a base de dados
df = pd.read_excel(r'local/arquivo')
display(df)


# In[7]:


# Calcular os indicadores (faturamento e quantidade)

faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()


# In[8]:


# Enviar o e-mail para o destinatário pré-definido

pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://exemplo@email.com')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(2534, 230, clicks=1)
pyautogui.write('exemplo@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
assunto= 'Relatório de Vendas de Ontem'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto=f"""

Prezados

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}

Atenciosamente
Ronaldo da Gama
"""
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')


# In[ ]:




