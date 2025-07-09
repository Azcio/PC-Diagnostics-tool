from tabulate import tabulate

def generate_report(info: dict, performance: dict, diagnostics: list):
    report = "\n--- System Information ---\n"
    report += tabulate(info.items(), tablefmt="grid")

    report += "\n\n--- Performance ---\n"
    report += tabulate(performance.items(), tablefmt="grid")

    report += "\n\n--- Diagnostics ---\n"
    for diag in diagnostics:
        report += f"- {diag}\n"

    return report
