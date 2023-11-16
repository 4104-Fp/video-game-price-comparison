# Video Game Price Comparison

## Table of contects

- [About](#about)
- [Usability Goals](#usability-goals)
- [Design](#design)
- [Project Setup](#project-setup)
  - [Installing Virtual Environment](#installing-virtual-environment)
  - [Adding virtualenv to PATH (if needed)](#adding-virtualenv-to-path-if-needed)
    - [For Mac](#for-mac)
    - [For Windows](#for-windows)
  - [Creating and Activating Virtual Environment](#creating-and-activating-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)

---

## API

- [CheapShark](https://apidocs.cheapshark.com/)

## About

This project deals with displaying Video game deals

---

## Usability Goals

1. Find video game deals
2. Compare prices between stores

---

## Design

- in progress sketching out the design

---

## Project Setup

This document guides you through the process of setting up a virtual environment, activating it, installing the
necessary dependencies, and ensuring the `virtualenv` script is correctly placed in your PATH.

### Installing Virtual Environment

1. **Install `virtualenv`**:
   ```bash
   pip install --user virtualenv
   ```

### Adding virtualenv to PATH (if needed)

#### For Mac:

1. Open your terminal.
2. Run the following command to open the `~/.zshrc` file in a text editor (assuming you're using `zsh` as your shell,
   substitute `.bash_profile` for `.zshrc` if you're using `bash`):
   ```bash
   nano ~/.zshrc
   ```
3. Add the following line at the end of the file, then save and exit:
   ```bash
   export PATH="/Users/yourusername/.local/bin:$PATH"
   ```
4. Apply the changes by sourcing your `~/.zshrc` file:
   ```bash
   source ~/.zshrc
   ```

#### For Windows:

1. Right-click on 'This PC' or 'My Computer' on your desktop or in File Explorer, and choose 'Properties'.
2. Click on 'Advanced system settings'.
3. Click on 'Environment Variables'.
4. Under 'System Variables', scroll down and select the 'Path' variable, then click 'Edit'.
5. Click 'New' and add the path to the directory where `virtualenv` was installed,
   e.g., `C:\Users\yourusername\AppData\Roaming\Python\PythonXX\Scripts`.
6. Click 'OK' to close each window.

### Creating and Activating Virtual Environment

1. **Create a virtual environment** in your project directory:

   ```bash
   virtualenv venv
   ```

2. **Activate the virtual environment**:

   - **On Mac and Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

### Installing Dependencies

1. With the virtual environment activated, **install the project dependencies** listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

Now, your environment is set up, activated, and ready to run the project.
