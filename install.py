import subprocess
import os


current_directory = os.getcwd()
# Get the current user's home directory
home_directory = os.path.expanduser('~')
desktop_directory = os.path.join(home_directory, '.local/share/applications')
desktop_file_path = os.path.join(desktop_directory, 'black_candle.desktop')

# Ensure the directory exists
os.makedirs(desktop_directory, exist_ok=True)

# Template for the .desktop file
desktop_template = f'''
[Desktop Entry]
Name=Black candle
Exec=bash -c "python3 {home_directory}/.local/black_candle/black_candle.py; bash -i"
Terminal=true
Icon={home_directory}/.local/black_candle/configs/logo.png
Type=Application
Categories=03-webapp-analysis;Utility;
'''

os_type = check_os()
if os_type == 'Windows':
    print("installing...")
    print("[\033[32m+\033[0m] installed")
elif os_type == 'Linux':
    subprocess.run('pip3 install -r requirements.txt',shell=True,check=True)
    subprocess.run('chmod +x black_candle.py', shell=True, check=True)
    subprocess.run('sudo update-desktop-database', shell=True, check=True)
    os.mkdir(f'{home_directory}/.local/black_candle')
    subprocess.run(f"mv {current_directory}/configs {home_directory}/.local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/black_candle.py {home_directory}/.local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/how_to_use_me.html {home_directory}/.local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/src {home_directory}/.local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/how_to_use_me.txt {home_directory}/.local/black_candle",shell=True)
    subprocess.run(f'sudo ln -sf {home_directory}/.local/black_candle/black_candle.py /usr/bin/black_candle', shell=True, check=True)
elif os_type == 'Darwin': #macos
    subprocess.run('',shell=True)
else:
    print("Unsupported operating system.")
    exit(1)

# the modified .desktop file
with open(desktop_file_path, 'w') as desktop_file:
    desktop_file.write(desktop_template)

# set permission on the .desktop file
os.chmod(desktop_file_path, 0o755)

print("[\033[32m+\033[0m] Installation completed successfully.")