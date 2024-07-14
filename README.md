# Protecting User Password Keys at Rest (on the Disk)

## Project Overview

This project focuses on developing an authorization application in Python to protect password keys at rest. The application encrypts user-chosen files or directories using AES-256 encryption and a randomly generated File Encryption Key (FEK). It securely stores the FEK in a file, protected by a user passphrase. The application ensures that neither the user passphrase nor the FEK is stored in plain text. Upon successful authentication of the user passphrase, the application retrieves and decrypts the file using the FEK.

## Features

1. **Encryption**: Encrypt a user-chosen file or directory with AES-256 using a randomly generated File Encryption Key (FEK).

2. **Key Storage**: Securely store the random key in a file protected by a user passphrase.

3. **Security**: Ensure neither the user passphrase nor the random key is stored in plain text.

4. **Decryption**: Authenticate the user passphrase to retrieve and decrypt the file using the File Encryption Key.

## Prerequisites

- Knowledge of Linux File System Operations
- Understanding of Crypto Algorithms
- Proficiency in programming languages suited for system software, such as Python

## Infrastructure Requirements

### Hardware

- Any x86 based Desktop or Server with Linux

## Project Files

- `project.py`: The main Python script that implements the encryption, key storage, and decryption functionalities.

## Project Outputs

1. Application workflow.
2. High-level algorithm.
3. Justification for various crypto algorithms used.
4. Type of open source and system routines used for various tasks.
5. Test plan for testing various simple and corner cases.
6. Actual source code with appropriate comments archived in GitHub.

## Learning Outcomes

1. Partitioning the high-level problem statement into workflow and smaller independent tasks.
2. Understanding different crypto algorithms and usage models.

## Usage

### Encrypting a File or Directory

1. **Run the Script**: 
    ```sh
    python project.py
    ```

2. **Choose the Encryption Option**: Follow the on-screen prompts to select the option for encrypting a file or directory.

3. **Select the File/Directory**: Provide the path to the file or directory you wish to encrypt.

4. **Enter a Passphrase**: Input a passphrase that will be used to protect the encryption key.

5. **Complete Encryption**: The application will encrypt the selected file or directory and store the encryption key securely.

### Decrypting a File or Directory

1. **Run the Script**: 
    ```sh
    python project.py
    ```

2. **Choose the Decryption Option**: Follow the on-screen prompts to select the option for decrypting a file or directory.

3. **Select the File/Directory**: Provide the path to the encrypted file or directory.

4. **Enter the Passphrase**: Input the passphrase used during the encryption process.

5. **Complete Decryption**: The application will authenticate the passphrase, retrieve the encryption key, and decrypt the file or directory.

## Contribution

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.

---

Feel free to modify this `README.md` to suit your specific needs and include additional information if necessary.
