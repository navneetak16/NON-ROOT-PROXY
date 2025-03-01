# 🛡 MITM Proxy Server for Debugging API Requests  

A simple MITM (Man-in-the-Middle) proxy written in Python to capture, modify, and forward API requests.  
This proxy allows you to intercept API calls, inspect headers, and debug network traffic.

---

## 🚀 Features  
✅ Logs incoming and outgoing HTTP requests  
✅ Works as a proxy server on `127.0.0.1:8080`  
✅ Supports `GET`, `POST`, `PUT`, and `DELETE` requests  
✅ Preserves request headers and body for accurate forwarding  
✅ Easily configurable  

---

## 📦 Requirements  

- **Android device** with Termux installed  
- **Python 3** installed  
- **Git** for cloning the repository  
- **Internet connection** to install dependencies  

---

## 🛠 Installation & Setup  

### *NOTE* TO USE THIS SERVER YOU NEED TO REPLACE THE HOST ADDRESS IN APPLICATION WITH 'http://127.0.0.1:8080' or redirect the requests to 'http://127.0.0.1:8080' using [PROXYPIN](https://play.google.com/store/apps/details?id=com.network.proxy)

Follow these steps to set up and run the proxy server in **Termux**.

### **1️⃣ Install Termux & Update Packages**  
If you haven’t installed Termux yet, download it from:  
🔗 [F-Droid (Recommended)](https://f-droid.org/en/packages/com.termux/)  

Then, open Termux and update all packages:  
`pkg update && pkg upgrade -y`

### **2️⃣ Install Required Dependencies**  
`pkg install python git -y && pip install requests`

This installs **Python**, **Git**, and the required **requests** library.

### **3️⃣ Clone the Repository**  
If you have already uploaded the project to GitHub, clone it:  
`git clone https://github.com/navneetak16/NON-ROOT-PROXY.git && cd YOUR_REPO`

If you haven’t created a GitHub repo yet, create a new directory and initialize a repository:  
`mkdir proxy_server && cd proxy_server && git init`

### **4️⃣ Configure the Proxy Server**  
Modify the `proxy_server.py` file to ensure the correct target host. Open the file with:  
`nano proxy_server.py`

Find this line:  
`TARGET_HOST = "https://friends-dot-indus-prod-mp.el.r.appspot.com"`

and **change it to**:  
`TARGET_HOST = "www.example.com"`

Then, save and exit (Press `CTRL + X`, then `Y`, then `ENTER`).

### **5️⃣ Run the Proxy Server**  
Start the proxy with:  
`python proxy_server.py`

If everything is set up correctly, you should see:  
`MITM Proxy running on 127.0.0.1:8080`

Now, your proxy is **ready to intercept API calls**.

---

## 🔧 Configuration  

Modify `proxy_server.py` if you need to:  
- Change the **target host**  
- Log request/response details differently  
- Handle specific HTTP methods differently  

---

## 📌 Example Usage  

1️⃣ **Configure your app or device to use the proxy**  
- Set **127.0.0.1** as the **proxy server**  
- Use port **8080**  

2️⃣ **Send a request through the proxy**  
- Any API call sent through this proxy will be logged and forwarded.  

3️⃣ **Inspect the logs in Termux**  
- Check the headers, body, and responses for debugging.  

---

## 🐞 Troubleshooting  

### ❓ **I get a "Bad Gateway" (502) error**  
✅ **Fix:** Ensure the `TARGET_HOST` is correctly set (without `https://`).  

### ❓ **Python not found**  
✅ **Fix:** Install Python with:  
`pkg install python -y`

### ❓ **Cannot clone GitHub repository**  
✅ **Fix:** Run:  
`pkg install git -y`

---

## 🌎 Pushing Your Project to GitHub  

If you make changes and want to upload them to GitHub:  
`git add . && git commit -m "Updated proxy server" && git push origin main`

---

## 🤝 Contributing  

Feel free to **fork** this repository and submit **pull requests**.  

---

## 📜 License  

This project is open-source under the **MIT License**.  

---

### 🔗 **Follow for More Projects**  
GitHub: [YOUR_USERNAME](https://github.com/navneetak16)  

---
