import sys
import time

def loading_bar():
    chars = "#"
    total = 20
    for i in range(total + 1):
        progress = i / total * 100
        sys.stdout.write(f"\rProgress: [{chars * i}{' ' * (total - i)}] {progress:.1f}%")
        sys.stdout.flush()
        time.sleep(0.1)
