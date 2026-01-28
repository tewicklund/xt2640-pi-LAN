# Usage:
1. SSH into pi with this script  
2. Install tmux if haven't already  
`sudo apt install tmux`  
3. Run  
`tmux new -s test-name-here`  
4. Start script  
`python3 main.py`  
5. Detach terminal with Ctrl+B then D  
6. To view screen if SSH fails  
`tmux attach -t test-name-here`
