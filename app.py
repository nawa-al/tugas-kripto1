from flask import Flask, render_template, request, send_file
import numpy as np
import tempfile
import os
import io
from cryptography.fernet import Fernet, InvalidToken
import base64

app = Flask(__name__)

# Generate a key and save it with encrypted content (for demonstration purposes)
def generate_and_save_encrypted_file():
    # Create a key
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Encrypt a sample content
    encrypted_content = cipher_suite.encrypt(b"Contoh teks untuk dienkripsi")
    
    # Save key and encrypted content in a file
    with open("encrypted_file.bin", "wb") as f:
        f.write(key + b'\n' + encrypted_content)

# Uncomment this line to generate and save the initial encrypted file
# generate_and_save_encrypted_file()

@app.route('/')
def index():
    return render_template('index.html', encrypted_text='')

@app.route('/process', methods=['POST'])
def process():
    function = request.form.get('action')  # Mendapatkan aksi (enkripsi/dekripsi)
    mode = request.form.get('mode')  # Mendapatkan mode cipher yang digunakan (AES, Vigenere, dsb)
    key = request.form.get('key')  # Mendapatkan kunci yang digunakan dalam enkripsi/dekripsi

    # Jika fungsi dekripsi, kita ambil input sesuai dengan jenis input
    if function in ['decrypt_file', 'decrypt']:
        # Mendapatkan teks input dari textarea jika tipe input adalah teks
        input_type = request.form.get('input_type')

        if input_type == 'text':
            input_text = request.form.get('input_text')  # Mendapatkan teks dari textarea
            if input_text and key:  # Pastikan ada teks dan kunci
                # Dekripsi berdasarkan mode yang dipilih
                if mode == 'aes':
                    decrypted_text = aes_decrypt(input_text, key)
                elif mode == 'vigenere':
                    decrypted_text = vigenere_decrypt(input_text, key)
                elif mode == 'auto_vigenere':
                    decrypted_text = auto_vigenere_decrypt(input_text, key)
                elif mode == 'playfair':
                    decrypted_text = playfair_decrypt(input_text, key)
                elif mode == 'hill':
                    decrypted_text = hill_decrypt(input_text, key)
                elif mode == 'super_encryption':
                    decrypted_text = super_decrypt(input_text, key)
                else:
                    return 'Metode cipher tidak diimplementasikan.'  # Jika mode tidak dikenal
                
                # Tampilkan hasil dekripsi
                return render_template('index.html', encrypted_text=decrypted_text)
            else:
                return "Teks input atau kunci tidak disediakan."  # Pesan kesalahan jika tidak ada teks input atau kunci
        
        elif input_type == 'file':
            # Mendapatkan file yang diunggah
            file = request.files.get('input_file')  
            if file and key:  # Pastikan ada file dan kunci
                encrypted_content = file.read()  # Membaca konten file
                # Dekripsi berdasarkan mode yang dipilih
                if mode == 'aes':
                    decrypted_text = aes_decrypt(encrypted_content.decode(), key)
                elif mode == 'vigenere':
                    decrypted_text = vigenere_decrypt(encrypted_content.decode(), key)
                elif mode == 'auto_vigenere':
                    decrypted_text = auto_vigenere_decrypt(encrypted_content.decode(), key)
                elif mode == 'playfair':
                    decrypted_text = playfair_decrypt(encrypted_content.decode(), key)
                elif mode == 'hill':
                    decrypted_text = hill_decrypt(encrypted_content.decode(), key)
                elif mode == 'super_encryption':
                    decrypted_text = super_decrypt(encrypted_content.decode(), key)
                else:
                    return 'Metode cipher tidak diimplementasikan.'  # Jika mode tidak dikenal
                
                # Tampilkan hasil dekripsi
                return render_template('index.html', encrypted_text=decrypted_text)
            else:
                return "Tidak ada file atau kunci yang disediakan."  # Pesan kesalahan jika tidak ada file atau kunci
    else:  # Jika fungsinya 'encrypt' (enkripsi)
        input_text = request.form.get('input_text')  # Mendapatkan teks input yang akan dienkripsi
        if function == 'encrypt_file':
            file = request.files.get('input_file')  # Mendapatkan file yang diunggah
            if file and key:
                input_text = file.read().decode()  # Menggunakan konten file sebagai teks input
            else:
                return "Tidak ada file atau kunci yang disediakan."  # Pesan kesalahan jika tidak ada file atau kunci

        if not input_text:
            return "Teks input tidak disediakan."  # Pesan kesalahan jika tidak ada teks input

        # Enkripsi berdasarkan mode yang dipilih
        if mode == 'aes':
            encrypted_text = aes_encrypt(input_text, key)
        elif mode == 'vigenere':
            encrypted_text = vigenere_encrypt(input_text, key)
        elif mode == 'auto_vigenere':
            encrypted_text = auto_vigenere_encrypt(input_text, key)
        elif mode == 'playfair':
            encrypted_text = playfair_encrypt(input_text, key)
        elif mode == 'hill':
            encrypted_text = hill_encrypt(input_text, key)
        elif mode == 'super_encryption':
            encrypted_text = super_encrypt(input_text, key)
        else:
            return 'Metode cipher tidak diimplementasikan.'  # Jika mode tidak dikenal
        
        # Tampilkan hasil enkripsi
        return render_template('index.html', encrypted_text=encrypted_text)

