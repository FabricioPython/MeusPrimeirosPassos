# Exercício com selenium.

O objetivo é entrar em um site específico de indicadores financeiros e baixar uma tabela csv com os dados de oscilação do dólar.

Um imprevisto que ocorreu foi um segundo pop-up que aparecia sem um tempo definido. Percebi que ele ativava toda vez que o cursor se aproximava da barra de fechar do site, quando não mexia o cursor ele aparecia quase que aleatoriamente bugando o código. Então fiz uma simulação do mouse com pyautogui que ativava o segundo pop-up perfeitamente para que pudesse ser fechado e continuar o código sem problemas.