# AuraTimer

**A terminal Pomodoro timer with a Rich-powered UI** — track focus sessions, attach tasks, and review summaries without leaving the command line.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Rich-CLI_UI-EE6C4D?style=flat-square" alt="Rich" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-4D4D4D?style=flat-square&logo=windows-terminal&logoColor=white" alt="Platform" />
</p>

---

## Overview

AuraTimer runs classic Pomodoro cycles (work → short break → repeat) in the terminal. It uses [Rich](https://github.com/Textualize/rich) for layout, spinners, and session tables so sessions feel polished rather than a plain countdown script.

## Features

| Feature | Description |
|--------|-------------|
| **Rich terminal UI** | ASCII branding, spinners, and a cyan/magenta palette |
| **Task labels** | Name the task you are focusing on for each run |
| **Audio alert** | System chime when a session ends |
| **Session summary** | Table of total focus and break time when cycles finish |
| **Configurable** | Work duration, break length, and cycle count via CLI flags |

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt` (`rich`)

## Installation

```bash
git clone https://github.com/ShahabAhmed01/AuraTimer.git
cd AuraTimer
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

**Default session** (25 min work, 5 min break, 4 cycles):

```bash
python auratimer.py
```

**Named task:**

```bash
python auratimer.py --task "Studying DSA"
```

**Custom timings:**

```bash
python auratimer.py --work 50 --break_time 10 --cycles 3 --task "Deep work"
```

| Argument | Short | Default | Description |
|----------|-------|---------|-------------|
| `--work` | `-w` | `25` | Work session (minutes) |
| `--break_time` | `-b` | `5` | Short break (minutes) |
| `--cycles` | `-c` | `4` | Cycles before long break |
| `--task` | `-t` | — | Task label for this run |

## Project structure

```
AuraTimer/
├── auratimer.py      # Entry point
├── requirements.txt
└── README.md
```

## Author

**Shahab Ahmed** — [GitHub](https://github.com/ShahabAhmed01) · [LinkedIn](https://www.linkedin.com/in/shahabahmed01/) · [Portfolio](https://shahabahmed01.github.io)

## License

Open source for learning and portfolio use.
