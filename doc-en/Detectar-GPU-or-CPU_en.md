Following is a Python script to detect and display information about the GPU and CPU available in the system.Also, I will explain when it is better to use GPU or CPU for specific tasks.

---

### Script Python to detect GPU and CPU
`` `python
import torn
import platform
Import Subprocess

def check_gpu ():
"" Check if a GPU is available and displays information about it. ""
print ("checking GPU ...")
if Torch.cuda.is_available ():
Print (F "GPU Available: {TORCH.CUDA.GET_DEVICE_NAME (0)}")
Print (F "Amount of GPUs available: {Torch.Cuda.Device_Count ()}")
Print (F "GPU Memory (MB): {Torch.cuda.get_device_properties (0) .total_memory / (1024 ** 2):. 2f}")
else:
Print ("GPU Not Available. Using CPU.")

def check_cpu ():
"" Displays information about the CPU. ""
Print ("\ Ninformations of the CPU:")
System = Platform.System ()
if system == "Windows":
# Use the `Wmic` command to get CPU information on Windows
Try:
Output = subprocess.check_output (["Wmic", "CPU", "get", "name"], shell = true)
CPU_Name = Output.Decode (). Split ("\ n") [1] .Strip ()
Print (F "CPU: {CPU_Name}")
exception exception and:
Print (F "Error when obtaining CPU information: {e}")
else:
# For Unix-Like Systems (Linux/Mac)
Try:
Output = subprocess.check_output (["lscpu"], universal_newlines = true)
Print (Output)
exception exception and:
Print (F "Error when obtaining CPU information: {e}")

DEF Main ():
"" Main function to check GPU and CPU. "" "
Print ("Hardware Detection: \ n")
check_cpu ()
check_gpu ()

if __name__ == "__main__":
Main ()
`` `

---

### How to execute
1. ** Dependencies: **
- Make sure you have the Pytorch installed to check the GPU: `Pip Install Torch`.
2. ** Run the script: **
- In the terminal or command prompt, execute:
`` `Bash
python script.py
`` `

---

### Which choice is best: CPU or GPU?

#### ** Use CPU: **
- **Tasks:**
- Text processing.
- Light scripts or prototypes.
- Modes of Machine Learning.
- ** Advantages: **
- Lower hardware cost.
- Easy to configure and use.
- ** Limitations: **
- Less efficient for massive calculations.

#### ** Use GPU: **
- **Tasks:**
- Deep Learning (deep neural networks).
- Image and videos processing.
- Mathematical or scientific simulations.
- ** Advantages: **
- Massive parallel processing.
- Much faster than CPUs for specific tasks.
- ** Limitations: **
- Requires dedicated (and more expensive) hardware.
- Higher energy consumption.

---