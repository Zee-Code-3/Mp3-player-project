# 🎮 How to Install Pygame Using `venv` on Windows

This guide walks you through creating a Python virtual environment and installing Pygame on Windows.

---

## ✅ Step 0: Make Sure Python Is Installed

Open **Command Prompt** and check if Python is installed:

```cmd
python --version
```

If it's not installed, download the installer from:  
👉 https://www.python.org/downloads/windows/

When installing, **make sure to check** ✅ **"Add Python to PATH"** before clicking Install.

---

## 🥾 Step 1: Create a Virtual Environment

Navigate to your project folder:

```cmd
cd path\to\Mp3-player-project
:: Example folder path, don't copy this exactly
```

Create the virtual environment:

```cmd
python -m venv venv
```

This will create a `venv\` folder containing an isolated Python environment.

---

## 🧼 Step 2: Activate the Virtual Environment

To activate the virtual environment, run:

```cmd
venv\Scripts\activate
```

Your command prompt should now show something like:

```cmd
(venv) C:\Users\YourName\Mp3-player-project>
```

---

## 📦 Step 3: Install Pygame

With the virtual environment activated, install Pygame:

```cmd
pip install pygame
```

To test that it works:

```cmd
python -m pygame.examples.aliens
```

If a small game window opens, it's working!

---

## 📴 Step 4: Deactivate the Virtual Environment

When you're done, deactivate the environment by running:

```cmd
deactivate
```

This will return you to your system’s default Python environment.

---

## ✅ Done!

You now have a working Python virtual environment with Pygame installed on Windows.  
Remember: **each time you want to run the project, activate the virtual environment first!**