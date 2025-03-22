import psutil
import platform
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def show_device_info():
    # Display hacker theme title with ASCII Art
    ascii_art = '''
    ███    ██ ███████  ██████  ██████   ██████   ██████  ████████  ████████ 
    ████   ██ ██      ██    ██ ██   ██ ██    ██ ██   ██    ██    ██    ██  
    ██ ██  ██ █████   ██    ██ ██████  ██    ██ ██   ██    ██    ████████  
    ██  ██ ██ ██      ██    ██ ██   ██ ██    ██ ██   ██    ██    ██    ██  
    ██   ████ ███████  ██████  ██   ██  ██████  ██████     ██    ██    ██  
    '''
    
    print(Fore.GREEN + ascii_art)
    print(Fore.CYAN + Style.BRIGHT + "Device Information - Hacker Mode")
    print(Fore.YELLOW + "=" * 50)

    # Basic System Info
    print(Fore.RED + "System Information".center(50, "-"))
    print(f"{Fore.WHITE}System: {Fore.GREEN}{platform.system()}")
    print(f"{Fore.WHITE}Node Name: {Fore.GREEN}{platform.node()}")
    print(f"{Fore.WHITE}Release: {Fore.GREEN}{platform.release()}")
    print(f"{Fore.WHITE}Version: {Fore.GREEN}{platform.version()}")
    print(f"{Fore.WHITE}Machine: {Fore.GREEN}{platform.machine()}")
    print(f"{Fore.WHITE}Processor: {Fore.GREEN}{platform.processor()}")

    # CPU Info
    print(Fore.RED + "\nCPU Info".center(50, "-"))
    print(f"{Fore.WHITE}CPU Count: {Fore.GREEN}{psutil.cpu_count(logical=False)} physical cores")
    print(f"{Fore.WHITE}Logical CPUs: {Fore.GREEN}{psutil.cpu_count(logical=True)} logical cores")
    print(f"{Fore.WHITE}CPU Usage: {Fore.GREEN}{psutil.cpu_percent(interval=1)}%")

    # Memory Info
    print(Fore.RED + "\nMemory Info".center(50, "-"))
    memory = psutil.virtual_memory()
    print(f"{Fore.WHITE}Total Memory: {Fore.GREEN}{memory.total / (1024 ** 3):.2f} GB")
    print(f"{Fore.WHITE}Available Memory: {Fore.GREEN}{memory.available / (1024 ** 3):.2f} GB")
    print(f"{Fore.WHITE}Used Memory: {Fore.GREEN}{memory.used / (1024 ** 3):.2f} GB")
    print(f"{Fore.WHITE}Memory Usage: {Fore.GREEN}{memory.percent}%")

    # Disk Info
    print(Fore.RED + "\nDisk Info".center(50, "-"))
    disk = psutil.disk_partitions()
    for partition in disk:
        print(f"{Fore.WHITE}Device: {Fore.GREEN}{partition.device}, Mount Point: {Fore.GREEN}{partition.mountpoint}, Filesystem Type: {Fore.GREEN}{partition.fstype}")
    disk_usage = psutil.disk_usage('/')
    print(f"{Fore.WHITE}Total Disk Space: {Fore.GREEN}{disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"{Fore.WHITE}Used Disk Space: {Fore.GREEN}{disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"{Fore.WHITE}Free Disk Space: {Fore.GREEN}{disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"{Fore.WHITE}Disk Usage: {Fore.GREEN}{disk_usage.percent}%")

    # Network Info
    print(Fore.RED + "\nNetwork Info".center(50, "-"))
    net = psutil.net_if_addrs()
    for interface, addresses in net.items():
        for address in addresses:
            print(f"{Fore.WHITE}Interface: {Fore.GREEN}{interface}, Address: {Fore.GREEN}{address.address}")

if __name__ == "__main__":
    show_device_info()
