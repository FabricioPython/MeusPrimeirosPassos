programa
{
	
	funcao inicio()
	{
		cadeia livros[] = {"01 Genesis", "02 Exodo", "03 Levitico", "04 Numeros", "05 Deuteronomio"}
		inteiro quantidade[] = {50, 40, 27, 36, 34}
		cadeia nomes[] = {"NOMES:", "CAPS:"}
		escreva("-----------------------------" + "\n")
		escreva("-----------TABELA------------" + "\n")
		escreva("\t", " " + "Pentateuco" + "\t\t" + "\n")
		escreva(nomes[0] + "\t\t\t" + nomes[1], "\n")

		para (inteiro contador = 0; contador <5; contador++) {
			
			escreva(livros[contador], "\t\t", "  ", quantidade[contador],"\n" )
		} escreva("-----------------------------" + "\n")
		  escreva("\n" + "(Esses são os 5 primeiros livros da Bíblia sagrada, e foram escritos por Moisés.)")
	} 
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 617; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */