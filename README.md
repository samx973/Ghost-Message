# 👻 Ghost Message: Secure Steganography Tool

> A cybersecurity tool that combines **LSB (Least Significant Bit) Steganography** with **Fernet Symmetric Encryption** to securely hide messages inside image files.

## 🚀 Overview
Ghost Message is a Python application designed to demonstrate secure data hiding. Unlike traditional steganography tools that simply hide text, this tool encrypts the payload using the `cryptography` library before embedding it into the image pixels. This ensures a double layer of security: obscurement (Steganography) + unreadability (Encryption).

## ✨ Key Features
* **Military-Grade Encryption:** Uses Fernet (AES-128) to encrypt messages before hiding them.
* **LSB Algorithm:** Modifies the least significant bits of image pixels for imperceptible changes.
* **Lossless Format Enforcement:** Automatically handles image formats to prevent data loss (converts to PNG).
* **Interactive CLI:** Simple command-line interface for both hiding (sending) and revealing (receiving) messages.

## 🛠️ Built With
* **Python 3**
* **Pillow (PIL):** For image processing.
* **Cryptography:** For encryption/decryption.

## 📦 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/ghost-message.git](https://github.com/YourUsername/ghost-message.git)
    cd ghost-message
    ```

2.  **Install Dependencies**
    You need to install the external libraries used in the project:
    ```bash
    pip install pillow cryptography
    ```

## 💻 Usage

Run the script using Python:

```bash
python Ghost-message.py
```
 ## Option 1: Hide Message (Sender)
Select option 1.

Enter the path of the image you want to use (e.g., image.jpg).

Type the secret message you want to hide.

SAVE THE KEY: The tool will generate a unique encryption key. You must copy and send this key to the receiver securely.

The tool will save the new image as encoded_image.png.

## Option 2: Reveal Message (Receiver)
Select option 2.

Paste the encryption Key provided by the sender.

Enter the path of the encoded image (e.g., encoded_image.png).

The hidden message will be decrypted and displayed.

## ⚠️ Disclaimer
This tool is created for educational purposes and to demonstrate cybersecurity concepts. Please use it responsibly and ethically.