@app.route('/download', methods=['POST'])
def download():
    encrypted_text = request.form.get('encrypted_text')
    
    # Create a temporary file to save the ciphertext
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.bin')
    with open(temp_file.name, 'wb') as f:
        f.write(encrypted_text.encode('utf-8'))  # Write as binary
    
    # Prepare to send the file
    return send_file(temp_file.name, as_attachment=True, download_name='ciphertext.bin', mimetype='application/octet-stream')

from cryptography.fernet import Fernet, InvalidToken
import tempfile
import io
import base64

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    file = request.files['input_file']
    key = request.form.get('key')  # User inputs the key separately, not included in the file

    if file and key:
        try:
            # Read the binary content from the uploaded file
            file_content = file.read()

            # Ensure the key is valid and in correct base64 format
            try:
                key = base64.urlsafe_b64decode(key.strip())
            except (ValueError, TypeError):
                return "Kunci tidak valid. Pastikan kunci adalah base64 yang valid."

            # Create a cipher suite using the provided key
            cipher_suite = Fernet(key)
            
            # Attempt to encrypt the file content
            encrypted_content = cipher_suite.encrypt(file_content)

            # Save the encrypted content to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.bin')
            with open(temp_file.name, 'wb') as f:
                f.write(encrypted_content)  # Write the encrypted content to the file

            # Return the encrypted file for download
            return send_file(temp_file.name, as_attachment=True, download_name='encrypted.bin', mimetype='application/octet-stream')

        except Exception as e:
            return f"Terjadi kesalahan: {str(e)}"

    return "Tidak ada file atau kunci yang disediakan."

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    file = request.files['encrypted_file']
    key = request.form.get('key')  # User inputs the key separately, not included in the file

    if file and key:
        try:
            # Read the binary content from the uploaded file
            encrypted_content = file.read()

            # Ensure the key is valid and in correct base64 format
            try:
                key = base64.urlsafe_b64decode(key.strip())
            except (ValueError, TypeError):
                return "Kunci tidak valid. Pastikan kunci adalah base64 yang valid."

            # Create a cipher suite using the provided key
            cipher_suite = Fernet(key)
            
            # Attempt to decrypt the file content
            try:
                decrypted_content = cipher_suite.decrypt(encrypted_content)

                # Save the decrypted content to a temporary file
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.bin')
                with open(temp_file.name, 'wb') as f:
                    f.write(decrypted_content)  # Write the decrypted content to the file

                # Return the decrypted file for download
                return send_file(temp_file.name, as_attachment=True, download_name='decrypted.bin', mimetype='application/octet-stream')

            except InvalidToken:
                return "Dekripsi gagal: Kunci yang dimasukkan tidak sesuai atau data telah diubah."

        except Exception as e:
            return f"Terjadi kesalahan: {str(e)}"

    return "Tidak ada file atau kunci yang disediakan."

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Vigenère Cipher standard
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            ciphertext += chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            plaintext += chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

# Auto-Key Vigenère Cipher
def auto_vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()  # Hanya huruf kapital
    key_index = 0  # Inisialisasi indeks kunci

    for char in plaintext:
        if char.isalpha():
            # Menghitung shift menggunakan karakter dari key
            shift = ord(key[key_index]) - ord('A')
            # Enkripsi karakter
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index += 1  # Pindah ke karakter berikutnya dalam kunci
            
            # Memperpanjang kunci dengan karakter yang telah dienkripsi
            key += encrypted_char  # Menambahkan karakter yang telah dienkripsi ke kunci
        else:
            ciphertext += char  # Karakter non-huruf ditambahkan tanpa perubahan

    return ciphertext

def auto_vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()  # Hanya huruf kapital
    key_index = 0  # Inisialisasi indeks kunci

    for char in ciphertext:
        if char.isalpha():
            # Memastikan key_index tidak melebihi panjang key
            if key_index >= len(key):
                # Jika key_index lebih besar atau sama dengan panjang key, kembalikan untuk menggunakan karakter sebelumnya
                raise ValueError("Key index out of range. The key is not sufficient for decryption.")

            # Menghitung shift menggunakan karakter dari key
            shift = ord(key[key_index]) - ord('A')
            # Dekripsi karakter
            decrypted_char = chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index += 1  # Pindah ke karakter berikutnya dalam kunci
        else:
            plaintext += char  # Karakter non-huruf ditambahkan tanpa perubahan

    return plaintext

