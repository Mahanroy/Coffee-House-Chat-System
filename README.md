<div align="center">

<img src="https://img.shields.io/badge/-%E2%98%95%20Coffee%20House-6F4E37?style=for-the-badge&logoColor=white" height="40"/>

# Coffee House Chat System

**A real-time chat web application brewed with Flask & WebSockets**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Flask-SocketIO](https://img.shields.io/badge/Flask--SocketIO-5.3.6-FF6B35?style=flat-square)](https://flask-socketio.readthedocs.io)
[![Eventlet](https://img.shields.io/badge/Eventlet-0.36.1-4CAF50?style=flat-square)](https://eventlet.net)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br/>

> ☕ *A cozy corner of the internet where conversations flow as smoothly as your morning brew.*

<br/>

[Features](#-features) · [Tech Stack](#-tech-stack) · [Getting Started](#-getting-started) · [Project Structure](#-project-structure) · [Screenshots](#-screenshots) · [Contributing](#-contributing)

---

</div>

<br/>

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ **Real-Time Messaging** | Instant bidirectional communication powered by WebSockets |
| 🏠 **Chat Rooms** | Join or create rooms to keep conversations organized |
| 👤 **Usernames** | Set a display name before entering the chat |
| 📡 **Live Presence** | See when users join and leave the room |
| 🎨 **Custom UI** | A warm, coffee-themed interface built from scratch |
| 🌐 **Browser-Based** | No installation needed for users — just open and chat |

<br/>

## 🛠 Tech Stack

```
Backend      →   Python · Flask · Flask-SocketIO · Eventlet
Frontend     →   HTML · CSS · JavaScript · Socket.IO (client)
Transport    →   WebSockets (with long-polling fallback)
```

<br/>

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.8+** and **pip** installed on your machine.

```bash
python --version   # Should be 3.8 or higher
pip --version
```

---

### 1 — Clone the Repository

```bash
git clone https://github.com/Mahanroy/Coffee-House-Chat-System.git
cd Coffee-House-Chat-System
```

---

### 2 — Create a Virtual Environment *(recommended)*

```bash
# Create
python -m venv venv

# Activate (macOS / Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

---

### 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:

```
Flask==3.0.3
Flask-SocketIO==5.3.6
eventlet==0.36.1
```

---

### 4 — Run the App

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

> 💡 To test real-time chat, open **multiple browser tabs or windows** and start messaging!

<br/>

## 📁 Project Structure

```
Coffee-House-Chat-System/
│
├── app.py                  # Main Flask application & SocketIO event handlers
├── requirements.txt        # Python dependencies
│
├── templates/              # Jinja2 HTML templates
│   └── ...                 # (index, chat room pages, etc.)
│
├── static/                 # Frontend assets
│   ├── css/                # Stylesheets
│   ├── js/                 # Client-side JavaScript
│   └── ...
│
└── Screen Shorts/          # App screenshots & previews
```

<br/>

## 📸 Screenshots

> Check the [`Screen Shorts/`](./Screen%20Shorts/) folder for visual previews of the application.

<br/>

## 🔌 How It Works

```
User opens browser
      │
      ▼
Flask serves the HTML page
      │
      ▼
Client connects via Socket.IO
      │
      ▼
User enters username & joins a room
      │
      ▼
Messages are emitted as WebSocket events
      │
      ▼
Flask-SocketIO broadcasts to all users in the room
      │
      ▼
All clients receive & display the message instantly
```

<br/>

## ⚙️ Configuration

By default the server runs in **debug mode** on port `5000`. You can adjust this in `app.py`:

```python
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
```

To run on a different port:

```python
socketio.run(app, debug=False, host='0.0.0.0', port=8080)
```

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

1. **Fork** the repository
2. **Create** your feature branch → `git checkout -b feature/your-feature-name`
3. **Commit** your changes → `git commit -m "Add: your feature description"`
4. **Push** to your branch → `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please keep PRs focused and descriptive. Bug reports and feature suggestions can be filed via [Issues](https://github.com/Mahanroy/Coffee-House-Chat-System/issues).

<br/>

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

<br/>

---

<div align="center">

Made with ☕ and Python by [Mahanroy](https://github.com/Mahanroy)

*If this project helped you, consider leaving a ⭐ on GitHub!*

</div>
