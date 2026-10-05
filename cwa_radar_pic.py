import subprocess
import time
import random
from pathlib import Path

env = "windows" # "linux" or "windows"
year = "2026"
mm = "10" # month
dd = "05" # day
MM = range(0, 60, 10) # minute
HH = range(0, 24, 1) # hour
MM = [f"{M:02d}" for M in MM]
HH = [f"{H:02d}" for H in HH]
picpath = Path("./pic")
picpath.mkdir(exist_ok=True, parents=True)

for H in HH:
    for M in MM:
        webpath = f"https://www.cwa.gov.tw/Data/radar/"
        filename = f"CV1_TW_3600_{year}{mm}{dd}{H}{M}.png"
        if env == "windows":
            commend = ["powershell", "-Command", "Invoke-WebRequest", "-Uri", f"{webpath}{filename}", "-OutFile", f"{str(picpath / filename)}"]
        elif env == "linux":
            commend = ["wget", "-P", str(picpath), f"{webpath}{filename}"]
        subprocess.run(commend)
        time.sleep(1 + random.randrange(50)/100) # don't touch this line