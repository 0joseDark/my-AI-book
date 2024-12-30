The `Requirements.txt` file is used to list the Python project facilities, making it easier to install the necessary packages.

---

### ** 1.Identify project dependencies **
- If you already have a virtual environment configured with the installed packages, you can automatically generate the file.
- Otherwise, handle the packages that the project needs manually.

---

### ** 2.Create the file `Requirements.txt` automatically **
1. ** Activate the virtual environment: **
`` `Bash
Picoyolo_env \ scripts \ Active
`` `

2. ** List the installed packages: **
Run the following command:
`` `Bash
Pip Freeze> Requirements.txt
`` `
This will create a file `Requirements.txt` with packages and versions installed in the virtual environment.

3. ** Example of output generated: **
The `Requirements.txt` file may look like this:
`` `
NUMPY == 1.24.3
TORCH == 2.0.1
TORCHVISION == 0.15.2
OpenCV-Python == 4.5.5.64
matplotlib == 3.7.2
`` `

---

### ** 3.Create manually the `refuirements.txt` ** file
If you want to create the file manually:
1. Open a text editor (eg notepad).
2. List the names of the packages and their versions, as in the example above.
3. Save the file with the name `Requirements.txt` in the project directory.

---

### ** 4.Install dependencies from the file **
When someone else (or yourself, in another environment) want to configure the project, just use it:
`` `Bash
PIP Install -r Requirements.TXT
`` `
This command installs all packages listed on the file.

---

### ** 5.Good practices **
- Include the versions of the packages to avoid incompatibility problems.
- Update the file whenever you add or remove packets from the project.
- For long projects, consider separating optional requirements from additional files such as `refucts-dev.txt`.