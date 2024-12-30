The ** picoyolo ** is a light version of the yolo algorithm (you only look for object detection.It is optimized for limited features such as microcontrollers and embedded systems.To use picoyolo on Windows 10, in European Portuguese, the process involves installing the facilities, setting up the environment and performing the model.

---

### ** 1.Prerequisites **
Before you start, make sure you have the following:
- A PC with Windows 10.
- Internet access to download packages and dependencies.
- Python 3.7 or higher installed.

---

### ** 2.Install python and set up the environment **
1. ** Install Python: **
- Download Python [here] (https://www.python.org/downloads/).
- During installation, select the ** "Add Python to Path" option ** **.

2. ** Create a virtual environment: **
- Open the ** command prompt ** or ** POWERSHELL **.
- Create a virtual environment:
`` `Bash
Python -m Venv picoyolo_env
`` `
- Activate the environment:
`` `Bash
Picoyolo_env \ scripts \ Active
`` `

---

### ** 3.Install dependencies **
1. Install ** pytorch ** and ** TORCHVISION ** (picoyolo requirements):
`` `Bash
PIP INSTALL TORCHVISION
`` `

2. Install other necessary dependencies:
`` `Bash
PIP Install Numpy Matplotlib OpenCV-Python
`` `

3. If the picoyolo project is in a Github repository, clone it:
`` `Bash
git clone https://github.com/<Repposition-picayolo>.git
Picoyolo CD
`` `

4. Install project requirements:
`` `Bash
PIP Install -r Requirements.TXT
`` `

---

### ** 4.Configure the Picoyolo model **
1. ** Get the pre-trained weights: **
- Download the pre-trained picoyolo weights, usually available as `.pth` or` .weights` files in the repository.

2. ** Edit the configuration file: **
- Locate the model configuration file (eg: `config.py` or` model_config.json`).
- Update the settings, such as the path to the weights and the input/output parameters.

3. ** Configure classes: **
- In the class file (eg: `coconut.names` or` classes.txt`), list the names of the classes that the model must recognize.

---

### ** 5.Test Picoyolo **
1. ** Run the model: **
- Use the main repository script for object detection:
`` `Bash
python detect.py -iMage path_da_imagem.jpg
`` `
- Replace `detect.py` with the correct repository script.

2. ** Additional parameters: **
- To use a webcam or video:
`` `Bash
python detect.py - -video path_video.mp4
`` `
- To save results:
`` `Bash
Python Detect.py -Save_output Way_do_output
`` `

---

### ** 6.View results **
1. Make sure the model output is configured to save images or videos with the detections.
2. Use ** OPENCV ** or ** matplotlib ** to view the results:
`` `python
import cv2
image = cv2.imread ("result.jpg")
cv2.imshow ("result", image)
cv2.waitkey (0)
CV2.DESTROYALLWINDOWS ()
`` `

---

### ** 7.Train Picoyolo (optional) **
If you want to train the model with a new data set:
1. ** Prepare the data: **
- Organize the data in yolo format, with images and annotation files `.txt`.

2. ** Setting the training: **
- Edit the training file (eg: `train.py`) to include the path to the initial data and weights.

3. ** Perform training: **
`` `Bash
python train.py -datada_dos_dados - -weights pesos_inicials.pth
`` `

---

### ** 8.Common problems and solutions **
1. ** CUDE ERROR: **
- If your PC does not have compatible GPU, force the use of CPU:
`` `python
Device = Torch.Device ("CPU")
`` `

2.
- Make sure to install all packages listed on the `Requirements.TXT` file.

---