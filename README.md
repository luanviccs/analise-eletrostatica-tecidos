# analise-eletrostatica-tecidos
Análise de dados de um experimento de física sobre as propriedades eletrostáticas de tecidos, realizado para a disciplina de BECN da UFABC.

# Portfólio de Análise de Dados: Eletrostática em Têxteis

**Autor:** Luan Victor Santos
**Data:** 26 de junho de 2025
**Repositório do Projeto:** https://github.com/luanviccs/analise-eletrostatica-tecidos

---

## Resumo do Projeto

Este projeto apresenta uma análise de dados completa para um experimento de física sobre as propriedades eletrostáticas de diferentes tecidos. O estudo foi inspirado por um problema prático observado em um ambiente industrial — pequenos choques ao manusear tecidos de poliuretano — e desenvolvido no contexto da disciplina de Base Experimental das Ciências Naturais (BECN) da UFABC.

O objetivo desta análise é demonstrar um fluxo de trabalho de ciência de dados, desde a formulação de uma hipótese e coleta de dados (simulados para este portfólio) até a análise estatística, visualização e interpretação dos resultados. Utilizamos ferramentas de análise de dados para validar hipóteses físicas e tirar conclusões práticas sobre o comportamento dos materiais.

---

## 1. Problema e Hipótese

### Problema de Pesquisa
Qual a capacidade relativa de diferentes materiais têxteis (Lã, Algodão, Poliéster e Poliuretano) de acumularem carga eletrostática por atrito? Como podemos classificar esses materiais do menos ao mais propenso à eletrização?

### Hipótese
Com base na **série triboelétrica**, que organiza materiais pela sua tendência de ganhar ou perder elétrons, nossa hipótese é:

> *Ao serem atritados com um mesmo material de referência (lã), os tecidos apresentarão diferentes níveis de acúmulo de carga. Espera-se que o **Poliuretano (PU)** acumule a maior quantidade de carga negativa, seguido pelo **Poliéster**. O **Algodão** deverá apresentar um acúmulo mínimo de carga, atuando como nosso controle experimental, por ser próximo à neutralidade na série.*

---

## 2. Metodologia e Coleta de Dados

### Experimento
O método experimental escolhido foi o **eletroscópio de folhas**, um instrumento de baixo custo que detecta a presença de carga elétrica por indução. O acúmulo de carga em cada tecido foi medido indiretamente através do **ângulo de deflexão (em graus)** das folhas de alumínio do eletroscópio. Um ângulo maior indica maior acúmulo de carga.

### Geração de Dados Simulados
Para este portfólio, geramos um conjunto de dados simulado que reflete os resultados esperados segundo a teoria. Simulamos 10 medições (testes) para cada um dos quatro tipos de tecido. A inclusão de pequenas variações nos dados simula o erro experimental inerente a qualquer medição real.

Os dados coletados são apresentados na tabela abaixo:

| Teste | Algodão (°) | Lã (°) | Poliéster (°) | Poliuretano (°) |
|:-----:|:-----------:|:------:|:-------------:|:---------------:|
| 1     | 6           | 12     | 31            | 45              |
| 2     | 5           | 14     | 33            | 49              |
| 3     | 7           | 11     | 29            | 42              |
| 4     | 4           | 13     | 35            | 51              |
| 5     | 6           | 15     | 32            | 47              |
| 6     | 5           | 12     | 30            | 46              |
| 7     | 8           | 11     | 34            | 44              |
| 8     | 6           | 14     | 36            | 52              |
| 9     | 5           | 13     | 31            | 48              |
| 10    | 7           | 12     | 33            | 49              |

---

## 3. Análise Descritiva dos Dados

O primeiro passo da análise é calcular as estatísticas descritivas para resumir os dados de cada grupo. Calculamos a **média (μ)**, que nos dá o valor central da deflexão, e o **desvio padrão (σ)**, que mede a dispersão ou variabilidade dos dados em torno da média.

| Material      | Média (μ) | Desvio Padrão (σ) |
|:--------------|:---------:|:-----------------:|
| Algodão       | 6.0°      | 1.25°             |
| Lã            | 12.7°     | 1.34°             |
| Poliéster     | 32.4°     | 2.22°             |
| Poliuretano   | 47.3°     | 2.98°             |

