# Protecting user password keys at rest (on the disk)
<h1>Project Description</h1>
<br>
This project focuses on developing an authorization application to protect password keys at rest, implemented in Python. The application provides robust encryption for user-selected files or directories using AES-256 encryption with a randomly generated File Encryption Key (FEK). The features of the application include:
Encryption: Encrypt a user-chosen file or directory with AES-256 using a randomly generated File Encryption Key (FEK).
Key Storage: Securely store the random key in a file protected by a user passphrase.
Security: Ensure neither the user passphrase nor the random key is stored in plain text.
Decryption: Authenticate the user passphrase to retrieve and decrypt the file using the File Encryption Key.
