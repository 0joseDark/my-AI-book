**Retriever-Augmented Generator (RAG)** básico que utiliza a CPU, ideal para rodar em um Windows 10. Usaremos bibliotecas populares como `langchain` e `transformers`. O processo será dividido em etapas com comentários e explicações para cada parte.

O sistema terá duas partes principais:
1. **Indexação:** Criamos um índice de documentos em texto.
2. **Busca e Geração:** O sistema recupera trechos relevantes do índice e gera uma resposta combinando busca e geração.

Segue o passo a passo:

---

### Código Python para RAG
```python
# Importar bibliotecas necessárias
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
import os

# Passo 1: Configuração inicial
# Certifique-se de ter as bibliotecas instaladas: langchain, transformers, faiss
# Utilize `pip install langchain transformers faiss-cpu`

# Passo 2: Configurar os documentos
# Crie uma lista de documentos para indexar. Estes documentos podem ser textos simples.
documents = [
    "Python é uma linguagem de programação de alto nível.",
    "Windows 10 é um sistema operacional popular.",
    "A inteligência artificial é o futuro da tecnologia."
]

# Passo 3: Criar embeddings para os documentos
# Utilizamos o modelo de embeddings MiniLM da HuggingFace para transformar os textos em vetores.
print("Criando embeddings...")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Passo 4: Criar o índice usando FAISS
# FAISS é uma biblioteca rápida para busca vetorial.
print("Criando índice FAISS...")
vectorstore = FAISS.from_texts(documents, embedding_model)

# Passo 5: Configurar o gerador de respostas (LLM)
# Usamos o modelo de linguagem `distilgpt2` da HuggingFace para gerar respostas.
print("Configurando o gerador de respostas...")
generator_pipeline = pipeline("text-generation", model="distilgpt2", device=-1)  # device=-1 usa a CPU
llm = HuggingFacePipeline(pipeline=generator_pipeline)

# Passo 6: Configurar o pipeline RAG
# Ligamos o gerador (LLM) ao índice via o pipeline RAG.
print("Configurando o pipeline RAG...")
retriever = vectorstore.as_retriever()
rag_chain = RetrievalQA(llm=llm, retriever=retriever)

# Passo 7: Testar o sistema RAG
# Solicitamos ao sistema que responda perguntas com base nos documentos indexados.
print("Sistema pronto. Faça perguntas!")
while True:
    query = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
    if query.lower() == "sair":
        print("Encerrando o sistema. Até mais!")
        break
    response = rag_chain.run(query)
    print(f"Resposta: {response}")
```

---

### Explicação do código

1. **Configuração inicial:**  
   Instalamos as bibliotecas necessárias (`langchain`, `transformers`, `faiss`) e importamos os módulos.

2. **Preparação de documentos:**  
   A lista `documents` contém os textos que serão indexados. Estes documentos podem ser adaptados para qualquer tema.

3. **Embeddings:**  
   Usamos o modelo `sentence-transformers/all-MiniLM-L6-v2` para converter documentos em vetores num espaço vetorial.

4. **Indexação com FAISS:**  
   O FAISS cria um índice eficiente para buscas vetoriais, permitindo encontrar documentos relevantes rapidamente.

5. **Gerador (LLM):**  
   Configuramos o modelo `distilgpt2` da HuggingFace para gerar respostas. Ele roda na CPU (`device=-1`).

6. **Pipeline RAG:**  
   Combinamos o índice FAISS (retriever) e o gerador de linguagem (LLM) usando o pipeline do LangChain.

7. **Interação:**  
   O sistema aceita perguntas do usuário no terminal, recupera informações relevantes do índice e usa o LLM para gerar respostas.

---

### Notas importantes
- **Performance:** O uso da CPU é suficiente para testes básicos. Para grandes volumes de dados, considere usar uma GPU.
- **Documentos personalizados:** Substitua a lista de documentos pelos seus textos.
- **Instalação:** Certifique-se de que todos os módulos estão instalados antes de rodar o script.