# Playfair Cipher (not implemented)
import numpy as np

def generate_playfair_matrix(key):
    # Buat set untuk menyimpan huruf unik
    key = key.upper().replace('J', 'I')  # Menggabungkan J dan I
    seen = set()
    key_string = ""

    # Tambahkan huruf dari kunci
    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            key_string += char

    # Tambahkan huruf yang tersisa dari alfabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Tidak ada J
        if char not in seen:
            seen.add(char)
            key_string += char

    # Membuat matriks 5x5
    matrix = np.array(list(key_string)).reshape(5, 5)
    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_encrypt(plaintext, key):
    # Siapkan teks yang akan dienkripsi
    plaintext = plaintext.upper().replace('J', 'I')  # Menggabungkan J dan I
    plaintext = ''.join(filter(str.isalpha, plaintext))  # Hanya huruf
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding jika panjang tidak genap

    matrix = generate_playfair_matrix(key)
    ciphertext = ""

    # Enkripsi
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            # Sama dalam baris, geser ke kanan
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Sama dalam kolom, geser ke bawah
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            # Buat persegi
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""

    # Dekripsi
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            # Sama dalam baris, geser ke kiri
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Sama dalam kolom, geser ke atas
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            # Buat persegi
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext

# Contoh penggunaan
key = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = playfair_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = playfair_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)


# Helper function to calculate modular inverse of a number mod 26
def modinv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Helper function to calculate determinant modulo 26
def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # Calculate determinant
    det_inv = modinv(det, mod)  # Find modular inverse of determinant
    
    if det_inv is None:
        return None, "Determinant has no inverse, decryption not possible."
    
    # Calculate the adjugate matrix
    matrix_inv = np.round(det_inv * np.linalg.inv(matrix) * det).astype(int) % mod
    return matrix_inv % mod, None

def mod_inverse(a, m):
    # Fungsi untuk mencari invers modulo dari a dalam modulus m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, modulus):
    # Hitung determinan
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = mod_inverse(det, modulus)
    
    if det_inv is None:
        return None, "Determinant has no inverse, decryption not possible."
    
    # Hitung invers dari matriks
    matrix_inv = np.round(det_inv * np.linalg.inv(matrix) * det).astype(int) % modulus
    return matrix_inv % modulus, None

# Hill Cipher encryption
def hill_encrypt(plaintext, key):
    n = int(np.sqrt(len(key)))
    key_matrix = [ord(char.upper()) - ord('A') for char in key]
    
    if len(key_matrix) != n * n:
        return "Key length must be a perfect square."
    
    key_matrix = np.array(key_matrix).reshape((n, n))
    
    # Prepare plaintext by padding if necessary
    while len(plaintext) % n != 0:
        plaintext += 'X'  # Padding with 'X'
        
    plaintext_vector = [(ord(char.upper()) - ord('A')) for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape((-1, n))

    result = []
    for vec in plaintext_matrix:
        encrypted_vec = np.dot(key_matrix, vec) % 26
        result.extend(encrypted_vec)

    ciphertext = ''.join([chr(int(num) + ord('A')) for num in result])
    return ciphertext

# Hill Cipher decryption
def hill_decrypt(ciphertext, key):
    n = int(np.sqrt(len(key)))
    key_matrix = [ord(char.upper()) - ord('A') for char in key]
    
    if len(key_matrix) != n * n:
        return "Key length must be a perfect square."
    
    key_matrix = np.array(key_matrix).reshape((n, n))

    # Calculate the inverse of the key matrix (mod 26)
    inv_key_matrix, error = matrix_mod_inverse(key_matrix, 26)
    
    if inv_key_matrix is None:
        return error  # If there's an error, return it

    ciphertext_vector = [(ord(char.upper()) - ord('A')) for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape((-1, n))

    result = []
    for vec in ciphertext_matrix:
        decrypted_vec = np.dot(inv_key_matrix, vec) % 26
        result.extend(decrypted_vec)

    plaintext = ''.join([chr(int(num) + ord('A')) for num in result])
    return plaintext

decrypted_message = hill_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)

# Super Encryption (combinatory method)
def super_encrypt(plaintext, key):
    encrypted_text = vigenere_encrypt(plaintext, key)
    # You can add more encryption methods here
    return encrypted_text

def super_decrypt(ciphertext, key):
    decrypted_text = vigenere_decrypt(ciphertext, key)
    # You can add more decryption methods here
    return decrypted_text

if __name__ == '__main__':
    app.run(debug=True)
