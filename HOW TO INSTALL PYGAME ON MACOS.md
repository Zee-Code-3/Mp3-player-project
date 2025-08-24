# 🎮 How to Install Pygame Using `venv` on macOS

This guide walks you through creating a Python virtual environment and installing Pygame on macOS.

---

## ✅ Step 0: Make Sure Python Is Installed

Check if Python 3 is installed:

```bash
python3 --version
```

If it's not installed, use Homebrew:

```bash
brew install python
```

Or download from: https://www.python.org/downloads/

---

## 🥾 Step 1: Create a Virtual Environment

Navigate to the project folder:

```bash
cd Mp3-player-project
# Example folder path, don't copy this exactly
```

Create the virtual environment in your folder:

```bash
python3 -m venv venv
```

This will create a `venv/` directory containing an isolated Python environment.

---

## 🧼 Step 2: Activate the Virtual Environment

 To activate the virtual environment, run:

```bash
source venv/bin/activate
```

Your terminal prompt will change to show the environment is active:

```bash
(venv) your-user-name@Mac project-folder %
```

---

## 📦 Step 3: Install Pygame

Now that your virtual environment is active, install Pygame using pip or python3:

```bash
pip install pygame
```
only use python3 if pip does not work for you:

```bash
python3 install pygame
```

You can test it with:

```bash
python3 -m pygame.examples.aliens
```

If a small game window opens, it's working!

---

## 📴 Step 4: Deactivate the Virtual Environment

Once you're done working:

```bash
deactivate
```

This will return you to your system’s default Python environment.

---

## ✅ Done!

You now have a working Python virtual environment with Pygame installed on macOS.  
Remember: **each time you want to run the project, activate the virtual environment first!**