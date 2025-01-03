**Pillow** é uma biblioteca Python de código aberto amplamente utilizada para manipulação de imagens. Ela é uma versão atualizada e mantida da antiga biblioteca **PIL (Python Imaging Library)**, oferecendo ferramentas para abrir, editar e salvar imagens em vários formatos.

### **Funcionalidades principais do Pillow**
1. **Abrir e salvar imagens** em formatos como JPEG, PNG, BMP, GIF, TIFF, entre outros.
2. **Manipulação básica de imagens**, como redimensionar, recortar, rotacionar e aplicar filtros.
3. **Efeitos avançados**, como ajuste de cores, transformação geométrica e aplicação de máscaras.
4. **Trabalhar com texto**, permitindo adicionar texto às imagens usando fontes personalizadas.
5. **Suporte a transparência**, trabalhando com canais alfa.
6. **Processamento em lote**, útil para aplicar operações em várias imagens automaticamente.

---

### **Instalação**
Para instalar o Pillow, basta usar o pip:
```bash
pip install pillow
```

---

### **Exemplos de Uso**

#### 1. **Abrir e exibir uma imagem**
```python
from PIL import Image

# Abrir uma imagem
imagem = Image.open("exemplo.jpg")

# Exibir a imagem
imagem.show()
```

#### 2. **Redimensionar uma imagem**
```python
from PIL import Image

# Abrir uma imagem
imagem = Image.open("exemplo.jpg")

# Redimensionar
nova_imagem = imagem.resize((300, 300))

# Salvar a nova imagem
nova_imagem.save("redimensionada.jpg")
```

#### 3. **Aplicar um filtro**
```python
from PIL import Image, ImageFilter

# Abrir uma imagem
imagem = Image.open("exemplo.jpg")

# Aplicar o filtro de desfoque
imagem_desfocada = imagem.filter(ImageFilter.BLUR)

# Salvar a imagem desfocada
imagem_desfocada.save("desfocada.jpg")
```

#### 4. **Adicionar texto a uma imagem**
```python
from PIL import Image, ImageDraw, ImageFont

# Abrir uma imagem
imagem = Image.open("exemplo.jpg")

# Configurar o desenho
draw = ImageDraw.Draw(imagem)

# Escolher a fonte (certifique-se de ter o ficheiro da fonte no caminho indicado)
fonte = ImageFont.truetype("arial.ttf", 36)

# Adicionar texto
draw.text((50, 50), "Olá, Mundo!", fill="white", font=fonte)

# Salvar a imagem com texto
imagem.save("com_texto.jpg")
```

#### 5. **Converter uma imagem para escala de cinza**
```python
from PIL import Image

# Abrir uma imagem
imagem = Image.open("exemplo.jpg")

# Converter para escala de cinza
imagem_cinza = imagem.convert("L")

# Salvar a imagem em escala de cinza
imagem_cinza.save("cinza.jpg")
```

---

### **Comentários Importantes**
1. **Formatos Suportados**: Certifique-se de que as extensões das imagens são suportadas pelo Pillow. Se necessário, converta para um formato compatível.
2. **Fontes**: Para adicionar texto, o Pillow precisa de arquivos de fontes (como `.ttf`). Certifique-se de especificar o caminho correto.
3. **Canais de Cor**: Use modos como `RGB`, `RGBA`, ou `L` (escala de cinza) para trabalhar com diferentes tipos de imagem.