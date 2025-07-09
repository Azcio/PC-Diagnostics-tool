import psutil

def check_disk_health():
    usage = psutil.disk_usage('/')
    if usage.percent > 90:
        return "Disk almost full! Consider cleanup."
    return "Disk health looks good."

def check_memory():
    mem = psutil.virtual_memory()
    if mem.percent > 85:
        return "High RAM usage detected!"
    return "RAM usage is within normal limits."
