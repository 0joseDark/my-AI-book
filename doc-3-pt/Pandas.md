O **Pandas** é uma biblioteca de código aberto para a linguagem Python, amplamente utilizada para análise e manipulação de dados. Ela oferece estruturas de dados e ferramentas de alto desempenho para trabalhar com tabelas, séries temporais, e outros formatos de dados estruturados.

### Estruturas de Dados Principais no Pandas

1. **Series**:
   - Um array unidimensional semelhante a uma lista ou array do NumPy, mas com rótulos (índices) associados.
   - É usado para manipular dados rotulados.

   ```python
   import pandas as pd

   # Criar uma Series
   series = pd.Series([10, 20, 30], index=["a", "b", "c"])
   print(series)
   ```

   **Saída**:
   ```
   a    10
   b    20
   c    30
   dtype: int64
   ```

2. **DataFrame**:
   - Uma estrutura bidimensional, similar a uma tabela em SQL ou planilha do Excel.
   - É composta por linhas e colunas, com suporte a indexação e operações vetorizadas.

   ```python
   # Criar um DataFrame
   data = {"Nome": ["Ana", "Bruno", "Carlos"], "Idade": [25, 30, 35]}
   df = pd.DataFrame(data)
   print(df)
   ```

   **Saída**:
   ```
       Nome  Idade
   0    Ana     25
   1  Bruno     30
   2 Carlos     35
   ```

3. **Index**:
   - Representa os índices dos eixos em Series e DataFrames.
   - É personalizável e pode ser usado para acessar ou manipular dados.

---

### Operações Comuns no Pandas

1. **Leitura e Escrita de Dados**:
   O Pandas suporta diversos formatos de dados, como CSV, Excel, JSON, SQL, etc.

   ```python
   # Ler um ficheiro CSV
   df = pd.read_csv("dados.csv")

   # Escrever para um ficheiro CSV
   df.to_csv("saida.csv", index=False)
   ```

2. **Seleção de Dados**:
   - Acessar colunas, linhas, ou células usando `.loc[]` e `.iloc[]`.

   ```python
   # Selecionar uma coluna
   print(df["Nome"])

   # Selecionar uma linha por índice
   print(df.iloc[1])

   # Selecionar células específicas
   print(df.loc[0, "Nome"])
   ```

3. **Filtros e Condições**:
   Aplicar condições para filtrar dados.

   ```python
   # Filtrar pessoas com idade maior que 30
   filtro = df[df["Idade"] > 30]
   print(filtro)
   ```

4. **Agrupamento e Estatísticas**:
   Usar `.groupby()` e funções agregadas para análise.

   ```python
   # Média de idade por nome
   media = df.groupby("Nome")["Idade"].mean()
   print(media)
   ```

5. **Manipulação de Dados**:
   - Adicionar ou remover colunas.
   - Alterar valores.

   ```python
   # Adicionar nova coluna
   df["Cidade"] = ["Lisboa", "Porto", "Coimbra"]

   # Remover coluna
   df.drop("Cidade", axis=1, inplace=True)
   ```

6. **Trabalhando com Dados Faltantes**:
   - Preencher ou remover dados nulos.

   ```python
   # Preencher valores nulos com 0
   df.fillna(0, inplace=True)

   # Remover linhas com valores nulos
   df.dropna(inplace=True)
   ```

---

### Benefícios do Pandas
- Simplicidade para manipular dados complexos.
- Alta eficiência no processamento de grandes volumes de dados.
- Integração com outras bibliotecas de ciência de dados, como NumPy, Matplotlib e Scikit-learn.