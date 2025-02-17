import psutil
import os
import socket

# Utility function for gradient coloring
def gradient_text(text, color_start="255;165;0", color_end="255;69;0"):
    """Apply a gradient effect to text using RGB values."""
    result = ""
    length = len(text)
    r1, g1, b1 = [int(x) for x in color_start.split(";")]
    r2, g2, b2 = [int(x) for x in color_end.split(";")]

    for i, char in enumerate(text):
        # Calculate intermediate color
        ratio = i / (length - 1) if length > 1 else 0
        r = int(r1 + ratio * (r2 - r1))
        g = int(g1 + ratio * (g2 - g1))
        b = int(b1 + ratio * (b2 - b1))
        result += f"\033[38;2;{r};{g};{b}m{char}"
    return result + "\033[0m"  # Reset at the end


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

IPAddr = IPAddr.split(".")
IPAddr = IPAddr[0] + "." + IPAddr[1]

# Banner with gradient
print(gradient_text("""
  ██████  ▄▄▄▄    ▄▄▄       ███▄    █▓██   ██▓  ▄████  ██▀███   ▄▄▄       ▄▄▄▄    ▄▄▄▄   ▓█████  ██▀███  
▒██    ▒ ▓█████▄ ▒████▄     ██ ▀█   █ ▒██  ██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄ ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒ ▒██ ██░▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒ ▄██▒██▒ ▄██▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒ ░ ▐██▓░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░█▀  ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░ ░ ██▒▓░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓░▓█  ▀█▓░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ██▒▒▒  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░▓██ ░▒░   ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░▒░▒   ░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ░    ░   ░   ▒      ░   ░ ░ ▒ ▒ ░░  ░ ░   ░   ░░   ░   ░   ▒    ░    ░  ░    ░    ░     ░░   ░ 
      ░   ░            ░  ░         ░ ░ ░           ░    ░           ░  ░ ░       ░         ░  ░   ░     
               ░                      ░ ░                                      ░       ░                        
> python anydesk ip grabber
> made with ❤️ by W0jas
""", "255;165;0", "255;69;0"))

logfile = "grabbedIP.txt"
process_name = "anydesk"
pidlist = list()
hostlist = list()

print(gradient_text("Looking for AnyDesk...", "255;200;0", "255;69;0"))

for proc in psutil.process_iter():
    if process_name in proc.name().lower():
        pidlist.append(proc.pid)

if len(pidlist) == 0:
    print(gradient_text("ERROR: No open AnyDesk found.", "255;69;0", "255;0;0"))
    exit()
else:
    print(gradient_text("ANYDESK found: Listening for connections (CTRL-C to stop)", "255;165;0", "255;69;0"))

while True:
    try:
        for x in os.popen("netstat -n -a -o").read().split("\n"):
            for y in pidlist:
                if str(y) in x and ("SYN_SENT" in x or "ESTABILISHED" in x) and ("UDP" not in x):
                    hostandport = x.split(":")
                    host = hostandport[1].split(" ")[-1]
                    port = hostandport[2].split(" ")[0]
                    if host not in hostlist:
                        hostlist.append(host)
                        print("\n" + gradient_text("#" * 40, "255;165;0", "255;69;0"))
                        flag = ""
                        if host.startswith(IPAddr):
                            flag = gradient_text("!! This may be your local IP address", "255;200;0", "255;69;0")
                        print(gradient_text(f"""NEW CONNECTION FOUND!
{flag}
info:
ip -> {host}
port -> {port}

process id -> {str(y)}""", "255;165;0", "255;69;0"))
                        with open(logfile, "a") as f:
                            f.write("INFO:\nip: " + host + "\nport: " + port + "\nPID: " + str(y) + "\n\n")
    except KeyboardInterrupt:
        print(gradient_text("\nCTRL+C detected, exiting...", "255;69;0", "255;0;0"))
        exit()
