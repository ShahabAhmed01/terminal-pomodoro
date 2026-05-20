<div align="center">
  <h1>🍅 Terminal Pomodoro</h1>
  <p><i>A beautiful, minimalist Pomodoro timer for your terminal.</i></p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Terminal Badge"/>
  
</div>

<br>

A lightweight, elegant command-line interface (CLI) Pomodoro timer built with Python and [Rich](https://github.com/Textualize/rich). Keep your focus sessions productive without leaving your terminal.

## ✨ Features
- **Sleek UI:** Beautiful terminal progress bars, spinners, and colors.
- **Customizable:** Easily change work, short break, and long break durations.
- **Cross-Platform:** Works on Windows, macOS, and Linux terminals.
- **Zero Distractions:** No notifications, just a clean timer in your workspace.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShahabAhmed01/terminal-pomodoro.git
   cd terminal-pomodoro
   ```

2. **Install dependencies:**
   *(It is recommended to use a virtual environment)*
   ```bash
   pip install -r requirements.txt
   ```

## ⏱️ Usage

Run the timer with default settings (25m work, 5m break, 4 cycles):
```bash
python pomodoro.py
```

### Custom Durations
You can pass arguments to customize your workflow:
```bash
python pomodoro.py --work 50 --break_time 10 --cycles 3
```

| Argument | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--work` | `-w` | Work session duration (minutes) | `25` |
| `--break_time` | `-b` | Short break duration (minutes) | `5` |
| `--cycles` | `-c` | Number of cycles before a long break | `4` |

---
<div align="center">
  <i>Stay focused.</i>
</div>