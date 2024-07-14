# Protecting user password keys at rest (on the disk)
<h1>Project Overview</h1>
This project focuses on developing an authorization application in Python to protect password keys at rest. The application encrypts user-chosen files or directories using AES-256 encryption and a randomly generated File Encryption Key (FEK). It securely stores the FEK in a file, protected by a user passphrase. The application ensures that neither the user passphrase nor the FEK is stored in plain text. Upon successful authentication of the user passphrase, the application retrieves and decrypts the file using the FEK.
<h1>Features</h1>

1. <b>Encryption</b>: Encrypt a user-chosen file or directory with AES-256 using a randomly generated File Encryption Key (FEK).

2. <b>Key Storage</b>: Securely store the random key in a file protected by a user passphrase.
<br>

3. <b>Security</b>: Ensure neither the user passphrase nor the random key is stored in plain text.
<br>

4. <b>Decryption</b>: Authenticate the user passphrase to retrieve and decrypt the file using the File Encryption Key.
<h1>Prerequisites</h1>

-Knowledge of Linux File System Operations
<br>

-Understanding of Crypto Algorithms
<br>

-Proficiency in programming languages suited for system software, such as Python
