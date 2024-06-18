import platform
import subprocess

def get_active_connections():
    system = platform.system()
    if system == 'Windows':
        command = 'netstat -an'
    elif system in ('Linux', 'Darwin'):
        command = 'netstat -an'
    else:
        raise NotImplementedError(f'Unsupported OS: {system}')

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    connections = result.stdout.splitlines()
    return connections
