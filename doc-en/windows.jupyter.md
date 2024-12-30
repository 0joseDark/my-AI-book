
# **Step by Step to Install and Use Jupyter Notebook on Windows 10**

## **Step 1: Install Python**

1. **Download Python:**
   - Visit the official Python website: [https://www.python.org](https://www.python.org).
   - Download the latest version of Python for Windows.

2. **Install Python:**
   - Run the downloaded installer.
   - **Check the "Add Python to PATH" option** before clicking "Install Now."
   - Complete the installation.

---

## **Step 2: Install Jupyter Notebook**

1. **Open Command Prompt:**
   - Press `Win + R`, type `cmd`, and press `Enter`.

2. **Install Pip (if necessary):**
   - Run the command to ensure `pip` is up to date:
     ```bash
     python -m pip install --upgrade pip
     ```

3. **Install Jupyter:**
   - Run the following command:
     ```bash
     pip install notebook
     ```
   - Wait for the installation to complete.

---

## **Step 3: Start Jupyter Notebook**

1. **Launch Jupyter Notebook:**
   - In the command prompt, navigate to the directory where you want to save files:
     ```bash
     cd your_directory_path
     ```
   - Start Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - This command will open your default browser with the Jupyter Notebook interface.

2. **Create a New Notebook:**
   - In the Jupyter interface, click **"New"** (top-right corner) and choose **Python 3**.

---

## **Step 4: Using Jupyter Notebook**

### **1. Jupyter Notebook Interface**
   - **Cells:** The Notebook is divided into cells that can contain code or text.
   - **Edit Mode:** Click on a cell to edit it.
   - **Command Mode:** Press `Esc` to use shortcuts in command mode.

### **2. Execute Code**
   - Write Python code in a cell.
   - Press `Shift + Enter` to run the cell and move to the next one.
   - Use `Ctrl + Enter` to run the cell without moving.

### **3. Add Text (Markdown)**
   - Change the cell type to **Markdown** from the top menu.
   - Write text, titles, or equations (using LaTeX).
   - Run the cell with `Shift + Enter` to render.

---

## **Step 5: Save and Export**

1. **Save the Notebook:**
   - Click the floppy disk icon or press `Ctrl + S`.

2. **Export to Other Formats:**
   - In the top menu, go to **File > Download as**.
   - Choose formats like `.ipynb` (notebook), `.html`, or `.pdf`.

---

## **Step 6: Stop Jupyter Notebook**

1. **Stop the Jupyter Server:**
   - In the command prompt where the server was started, press `Ctrl + C`.
   - Confirm with `Y` to stop.

2. **Close the Browser:**
   - Close the browser tab where Jupyter was open.

---

## **Step 7: Tips and Additional Resources**

1. **Useful Extensions:**
   - Install extensions like `Jupyter Notebook Extensions` for added functionality:
     ```bash
     pip install jupyter_contrib_nbextensions
     jupyter contrib nbextension install --user
     ```

2. **Alternative Tools:**
   - Try **JupyterLab**, a more advanced version of Jupyter Notebook:
     ```bash
     pip install jupyterlab
     ```

3. **Troubleshooting:**
   - If errors occur, use the command:
     ```bash
     pip install notebook --upgrade
     ```

Now, you're ready to use Jupyter Notebook to prototype, test, and document your Python scripts!
