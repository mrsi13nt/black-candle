import subprocess
import platform
import os
from win32com.client import Dispatch
import winshell
import shutil

# ---------------- windows ---------------------
def create_batch_file(script_path, batch_file_dir):
    # Create the batch file content
    batch_file_content = f'''@echo off
    python "{script_path}" %*
    '''

    # Ensure the batch file directory exists
    os.makedirs(batch_file_dir, exist_ok=True)

    # Write the batch file
    batch_file_path = os.path.join(batch_file_dir, 'black_candle.bat')
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(batch_file_content)

    print(f"Batch file created at: {batch_file_path}")
    return batch_file_path

def create_shortcut(batch_file_path, shortcut_path, icon_path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = batch_file_path
    shortcut.WorkingDirectory = os.path.dirname(batch_file_path)
    shortcut.IconLocation = icon_path
    shortcut.save()


# --------------- Linux -------------------
# check if OS is WSL or not
def is_wsl():
    try:
        with open('/proc/version', 'r') as file:
            version_info = file.read().lower()
            if 'microsoft' in version_info or 'wsl' in version_info:
                return True
    except FileNotFoundError:
        pass
    return False

# check if OS have GUI or not
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

# ----------- macOS -----------------    
def create_applescript(script_path, app_path):
    # AppleScript content to run the Python script
    applescript_content = f'''do shell script "python3 {script_path}"'''

    # Ensure the application directory exists
    os.makedirs(app_path, exist_ok=True)

    # Write the AppleScript
    applescript_file = os.path.join(app_path, 'black_candle.scpt')
    with open(applescript_file, 'w') as f:
        f.write(applescript_content)

    # Convert the script to an application
    os.system(f"osacompile -o {app_path} {applescript_file}")



# check what OS that user use
os_type = check_os()
if os_type == 'Windows':
    print("installing...")
    current_path = os.getcwd()
    
    # Path to your Python script
    script_path = fr'{current_path}\black_candle.py'

    # Directory to place the batch file
    batch_file_dir = fr'{current_path}'

    # Path to your icon file (.ico)
    icon_path = fr'{current_path}\configs\icon.ico'

    # Path to place the shortcut
    shortcut_path = os.path.join(winshell.desktop(), 'black_candle.lnk')

    # Create the batch file
    batch_file_path = create_batch_file(script_path, batch_file_dir)

    # Create the shortcut with custom icon
    create_shortcut(batch_file_path, shortcut_path, icon_path)

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
            subprocess.run(f'sudo ln -sf {home_directory}/.local/black_candle/black_candle.py /usr/bin/black_candle', shell=True, check=True)


elif os_type == 'Darwin': #macos
    subprocess.run('pip3 install -r requirements.txt',shell=True,check=True)
    current_directory = os.getcwd()
    # Get the current user's home directory
    home_directory = os.path.expanduser('~')
    subprocess.run('chmod +x black_candle.py', shell=True, check=True)
    os.mkdir(f'/usr/local/black_candle')
    subprocess.run(f"mv {current_directory}/configs /usr/local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/black_candle.py /usr/local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/how_to_use_me.html /usr/local/black_candle",shell=True)
    subprocess.run(f"mv {current_directory}/src /usr/local/black_candle",shell=True)
    subprocess.run(f'sudo ln -sf /usr/local/black_candle/black_candle.py /usr/local/bin/black_candle', shell=True, check=True)
    # Path to your Python script
    script_path = f'/usr/local/black_candle/black_candle.py'

    # Path to place the AppleScript application
    app_path = os.path.expanduser('~/Applications/black_candle.app')

    # Create the AppleScript application
    create_applescript(script_path, app_path)
else:
    print("Unsupported operating system.")
    exit(1)



print("[\033[32m+\033[0m] Installation completed successfully.")