Segue um script Python para detectar e exibir informações sobre a GPU e CPU disponíveis no sistema. Além disso, vou explicar quando é melhor usar a GPU ou a CPU para tarefas específicas.

---

### Script Python para Detectar GPU e CPU
```python
import torch
import platform
import subprocess

def check_gpu():
    """Verifica se uma GPU está disponível e exibe informações sobre ela."""
    print("Verificando GPU...")
    if torch.cuda.is_available():
        print(f"GPU disponível: {torch.cuda.get_device_name(0)}")
        print(f"Quantidade de GPUs disponíveis: {torch.cuda.device_count()}")
        print(f"Memória da GPU (MB): {torch.cuda.get_device_properties(0).total_memory / (1024 ** 2):.2f}")
    else:
        print("GPU não disponível. Usando a CPU.")

def check_cpu():
    """Exibe informações sobre a CPU."""
    print("\nInformações da CPU:")
    system = platform.system()
    if system == "Windows":
        # Usar o comando `wmic` para obter informações da CPU no Windows
        try:
            output = subprocess.check_output(["wmic", "cpu", "get", "name"], shell=True)
            cpu_name = output.decode().split("\n")[1].strip()
            print(f"CPU: {cpu_name}")
        except Exception as e:
            print(f"Erro ao obter informações da CPU: {e}")
    else:
        # Para sistemas Unix-like (Linux/Mac)
        try:
            output = subprocess.check_output(["lscpu"], universal_newlines=True)
            print(output)
        except Exception as e:
            print(f"Erro ao obter informações da CPU: {e}")

def main():
    """Função principal para verificar GPU e CPU."""
    print("Detecção de Hardware:\n")
    check_cpu()
    check_gpu()

if __name__ == "__main__":
    main()
```

---

### Como Executar
1. **Dependências:** 
   - Certifique-se de ter o PyTorch instalado para verificar a GPU: `pip install torch`.
2. **Rodar o script:** 
   - No terminal ou prompt de comando, execute:  
     ```bash
     python script.py
     ```

---

### Qual Escolha é Melhor: CPU ou GPU?

#### **Usar CPU:**
- **Tarefas:** 
  - Processamento de texto.
  - Scripts leves ou protótipos.
  - Modelos de machine learning pequenos.
- **Vantagens:** 
  - Menor custo de hardware.
  - Fácil de configurar e usar.
- **Limitações:** 
  - Menos eficiente para cálculos massivos.

#### **Usar GPU:**
- **Tarefas:** 
  - Deep learning (redes neurais profundas).
  - Processamento de imagens e vídeos.
  - Simulações matemáticas ou científicas.
- **Vantagens:** 
  - Processamento paralelo massivo.
  - Muito mais rápido que CPUs para tarefas específicas.
- **Limitações:** 
  - Requer hardware dedicado (e mais caro).
  - Maior consumo de energia.

---

