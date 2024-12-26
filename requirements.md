O ficheiro `requirements.txt` é utilizado para listar as dependências do projeto Python, facilitando a instalação dos pacotes necessários. Aqui está como criar e usar este ficheiro:

---

### **1. Identificar as dependências do projeto**
- Se você já tem um ambiente virtual configurado com os pacotes instalados, pode gerar o ficheiro automaticamente.
- Caso contrário, liste manualmente os pacotes que o projeto precisa.

---

### **2. Criar o ficheiro `requirements.txt` automaticamente**
1. **Ative o ambiente virtual:**
   ```bash
   picoYOLO_env\Scripts\activate
   ```
   
2. **Liste os pacotes instalados:**
   Execute o seguinte comando:
   ```bash
   pip freeze > requirements.txt
   ```
   Isso criará um ficheiro `requirements.txt` com os pacotes e versões instalados no ambiente virtual.

3. **Exemplo de saída gerada:**
   O ficheiro `requirements.txt` pode ter uma aparência semelhante a esta:
   ```
   numpy==1.24.3
   torch==2.0.1
   torchvision==0.15.2
   opencv-python==4.5.5.64
   matplotlib==3.7.2
   ```

---

### **3. Criar manualmente o ficheiro `requirements.txt`**
Se você quiser criar o ficheiro manualmente:
1. Abra um editor de texto (ex.: Notepad).
2. Liste os nomes dos pacotes e suas versões, como no exemplo acima.
3. Salve o ficheiro com o nome `requirements.txt` no diretório do projeto.

---

### **4. Instalar dependências a partir do ficheiro**
Quando outra pessoa (ou você mesmo, em outro ambiente) quiser configurar o projeto, basta usar:
```bash
pip install -r requirements.txt
```
Este comando instala todos os pacotes listados no ficheiro.

---

### **5. Boas práticas**
- Inclua as versões dos pacotes para evitar problemas de incompatibilidade.
- Atualize o ficheiro sempre que adicionar ou remover pacotes do projeto.
- Para projetos longos, considere separar requisitos opcionais em ficheiros adicionais, como `requirements-dev.txt`.
