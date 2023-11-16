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

- [CheapShark API Documentation](https://apidocs.cheapshark.com/)

CheapShark API provides access to the latest video game deals across various online stores. It offers detailed information about discounts, game prices, store ratings, and deal ratings. This allows us to compare prices efficiently and present the best deals to our users.

## About

The "Video Game Price Comparison" project is a web application designed to help gamers find the best deals for their favorite video games. Utilizing the CheapShark API, this application compares prices across multiple online gaming stores, ensuring users have access to the most cost-effective options. Our platform is not just about finding the cheapest price; it's about making informed purchasing decisions with comprehensive deal ratings and store reviews. 

Whether you are a casual gamer or a dedicated enthusiast, this tool is your gateway to affordable gaming experiences. Our easy-to-use interface and powerful search capabilities ensure that you are only a few clicks away from your next great gaming adventure.

---

## Usability Goals

1. **Efficient Price Comparison**: Quickly compare game prices across different stores, ensuring users can find the best deals with ease.
2. **Deal Rating System**: Implement a deal rating system to help users discern the quality of the deals beyond just the price.
3. **User-Friendly Interface**: Design an intuitive and straightforward interface that caters to both tech-savvy individuals and those less familiar with such platforms.
4. **Responsive Design**: Ensure the application is accessible and functional across various devices and screen sizes.
5. **Error Prevention and Handling**: Implement robust error checking and provide clear feedback, minimizing user frustration and confusion.

---

## Design

- in progress sketching out the design

---

## Project Setup

---

### **If you clone and open this project with an IDE such as PyCharm, you can skip the following steps.**

---

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
