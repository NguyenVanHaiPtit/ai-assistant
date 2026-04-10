import subprocess


def run_command(cmd: str) -> str:
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        if result.returncode != 0:
            return f"Lệnh lỗi:\n{result.stderr}"

        output = result.stdout.strip()
        return output if output else "Không có dữ liệu trả về."
    except Exception as e:
        return f"Lỗi chạy lệnh: {e}"


def get_disk() -> str:
    return run_command("wmic logicaldisk get size,freespace,caption")


def get_memory() -> str:
    return run_command("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize")


def get_process() -> str:
    return run_command("tasklist")