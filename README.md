<div align="center">
  <h1>✨ AuraTimer ✨</h1>
  <p><i>A premium, highly aesthetic Pomodoro timer for your terminal.</i></p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Terminal Badge"/>
  
</div>

<br>

**AuraTimer** elevates your focus sessions. Built with Python and [Rich](https://github.com/Textualize/rich), it provides a deeply immersive, distraction-free environment right inside your command line.

## 🌟 Premium Features
- **Aesthetic UI:** Beautiful ASCII art, smooth spinner animations, and carefully curated cyan/magenta color palettes.
- **Task Tracking:** Assign a specific task to your timer and stay locked in.
- **Audio Alerts:** Plays a soft system chime when a session completes, so you can look away from the terminal.
- **Session Summaries:** Automatically generates a rich data table detailing your total focus and break times when you finish your cycles.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShahabAhmed01/AuraTimer.git
   cd AuraTimer
   ```

2. **Install dependencies:**
   *(It is recommended to use a virtual environment)*
   ```bash
   pip install -r requirements.txt
   ```

## ⏱️ Usage

Run the timer with default settings (25m work, 5m break, 4 cycles):
```bash
python auratimer.py
```

### Track a Specific Task
```bash
python auratimer.py --task "Building a React App"
```

### Custom Durations
You can pass arguments to customize your workflow:
```bash
python auratimer.py --work 50 --break_time 10 --cycles 3 --task "Deep Work"
```

| Argument | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--work` | `-w` | Work session duration (minutes) | `25` |
| `--break_time` | `-b` | Short break duration (minutes) | `5` |
| `--cycles` | `-c` | Number of cycles before a long break | `4` |
| `--task` | `-t` | Name of the task you are focusing on | `None` |

---
<div align="center">
  <i>Cultivate your focus. Protect your aura.</i>
</div>