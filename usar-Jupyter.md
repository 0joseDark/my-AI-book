Aqui está um guia passo a passo para instalar, configurar e usar o Jupyter Notebook no Windows 10:

---

## **Passo 1: Instalar o Python**

1. **Baixar Python:**
   - Acesse o site oficial do Python: [https://www.python.org](https://www.python.org).
   - Baixe a versão mais recente do Python para Windows.

2. **Instalar Python:**
   - Execute o instalador baixado.
   - **Marque a opção "Add Python to PATH"** antes de clicar em "Install Now".
   - Conclua a instalação.

---

## **Passo 2: Instalar o Jupyter Notebook**

1. **Abrir o Prompt de Comando:**
   - Pressione `Win + R`, digite `cmd` e pressione `Enter`.

2. **Instalar o Pip (se necessário):**
   - Digite o comando para garantir que o `pip` está atualizado:
     ```bash
     python -m pip install --upgrade pip
     ```

3. **Instalar o Jupyter:**
   - Digite o comando:
     ```bash
     pip install notebook
     ```
   - Aguarde a conclusão da instalação.

---

## **Passo 3: Iniciar o Jupyter Notebook**

1. **Abrir o Jupyter Notebook:**
   - No prompt de comando, navegue até o diretório onde deseja salvar os arquivos:
     ```bash
     cd caminho_do_seu_diretorio
     ```
   - Inicie o Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Este comando abrirá o navegador padrão com a interface do Jupyter Notebook.

2. **Criar um Novo Notebook:**
   - Na interface do Jupyter, clique em **"New"** (canto superior direito) e escolha **Python 3**.

---

## **Passo 4: Usar o Jupyter Notebook**

### **1. Interface do Jupyter Notebook**
   - **Células:** O Notebook é dividido em células, que podem conter código ou texto.
   - **Modo de Edição:** Clique em uma célula para editá-la.
   - **Modo de Comando:** Pressione `Esc` para usar atalhos no modo de comando.

### **2. Executar Código**
   - Escreva código Python em uma célula.
   - Pressione `Shift + Enter` para executar a célula e mover para a próxima.
   - Use `Ctrl + Enter` para executar sem sair da célula.

### **3. Adicionar Texto (Markdown)**
   - Mude o tipo da célula para **Markdown** no menu superior.
   - Escreva texto, títulos ou equações (usando LaTeX).
   - Execute com `Shift + Enter` para renderizar.

---

## **Passo 5: Salvar e Exportar**

1. **Salvar o Notebook:**
   - Clique no ícone de disquete ou pressione `Ctrl + S`.

2. **Exportar para Outros Formatos:**
   - No menu superior, vá em **File > Download as**.
   - Escolha formatos como `.ipynb` (notebook), `.html` ou `.pdf`.

---

## **Passo 6: Encerrar o Jupyter Notebook**

1. **Parar o Servidor Jupyter:**
   - No prompt de comando onde iniciou o servidor, pressione `Ctrl + C`.
   - Confirme com `Y` para encerrar.

2. **Fechar o Navegador:**
   - Feche a aba do navegador onde o Jupyter estava aberto.

---

## **Passo 7: Dicas e Recursos Adicionais**

1. **Extensões Úteis:**
   - Instale extensões como `Jupyter Notebook Extensions` para funcionalidades adicionais:
     ```bash
     pip install jupyter_contrib_nbextensions
     jupyter contrib nbextension install --user
     ```

2. **Ferramentas Alternativas:**
   - Experimente o **JupyterLab**, uma versão mais avançada do Jupyter Notebook:
     ```bash
     pip install jupyterlab
     ```

3. **Resolver Problemas:**
   - Se ocorrerem erros, utilize o comando:
     ```bash
     pip install notebook --upgrade
     ```

Agora, você está pronto para usar o Jupyter Notebook para prototipar, testar e documentar seus scripts em Python!
