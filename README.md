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
    ...
}