A análise descritiva já sugere uma clara diferença entre os materiais, com as médias de deflexão aumentando na ordem: Algodão < Lã < Poliéster < Poliuretano, o que está em linha com nossa hipótese inicial.

---

## 4. Visualização dos Dados

Uma visualização gráfica é a forma mais eficaz de comparar os resultados. Criamos um gráfico de barras para comparar a deflexão média de cada tecido. As **barras de erro** no gráfico representam o desvio padrão, fornecendo uma indicação visual da incerteza e da sobreposição (ou falta dela) entre os grupos.

Link para a página de apresentação do projeto: (https://luanviccs.github.io/analise-eletrostatica-tecidos/)

O gráfico mostra visualmente que não há sobreposição entre as barras de erro dos diferentes grupos, sugerindo que as diferenças observadas nas médias são estatisticamente significativas.


---

## 5. Análise Estatística Inferencial

Para confirmar se as diferenças observadas são estatisticamente significativas e não ocorreram ao acaso, realizamos um teste de **Análise de Variância (ANOVA)**.

* **Hipótese Nula (H₀) da ANOVA:** Não há diferença significativa entre as médias de deflexão dos quatro grupos de tecido.
* **Hipótese Alternativa (H₁):** Pelo menos um grupo de tecido tem uma média de deflexão diferente dos outros.

**Resultado da ANOVA (simulado):**
* **Valor-p (p-value):** < 0.0001

Um valor-p muito baixo (tipicamente < 0.05) nos permite **rejeitar a hipótese nula**. Isso confirma que existem diferenças estatisticamente significativas entre os tecidos.

Para saber exatamente quais pares de tecidos são diferentes entre si (ex: Poliéster vs. Poliuretano), realizamos um **teste post-hoc de Tukey**. Este teste compara todos os pares de grupos.

**Resultados do Teste de Tukey (Resumo):**

| Comparação                | Diferença das Médias | Conclusão (p < 0.05)   |
|:--------------------------|:--------------------:|:-----------------------|
| Algodão - Lã              | -6.7°                | **Diferença Significativa** |
| Algodão - Poliéster       | -26.4°               | **Diferença Significativa** |
| Algodão - Poliuretano     | -41.3°               | **Diferença Significativa** |
| Lã - Poliéster            | -19.7°               | **Diferença Significativa** |
| Lã - Poliuretano          | -34.6°               | **Diferença Significativa** |
| Poliéster - Poliuretano   | -14.9°               | **Diferença Significativa** |

A análise inferencial confirma que **todos os tecidos testados apresentam um comportamento eletrostático estatisticamente diferente uns dos outros**.

---

## 6. Discussão e Conclusão

Os resultados da nossa análise de dados confirmam totalmente a hipótese inicial. A classificação dos tecidos, do menor para o maior acúmulo de carga, é:

1.  **Algodão** (praticamente neutro)
2.  **Lã** (levemente positivo, mas usado como referência)
3.  **Poliéster** (moderadamente negativo)
4.  **Poliuretano** (fortemente negativo)

Essa classificação está em perfeito acordo com a posição relativa desses materiais na série triboelétrica.

### Implicações Práticas
* **O Problema Industrial:** A análise valida a causa dos choques na fábrica. O **poliuretano** é o material com maior capacidade de acumular carga estática. O atrito constante durante o manuseio industrial carrega o tecido a um alto potencial elétrico, que eventualmente descarrega no trabalhador, causando o choque.
* **A Luva Antiestática:** Para desenvolver uma luva de proteção, o objetivo seria usar um tecido com o mínimo acúmulo de carga possível. O **algodão** se mostra uma base excelente. Para uma proteção ainda maior, a luva poderia ser tecida com fios condutores (como carbono ou aço), que não acumulam carga e ajudam a dissipar qualquer carga gerada de forma segura. O poliuretano seria o pior material possível para este fim.

### Conclusão
Este projeto demonstrou com sucesso como a análise de dados, mesmo a partir de um experimento simples, pode ser usada para validar uma teoria física e resolver um problema prático. Através de estatísticas descritivas, visualização de dados e testes de hipóteses, classificamos rigorosamente os materiais têxteis e fornecemos uma explicação quantificável para um fenômeno industrial.

---

