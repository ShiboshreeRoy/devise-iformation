# Device Info - Hacker Mode

This Python script displays detailed device information such as system, CPU, memory, disk, and network stats in a fun, "hacker theme" style. The script utilizes ASCII art, color-coded output, and a table-like structure for a visually appealing display.

## Features

- **System Info**: Shows OS, release version, processor, and machine architecture.
- **CPU Info**: Displays the number of physical and logical CPU cores, along with current CPU usage.
- **Memory Info**: Displays total, available, used memory, and memory usage percentage.
- **Disk Info**: Lists disk partitions, total disk space, used space, free space, and disk usage percentage.
- **Network Info**: Lists network interfaces and their associated addresses.

## Requirements

- Python 3.x
- `psutil` library for system monitoring
- `colorama` library for color output in the terminal

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shiboshreeroy/device-info.git
   cd device-info
   ```

2. Install the required libraries:

   ```bash
   pip install psutil colorama
   ```

## Usage

To run the script and see the device information with the hacker theme:

```bash
python device.py
```

## Example Output

```
    ███    ██ ███████  ██████  ██████   ██████   ██████  ████████  ████████ 
    ████   ██ ██      ██    ██ ██   ██ ██    ██ ██   ██    ██    ██    ██  
    ██ ██  ██ █████   ██    ██ ██████  ██    ██ ██   ██    ██    ████████  
    ██  ██ ██ ██      ██    ██ ██   ██ ██    ██ ██   ██    ██    ██    ██  
    ██   ████ ███████  ██████  ██   ██  ██████  ██████     ██    ██    ██  

Device Information - Hacker Mode
==================================================
--------------------------System Information---------------------------
System: Windows
Node Name: DESKTOP-XXXX
Release: 10
Version: 10.0.19045
Machine: AMD64
Processor: Intel64 Family 6 Model 158 Stepping 10

--------------------------CPU Info---------------------------
CPU Count: 4 physical cores
Logical CPUs: 8 logical cores
CPU Usage: 12%

--------------------------Memory Info---------------------------
Total Memory: 15.92 GB
Available Memory: 7.91 GB
Used Memory: 6.45 GB
Memory Usage: 42%

--------------------------Disk Info---------------------------
Device: C:, Mount Point: C:\, Filesystem Type: NTFS
Total Disk Space: 232.98 GB
Used Disk Space: 120.05 GB
Free Disk Space: 112.93 GB
Disk Usage: 51%

--------------------------Network Info---------------------------
Interface: Ethernet, Address: 192.168.1.2
Interface: Wi-Fi, Address: 192.168.0.2
```

## Customization

- You can modify the script to add or remove system information.
- Customize the ASCII art to change the theme.
- Adjust the color scheme by editing the color codes in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [Shiboshree Roy](https://github.com/shiboshreeroy)



