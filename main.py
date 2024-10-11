import os
import subprocess

# Define ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Colorful banner
banner = f"""{GREEN}
  __  __      _    _                       
 |  \/  |    | |  | |                      
 | \  / |_ __| |__| | __ _ ___  __ _ _ __  
 | |\/| | '__|  __  |/ _` / __|/ _` | '_ \ 
 | |  | | |  | |  | | (_| \__ \ (_| | | | |
 |_|  |_|_|  |_|  |_|\__,_|___/\__,_|_| |_|
                                  
{RESET}"""

# Colorful info
info = f"""{YELLOW}
--------------------------------------------------------
 𝐀ᴜᴛʜᴏʀ ➜ {CYAN}𝐌ʀ.𝐇ᴀsᴀɴ{YELLOW}
 𝐆ɪᴛʜᴜʙ ➜ {CYAN}@MrHasan1337{YELLOW}
 𝐓ᴇʟᴇɢʀᴀᴍ ➜ {CYAN}@Its_Me_Hasan{YELLOW}
 𝐓ᴏᴏʟs ➜ {CYAN}Blum Bot{YELLOW}
--------------------------------------------------------{RESET}
"""

os.system("clear")
print(banner)
print(info)

auth_token = input(f"{MAGENTA}𝐄ɴᴛᴇʀ 𝐘ᴏᴜʀ 𝐐ᴜᴇʀʏ 𝐈ᴅ ➜ {RESET}")

# Step 2: Delete the old query_id.txt file if it exists
file_path = 'data.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{GREEN}----------------------------------------------------------{RESET}")
else:
    print(f"{YELLOW}does not exist, creating a new one.{RESET}")

# Step 3: Save the new auth token into query_id.txt
with open(file_path, 'w') as file:
    file.write(auth_token)
    print(f"{GREEN}----------------------------------------------------------{RESET}")

# Step 4: Run memefi.py
try:
    subprocess.run(['python', 'bot.py'])
except Exception as e:
    print(f"{RED}Failed to run bot.py: {e}{RESET}")
