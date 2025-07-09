from diagnostics.system_info import get_system_info
from diagnostics.performance import get_performance
from diagnostics.hardware_check import check_disk_health, check_memory
from reports.report_generator import generate_report

def main():
    print("Starting system diagnostics...")

    sys_info = get_system_info()
    print(f"System info: {sys_info}")

    perf = get_performance()
    print(f"Performance info: {perf}")

    disk_health = check_disk_health()
    print(f"Disk health: {disk_health}")

    memory_health = check_memory()
    print(f"Memory health: {memory_health}")

    diagnostics = [disk_health, memory_health]

    report = generate_report(sys_info, perf, diagnostics)
    print("Generated report:")
    print(report)

    with open("system_report.txt", "w") as f:
        f.write(report)

    input("Diagnostics complete. Press Enter to exit.")

if __name__ == "__main__":
    main()