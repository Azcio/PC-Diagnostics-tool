import psutil

def get_performance():
    return {
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
        "RAM Usage": f"{psutil.virtual_memory().percent}%",
        "Disk Usage": f"{psutil.disk_usage('/').percent}%",
        "Battery": f"{psutil.sensors_battery().percent if psutil.sensors_battery() else 'N/A'}%"
    }