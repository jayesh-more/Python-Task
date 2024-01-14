import os
import platform
import psutil
import speedtest
import socket
import uuid
from screeninfo import get_monitors

def get_installed_software():
    software_list = os.popen('wmic product get name,version').read()
    return software_list

'''def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / (1024 * 1024)
    upload_speed = st.upload() / (1024 * 1024)
    return download_speed, upload_speed '''

def get_screen_resolution():
    monitors = get_monitors()
    resolutions = [(m.width, m.height) for m in monitors]
    return resolutions

def get_cpu_info():
    cpu_info = {
        'model': platform.processor(),
        'cores': psutil.cpu_count(logical=False),
        'threads': psutil.cpu_count(logical=True)
    }
    return cpu_info

def get_gpu_info():
    try:
        import GPUtil
        gpu = GPUtil.getGPUs()[0]
        gpu_info = {
            'model': gpu.name
        }
        return gpu_info
    except ImportError:
        return None

def get_ram_size():
    ram_size = psutil.virtual_memory().total / (1024 ** 3)
    return ram_size

def get_screen_size():
    # Assuming primary monitor size
    monitors = get_monitors()
    if monitors:
        primary_monitor = monitors[0]
        screen_size = f'{primary_monitor.width}x{primary_monitor.height} pixels'
        return screen_size
    else:
        return None

def get_network_info():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    ip_address = socket.gethostbyname(socket.gethostname())
    return mac_address, ip_address

def get_windows_version():
    return platform.win32_ver()

if __name__ == "__main__":
    installed_software = get_installed_software()
    # internet_speed = get_internet_speed()
    screen_resolution = get_screen_resolution()
    cpu_info = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_size = get_ram_size()
    screen_size = get_screen_size()
    mac_address, ip_address = get_network_info()
    windows_version = get_windows_version()

    print("1) Installed Software:\n", installed_software)
   #print("\nInternet Speed (Mbps):\nDownload: {:.2f}, Upload: {:.2f}".format(*internet_speed)
    print("\n3) Screen Resolution:\n", screen_resolution)
    print("\n4) CPU Info:\n", cpu_info)
    print("\n5) GPU Info:\n", gpu_info)
    print("\n7) RAM Size (GB):\n", ram_size)
    print("\n8) Screen Size:\n", screen_size)
    print("\n9,10) Network Info:\nMAC Address: {}, IP Address: {}".format(mac_address, ip_address))
    print("\n11) Windows Version:\n", windows_version)
