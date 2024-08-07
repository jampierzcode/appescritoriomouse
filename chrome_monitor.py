import psutil

def check_chrome_tabs():
    chrome_processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'chrome.exe' in p.info['name']]
    for process in chrome_processes:
        print(f"Chrome proceso encontrado: PID={process['pid']} {process}")
        # Aquí puedes agregar lógica adicional para verificar el estado de la pestaña.
