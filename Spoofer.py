import requests
import os
import sys
import time

VERSION = "1.5.0"
UPDATE_CHECK_URL = "https://pastebin.com/raw/YOUR_PASTE_ID"  # Replace this!

def print_colored(text, color_code=15):
    import ctypes
    h = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.SetConsoleTextAttribute(h, color_code)
    print(text)
    ctypes.windll.kernel32.SetConsoleTextAttribute(h, 15)

def check_for_update():
    try:
        response = requests.get(UPDATE_CHECK_URL, timeout=5)
        latest_version, download_url = response.text.strip().split("|")

        if latest_version != VERSION:
            print_colored("Checking for updates...", 11)
            print_colored(f"Update available: v{latest_version}", 14)

            new_code = requests.get(download_url, timeout=10).text
            script_path = os.path.realpath(sys.argv[0])

            with open(script_path, "w", encoding="utf-8") as f:
                f.write(new_code)

            print_colored("Update downloaded. Restarting...", 10)
            time.sleep(2)
            os.execl(sys.executable, sys.executable, *sys.argv)

    except Exception as e:
        print_colored(f"[!] Update check failed: {e}", 12)
        time.sleep(1)

def main():
    print_colored(f"Running version {VERSION}", 11)
    input("Press ENTER to continue...")

if __name__ == "__main__":
    check_for_update()
    main()
