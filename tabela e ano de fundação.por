programa
{
	
	funcao inicio()
	{
		// variaveis: contador e verTabela
		inteiro contador = 0, verTabela = 0

		// matriz tabela, amrazena a tabela simples dos 10 primeiros do brasileiro
		cadeia tabela[][] = {{"Flamengo", "71 pontos", "saldo de gols: 21"}, {"Internacional", "69 pontos", "saldo de gols: 26"}, {"Altético-MG", "65 pontos", "Saldo de gols: 17"},
		{"São Paulo", "63 pontos", "Saldo de gols: 17"}, {"Fluminense", "61 pontos", "Saldo de gols: 11"}, {"Grêmio", "59 pontos", "Saldo de gols: 14"}, {"Palmeiras", "58 pontos", "Saldo de gols: 16"},
		{"Santos", "54 pontos", "Saldo de gols: 3"}, {"Atlético-PR", "50 pontos", "Saldo de gols: 0"}, {"Corinthians",  "50 pontos", "Saldo de gols: 0"} 
		}
		// mesu simplificado
		escreva("[1] - Ver tabela, [2] - Ano de Fundação, [3] - Sair: ")
		leia(verTabela)

		// desvio condicional do menu e estrutura de repetição para detalhá-los
		escolha(verTabela){
			caso 1: 
			faca{escreva("\n" + (contador + 1) + " - " + tabela[contador][0] + ", Pontuação: " + tabela[contador][1] + ". SG: " + tabela[contador][2] + "\n" + "\n")
		     contador++
		    }enquanto(contador<=9)
		     pare
               
		     caso 2:
		     cadeia times[] = {"Flamengo, 17 de novembro de 1895 - RJ", "Internacional, 4 de abril de 1909 - RS",
		     "Atlético-MG,  25 de março de 1908 - MG", "São Paulo, 25 de janeiro de 1930 - SP", "Fluminense, 21 de julho de 1902 - RJ",
		     "Grêmio, 15 de setembro de 1903 - RS","Palmeiras, 26 de agosto de 1914 - SP", "Santos, 14 de abril de 1912 - SP", "Atlético-PR, 26 de março de 1924 - PR", "Corinthinas, 1 de setembro de 1910 - SP"}
		     // acima temos um vetor 
		     
		     faca{
		     	escreva("\n" + (contador + 1) + " - " + times[contador] + "\n")
		     	escreva("\n")
		     	contador++
		     	
		     }enquanto(contador<=9)
		     pare

		     caso 3:
		     escreva("saindo.... OPS! Palmeiras não tem Mundial")
		     pare	      
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1793; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */