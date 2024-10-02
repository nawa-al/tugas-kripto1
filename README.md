# WEB GUI ENKRIP-DEKRIP
###### Program ini adalah aplikasi berbasis web dengan antarmuka grafis (GUI) yang mengimplementasikan berbagai algoritma enkripsi dan dekripsi. Program ini menggunakan salah satu bahasa pemrograman yaitu Python
\
Algoritma yang diimplementasikan termasuk :
1. Vigenere Cipher
2. Auto-Key Vigenere Cipher
3. Playfair Cipher
4. Hill Cipher
5. Super Encryption (kombinasi Vigenere Cipher dan metode kolom transposisi)


## Features WEB GUI Enkrip-Dekrip

- Program dapat menerima input berupa File teks (file bin atau txt) dan Pesan yang diketik dari papan ketik.
- Program mengenkripsi karakter alfabet saja. Karakter non-alfabet (angka, spasi, dan tanda baca) akan dibuang
- Program dapat mendekripsi ciphertext menjadi plaintext semula
- Plaintext dan ciphertext akan ditampilkan pada layar.
- Beberapa Ciphertext yang dihasilkan beberapa Algoritma ditampilkan tanpa spasi dan huruf kapital.
- Pengguna dapat menyimpan ciphertext ke dalam file (opsi "Save As" atau "Download As" dalam format biner)
- Kunci dimasukkan oleh pengguna dengan panjang bebas (Kecuali Algoritma Auto-key dan Hill).
- Program membaca setiap byte dalam file dan mengenkripsinya, termasuk byte header. File terenkripsi tidak dapat dibuka oleh program aplikasi, tetapi dapat didekripsi kembali.
- Ketika mendekripsi, pengguna harus menyimpan dengan ekstensi file yang sama seperti file plaintext. Misalnya, file bertipe .bin harus disimpan sebagai .bin saat didekripsi.
- Pengembang menggunakan framework pemrograman Flask


## Tech

Aplikasi ini dibangun dengan menggunakan :
- [XAMPP] : Digunakan sebagai server lokal untuk menghosting aplikasi web. XAMPP memungkinkan pengembang untuk menjalankan aplikasi PHP dan Python secara bersamaan dengan mudah di lingkungan lokal.
- [Python] : Bahasa pemrograman yang digunakan untuk membangun logika enkripsi dan dekripsi, serta untuk mengelola backend aplikasi. Python juga memungkinkan penggunaan berbagai pustaka untuk pemrosesan matematis yang diperlukan dalam algoritma kriptografi.
- [Visual Studio Code (VSCode)] : Editor kode sumber yang digunakan untuk pengembangan. VSCode menyediakan fitur-fitur seperti debugging, syntax highlighting, dan ekstensi yang mempermudah proses pengembangan aplikasi.
- [HTML] : Digunakan untuk membangun antarmuka pengguna (UI) dari aplikasi berbasis web. HTML akan menampilkan form untuk input plaintext, ciphertext, dan kunci, serta menampilkan hasil enkripsi dan dekripsi.
- [Microsoft Edge] : Browser yang digunakan untuk menampilkan aplikasi web. Microsoft Edge menyediakan performa yang baik dan dukungan untuk fitur-fitur modern dalam pengembangan web.
- [GitHub] : Platform yang digunakan untuk menyimpan dan mengelola versi kode sumber proyek. GitHub memudahkan kolaborasi antar pengembang dan pelacakan perubahan dalam proyek.

## Structure
```
📦tugas_kripto
 ┣ 📂.git
 ┃ ┣ 📂hooks
 ┃ ┃ ┣ 📜applypatch-msg.sample
 ┃ ┃ ┣ 📜commit-msg.sample
 ┃ ┃ ┣ 📜fsmonitor-watchman.sample
 ┃ ┃ ┣ 📜post-update.sample
 ┃ ┃ ┣ 📜pre-applypatch.sample
 ┃ ┃ ┣ 📜pre-commit.sample
 ┃ ┃ ┣ 📜pre-merge-commit.sample
 ┃ ┃ ┣ 📜pre-push.sample
 ┃ ┃ ┣ 📜pre-rebase.sample
 ┃ ┃ ┣ 📜pre-receive.sample
 ┃ ┃ ┣ 📜prepare-commit-msg.sample
 ┃ ┃ ┣ 📜push-to-checkout.sample
 ┃ ┃ ┣ 📜sendemail-validate.sample
 ┃ ┃ ┗ 📜update.sample
 ┃ ┣ 📂info
 ┃ ┃ ┗ 📜exclude
 ┃ ┣ 📂logs
 ┃ ┃ ┣ 📂refs
 ┃ ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┃ ┗ 📂remotes
 ┃ ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📜HEAD
 ┃ ┣ 📂objects
 ┃ ┃ ┣ 📂07
 ┃ ┃ ┃ ┗ 📜a2ba0b67dff5a15f2da95fde0aa5bcb92fb653
 ┃ ┃ ┣ 📂0c
 ┃ ┃ ┃ ┗ 📜f7dc2d7f7a8ee5c0c20799b123bfe339bf8596
 ┃ ┃ ┣ 📂3c
 ┃ ┃ ┃ ┗ 📜2bde77dbdb26ac9fe3457beef761364530df41
 ┃ ┃ ┣ 📂70
 ┃ ┃ ┃ ┗ 📜2f055196bd0e7384c96ec4e8854addaaff8098
 ┃ ┃ ┣ 📂8f
 ┃ ┃ ┃ ┗ 📜8efa048fc0d74ed2e10913349cc708e38d3eb9
 ┃ ┃ ┣ 📂info
 ┃ ┃ ┗ 📂pack
 ┃ ┣ 📂refs
 ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┣ 📂remotes
 ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📂tags
 ┃ ┣ 📜COMMIT_EDITMSG
 ┃ ┣ 📜config
 ┃ ┣ 📜description
 ┃ ┣ 📜HEAD
 ┃ ┗ 📜index
 ┣ 📂templates
 ┃ ┣ 📂download
 ┃ ┗ 📜index.html
 ┗ 📜app.py
```
## Installation
Pindahkan Folder tugas-kripto1 ke dalam folder :
```sh
C:\xampp\htdocs\
```
Buka teks editor kalian lalu open folder yang sudah disimpan tadi
buka terminal atau comand prompt, pastikan mengakses folder :
```sh
C:\xampp\htdocs\tugas-kripto1
```
jalankan pemrograman dengan mengetikkan perintah berikut di terminal :
```sh
python app.py
```
akses pada browser dengan url yang ditampilkan pada terminal teks editor kalian, misalnya :
```sh
https://localhost/tugas-kripto1 atau http://127.0.0.1:5000/tugas-kripto1
```

## Credit
> kelompok 3 Kriptografi
> AL MUNAWAROH 
> RENO RIDHOI


