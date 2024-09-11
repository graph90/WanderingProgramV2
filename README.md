# WanderingProgramV2

## Overview

WanderingProgramV2 is a Python script designed to explore the concept of a self replicating and self mutating program with enhanced stealth and persistence features. This script continuously moves around different directories in Linux, replicates itself, mutates its own code, and introduces decoys to avoid detection. It demonstrates a persistent and evolving process within a file system.

## Features

- **Encryption/Decryption:** Uses XOR encryption to secure its files.
- **File Replication:** Copies itself to various directories and encrypts the copies.
- **Code Mutation:** Randomly alters its own code to introduce variations.
- **Directory Selection:** Dynamically chooses directories based on the current context and avoids directories with similar programs.
- **Decoy Creation:** Generates decoy files to mislead potential detection systems.
- **Self Preservation:** Creates backups of its original file and encrypts it to protect against tampering.
- **Self Repair:** Restores the original file from backups if tampering is detected.
- **Background Execution:** Uses a secondary script to run the main program in the background and delete the secondary script itself.

## How It Works

1. **Encryption/Decryption:** Encrypts or decrypts files using XOR with a generated key.
2. **File Replication:** Copies itself to a new location, encrypts the copy, and appends content to `.txt` files in the target directory.
3. **Code Mutation:** Applies random mutations to its code to alter its behavior and avoid detection.
4. **Decoy Creation:** Creates decoy files to distract from the main program's activity.
5. **Self Preservation:** Backs up and encrypts the original file to protect against tampering.
6. **Self Repair:** Restores the original file from a backup if tampering is detected.
7. **Background Execution:** Uses `trigger.py` to execute the main program in the background and then deletes itself.

## Running the Program

### Prerequisites

- Python 3.x
- A virtual machine (VM) environment for testing

### Setup

1. **Create a VM:**
   - Use VirtualBox or VMware.
   - Install a Linux based OS (Ubuntu) for easier directory management.

2. **Run the Main Program:**
   - Ensure `wander2.py` and `trigger.py` are in the same directory.
   - Execute `trigger.py` to start the main program in the background and handle self-deletion.

### Safety

This program is for experimental purposes only.
