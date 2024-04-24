import subprocess
import os

if os.name == 'nt':
    print("installing...")
    print("installed")
else:
    subprocess.run('pip3 install -r requirements.txt',shell=True)
    subprocess.run('sudo bash config/installing_help.sh',shell=True)