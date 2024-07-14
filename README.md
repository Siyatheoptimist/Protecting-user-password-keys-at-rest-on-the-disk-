# Protecting user password keys at rest (on the disk)
<h1>Project Description</h1>
This project focuses on developing an authorization application to protect password keys at rest, implemented in Python. The application provides robust encryption for user-selected files or directories using AES-256 encryption with a randomly generated File Encryption Key (FEK). 
<h2>The features of the application include:</h2>
1.<b>Encryption</b>: Encrypt a user-chosen file or directory with AES-256 using a randomly generated File Encryption Key (FEK).
<br>
2.<b>Key Storage</b>: Securely store the random key in a file protected by a user passphrase.
<br>
3.<b>Security</b>: Ensure neither the user passphrase nor the random key is stored in plain text.
<br>
4.<b>Decryption</b>: Authenticate the user passphrase to retrieve and decrypt the file using the File Encryption Key.
