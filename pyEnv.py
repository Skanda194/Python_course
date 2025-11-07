"""
What is a Virtual Environment in Python?

A virtual environment is an isolated space for a Python project. It has its own Python interpreter and packages, so dependencies of one project do not affect others or the system Python.

Main benefits  
	Avoid version conflicts (e.g., Project A needs Django 3, Project B needs Django 5)  
	No need for admin/sudo rights  
	Easy to share exact package versions with teammates  

Built-in `venv` (Python 3.3+)

Step-by-step commands (works on Windows, macOS, Linux)

 1. Open terminal and go to your project folder
cd /path/to/your/project
 Example:
mkdir myproject && cd myproject

 2. Create virtual environment
python -m venv venv           Windows
python3 -m venv venv          macOS / Linux

 3. Activate it
 Windows Command Prompt
venv\Scripts\activate

 Windows PowerShell
venv\Scripts\Activate.ps1

 macOS / Linux
source venv/bin/activate

 You will see (venv) at the start of your prompt

 4. Install packages (only inside this project)
pip install --upgrade pip
pip install requests django numpy

 5. Save exact versions for others
pip freeze > requirements.txt

 6. Deactivate when done
deactivate

"""

