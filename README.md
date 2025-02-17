# 🌐 SB-anyGrabber

`SB-anyGrabber` is a lightweight program built in python designed to detect and log the IP addresses of users connecting to your system via AnyDesk. This tool can be used for monitoring purposes to understand connection details in real-time. The project is created **strictly for educational purposes only** and must not be used for any malicious or unauthorized activity. 

---

## ⚡ Features
- 🕵️ **IP Address Detection**: Logs the IP address and port of users connected via AnyDesk.
- 🔍 **Real-Time Monitoring**: Continuously scans for active connections.
- 🗂️ **Logs Connection Details**: Automatically saves the information (IP, port, and process ID) to a log file.
- 🚀 **User-Friendly Output**: Displays colorful, gradient-enhanced information for easy readability.
- ❌ **Local IP Warning**: Identifies if a detected IP might be your local address.

---

## 🚀 Installation

1. Clone the repository or download the `anyGrabber.py` file:
   ```bash
   git clone https://github.com/YourUsername/anyGrabber.git
   cd anyGrabber
   ```

2. Install the required dependencies:
   ```bash
   pip install psutil
   ```

3. Run the program:
   ```bash
   python anyGrabber.py
   ```

---

## 🛠️ Usage

1. Ensure AnyDesk is running on your system.
2. Launch the script:
   ```bash
   python anyGrabber.py
   ```
3. If there are active AnyDesk connections, the tool will display their details, including:
   - IP Address
   - Port Number
   - Process ID (PID)
4. All logged details are saved to `grabbedIP.txt` for later review.

---

## 📖 Example

```bash
$ python anyGrabber.py

🌟 ANYDESK found: Listening for connections (CTRL-C to stop)

########################################
NEW CONNECTION FOUND!
!! This may be your local IP address
info:
ip -> 1.1.1.1
port -> 4896
process id -> 1234
```

The script will keep running and updating the log file until you stop it using `CTRL-C`.

---

## ⚠️ Disclaimer
This tool is intended for **educational purposes only**. The author is not responsible for any misuse of this tool. Ensure you have proper authorization when using this program and respect privacy laws in your region.

---

## 📦 Dependencies
- Python 3.8+
- psutil library

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## ✨ Contributing
Contributions are welcome! If you’d like to improve this tool:

1. Fork the repository.
2. Create a new branch (`feature/YourFeatureName`).
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 🌟 Support
If you find this project useful, consider giving it a ⭐ on GitHub. Your support inspires future updates!

---

### Made with ❤️ by Wojas
