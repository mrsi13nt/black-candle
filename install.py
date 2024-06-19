import subprocess
import platform
import os

def is_wsl():
    try:
        with open('/proc/version', 'r') as file:
            version_info = file.read().lower()
            if 'microsoft' in version_info or 'wsl' in version_info:
                return True
    except FileNotFoundError:
        pass
    return False

def has_gui():
    display_var = os.getenv('DISPLAY')
    if display_var:
        return True
    
    # Check if any common GUI package is installed
    gui_packages = ['gnome-session', 'kde-plasma']
    for package in gui_packages:
        if subprocess.call(['which', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            return True
    
    return False



os_type = check_os() # check what OS that user use
if os_type == 'Windows':
    print("installing...")
elif os_type == 'Linux':
    if is_wsl(): # this all broken until we understand WSL OS files
        if has_gui():
            current_directory = os.getcwd()
            # Get the current user's home directory
            home_directory = os.path.expanduser('~')

            # installing process 
            subprocess.run('pip3 install -r requirements.txt',shell=True,check=True)
            subprocess.run('chmod +x black_candle.py', shell=True, check=True)
            os.mkdir(f'{home_directory}/.local/black_candle')
            subprocess.run(f"mv {current_directory}/configs {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/black_candle.py {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/how_to_use_me.html {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/src {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/how_to_use_me.txt {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f'sudo ln -sf {home_directory}/.local/black_candle/black_candle.py /usr/bin/black_candle', shell=True, check=True)
        else:
            current_directory = os.getcwd()
            # Get the current user's home directory
            home_directory = os.path.expanduser('~')

            # installing process 
            subprocess.run('pip3 install -r requirements.txt',shell=True,check=True)
            subprocess.run('chmod +x black_candle.py', shell=True, check=True)
            os.mkdir(f'{home_directory}/.local/black_candle')
            subprocess.run(f"mv {current_directory}/configs {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/black_candle.py {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/how_to_use_me.html {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/src {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f"mv {current_directory}/how_to_use_me.txt {home_directory}/.local/black_candle",shell=True)
            subprocess.run(f'sudo ln -sf {home_directory}/.local/black_candle/black_candle.py /usr/bin/black_candle', shell=True, check=True)
    else: # normal Linux
        if has_gui():
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

            # installing process 
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
            # the modified .desktop file
            with open(desktop_file_path, 'w') as desktop_file:
                desktop_file.write(desktop_template)

            # set permission on the .desktop file
            os.chmod(desktop_file_path, 0o755)
        else: # normal linux without GUI
            current_directory = os.getcwd()
            # Get the current user's home directory
            home_directory = os.path.expanduser('~')

            # installing process 
            subprocess.run('pip3 install -r requirements.txt',shell=True,check=True)
            subprocess.run('chmod +x black_candle.py', shell=True, check=True)
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



print("[\033[32m+\033[0m] Installation completed successfully.")