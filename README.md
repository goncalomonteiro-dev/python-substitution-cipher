![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/status-Finished-brightgreen)
![Type](https://img.shields.io/badge/type-CLI%20App-purple)
![Category](https://img.shields.io/badge/category-Encryption-orange)


# 🔐 Python Substitution Cipher

A simple Python program that **encrypts and decrypts messages** using a custom substitution cipher.

This project was initially developed as a university exercise and later structured for better readability and GitHub presentation.

---

## ✅ Features
- Encrypt any message using a predefined character mapping  
- Decrypt using the reverse mapping  
- Handles lowercase letters and keeps other characters unchanged  
- Interactive menu  

---

## 🧠 How it Works
Each letter is replaced by another according to the `cifra` dictionary defined in the code:


```python
cifra = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c',
    'f': 'x', 'g': 'z', 'h': 'l', 'i': 'k', 'j': 'j',
    'k': 'h', 'l': 'g', 'm': 'f', 'n': 'd', 'o': 's',
    'p': 'a', 'q': 'q', 'r': 'w', 's': 'e', 't': 'r',
    'u': 't', 'v': 'y', 'w': 'u', 'x': 'i', 'y': 'o',
    'z': 'p'
}
```
The program then automatically generates the reversed dictionary for decryption.

---

## ▶️ Running the Program

- Make sure you have Python 3 installed.
- Run the script using: `python cipher.py`

- You will see a menu like:

--- CIPHER MENU ---
1. Encrypt message
2. Decrypt message
3. Exit

---

## ✅ Example
Input:
hello

Encrypted:
lgssc

---

## 📁 Project Structure

python-substitution-cipher/
│
├── cipher.py       # main script
└── README.md       # project documentation

---

## 📚 What I Learned

- Working with dictionaries in Python
- Creating reverse mappings
- Handling strings and character substitution
- Structuring a Python project for GitHub

---

## 📄 License
This project is free to use for educational purposes.

