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
Exec=bash -c "python3 {home_directory}/Desktop/black-candle/black_candle.py; bash -i"
Terminal=true
Icon={home_directory}/Desktop/black-candle/configs/logo.png
Type=Application
Categories=Utility
'''


if os.name == 'nt':
    print("installing...")
    print("installed")
else:
    subprocess.run('pip3 install -r requirements.txt',shell=True,check=True)
    subprocess.run(f'sudo ln -sf {current_directory}/black_candle.py /usr/bin/black_candle', shell=True, check=True)
    subprocess.run('chmod +x black_candle.py', shell=True, check=True)
    subprocess.run('sudo update-desktop-database', shell=True, check=True)

    # the modified .desktop file
    with open(desktop_file_path, 'w') as desktop_file:
        desktop_file.write(desktop_template)

    # set permission on the .desktop file
    os.chmod(desktop_file_path, 0o755)

    print("Installation completed successfully.")