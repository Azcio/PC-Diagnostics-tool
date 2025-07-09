import platform
import psutil
import cpuinfo
import GPUtil

def get_system_info():
    info = {}
    info["OS"] = platform.system() + " " + platform.release()
    info["CPU"] = cpuinfo.get_cpu_info()['brand_raw']
    info["RAM"] = f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
    info["Disk"] = f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB"
    
    gpus = GPUtil.getGPUs()
    if gpus:
        info["GPU"] = gpus[0].name
    else:
        info["GPU"] = "No GPU Detected"

    return info
