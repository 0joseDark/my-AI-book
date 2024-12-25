Vou criar um **Retriever-Augmented Generator (RAG)** básico que utiliza a CPU, ideal para rodar em um Windows 10. 
Usaremos bibliotecas populares como `langchain` e `transformers`. O processo será dividido em etapas com comentários e explicações para cada parte.

O sistema terá duas partes principais:
1. **Indexação:** Criamos um índice de documentos em texto.
2. **Busca e Geração:** O sistema recupera trechos relevantes do índice e gera uma resposta combinando busca e geração.
### Notas importantes
- **Performance:** O uso da CPU é suficiente para testes básicos. Para grandes volumes de dados, considere usar uma GPU.
- **Documentos personalizados:** Substitua a lista de documentos pelos seus textos.
- **Instalação:** Certifique-se de que todos os módulos estão instalados antes de rodar o script.
