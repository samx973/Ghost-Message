from PIL import Image
from cryptography.fernet import Fernet
import sys

# Steganography Project
# Using LSB algorithm to hide encrypted text inside images

class StegoTool:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
            
        self.cipher = Fernet(self.key)

    def toBinary(self, data):
        # convert string to binary format
        return ''.join(format(ord(i), '08b') for i in data)

    def toString(self, binary_data):
        text = ""
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            text += chr(int(byte, 2))
        return text

    def encrypt(self, msg):
        return self.cipher.encrypt(msg.encode()).decode()

    def decrypt(self, enc_msg):
        try:
            return self.cipher.decrypt(enc_msg.encode()).decode()
        except:
            return None # Wrong key or corrupted data

    def hide(self, imgPath, message, saveName):
        print(f"KEY (Save this): {self.key.decode()}")
        
        # 1. Encrypt and add delimiter
        enc_msg = self.encrypt(message) + "==END=="
        bin_msg = self.toBinary(enc_msg)
        
        try:
            img = Image.open(imgPath)
            width, height = img.size
            img = img.convert("RGB")
            
            # check if image is big enough
            if len(bin_msg) > width * height:
                print("Message is too long for this image.")
                return

            pixels = img.load() # Access pixels directly
            
            data_index = 0
            data_len = len(bin_msg)
            
            # Loop through pixels
            for y in range(height):
                for x in range(width):
                    if data_index < data_len:
                        r, g, b = pixels[x, y]
                        # Modify the LSB of Red channel
                        new_r = (r & ~1) | int(bin_msg[data_index])
                        pixels[x, y] = (new_r, g, b)
                        data_index += 1
                    else:
                        break
                if data_index >= data_len:
                    break
            
            img.save(saveName)
            print("Done! Image saved.")
            
        except Exception as e:
            print(f"Error: {e}")

    def reveal(self, imgPath):
        try:
            img = Image.open(imgPath)
            img = img.convert("RGB")
            pixels = img.load()
            
            width, height = img.size
            binary_data = ""
            
            # Extract bits
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    binary_data += str(r & 1)

            # Convert to text and look for delimiter
            current_chars = ""
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                char = chr(int(byte, 2))
                current_chars += char
                
                if "==END==" in current_chars:
                    encrypted_part = current_chars.split("==END==")[0]
                    decrypted = self.decrypt(encrypted_part)
                    
                    if decrypted:
                        print(f"\nMessage Found: {decrypted}\n")
                    else:
                        print("\nFailed to decrypt (Wrong Key?)")
                    return

            print("No hidden message found.")
            
        except Exception as e:
            print(f"Error opening image: {e}")


# Main Program
if __name__ == "__main__":
    print("--- Stego Tool ---")
    action = input("1 to Hide, 2 to Reveal: ")
    
    if action == '1':
        p = input("Image path: ")
        m = input("Message: ")
        out = input("Output name (use .png): ")
        
        s = StegoTool()
        s.hide(p, m, out)
        
    elif action == '2':
        k = input("Enter Key: ").encode()
        p = input("Image path: ")
        
        s = StegoTool(key=k)
        s.reveal(p)
        ##test