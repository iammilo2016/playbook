import subprocess

def run_ansible_playbook(playbook_path):
    try:
        # Running the Ansible playbook
        subprocess.run(["ansible-playbook", "-i", "/home/user/Assignment_5/inventory", playbook_path], check=True)
        print("Playbook executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    playbook_path = "/home/user/Assignment_5/Playbook_1.yml"
    run_ansible_playbook(playbook_path)
