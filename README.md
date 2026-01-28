# Usage:
SSH into pi with this script
Install tmux if haven't already
  `sudo apt install tmux`
Run
  `tmux new -s test-name-here`
Start script
  `python3 main.py`
Detach terminal with Ctrl+B then D
To view screen if SSH fails
  `tmux attach -t test-name-here`
