# Geração de Relatório Automatizado 

## Desafio
Diariamente o sistema atualiza as vendas do dia anterior. Como analista, preciso enviar um e-mail para os meus superiores assim que começo os trabalhos do dia, com o faturamento e a quantidade de produtos vendidos no dia anterior.

## Solução Proposta
Uma solução para o problema é construir um algoritmo que reduza o trabalho operacional, tornando-o mais eficiente.

## Sobre
Projeto desenvolvido utilizando a linguagem Python para automatizar uma análise e elaboração de relatório para um destinatário pré-definido.

As informações que alimentam o código são dados referentes a vendas de vários produtos de diferentes lojas.

![image](https://github.com/ronaldo-gamajr/Automatizacao-envio-relatorio-email/assets/111927733/2b9fd3b5-420f-4a26-b358-1b2942aecfce)

## Algoritmo da automação

1. Entrar no sistema da empresa (onde está o arquivo com os dados);

2. Navegar no sistema e encontrar a base de vendas;

3. Fazer o download da base de vendas;

4. Importar a base de vendas pro Python;

5. Calcular os indicadores da empresa: faturamento e quantidade de produtos vendidos;

6. Enviar um e-mail para a diretoria com os indicadores de venda;

![email_relatorio](https://github.com/ronaldo-gamajr/Automatizacao-envio-relatorio-email/assets/111927733/c90fb04d-8e1d-4cd0-9f38-d3b74acca548)

- Bibliotecas: **Pandas** e **Pyautogui**

5. enviar o e-mail
   
   ```python
   pyautogui.hotkey("ctrl", "enter")
   ```
