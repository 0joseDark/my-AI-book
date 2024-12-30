### Como funciona este script?

1. **Seleção de Arquivo de Entrada**: O botão "Selecionar" abre um explorador de arquivos para escolher um arquivo `.md`.
2. **Seleção de Pasta de Saída**: Outro botão abre um explorador de pastas para definir onde salvar o arquivo traduzido.
3. **Tradução**: O botão "Traduzir" lê o conteúdo do arquivo Markdown, usa a API do Google Translate para traduzir do português para o inglês e salva o resultado na pasta selecionada, mantendo o formato Markdown.

### Requisitos

- **Instalar as dependências**: Execute no terminal:
  ```bash
  pip install googletrans==4.0.0-rc1
  ```

### Considerações

- Este script depende da API `googletrans`, que pode ter limitações de uso.
- Caso precise de controle avançado ou suporte oficial, considere usar a API oficial do Google Cloud Translation.
