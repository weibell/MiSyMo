# MiSyMo
A Minimalistic System Monitor for the command-line written in Python

[![asciicast](https://asciinema.org/a/45cAx7ANMymeQi6WFSsRBn86X.svg)](https://asciinema.org/a/45cAx7ANMymeQi6WFSsRBn86X)


## Example usage

Setup:
```bash
git clone https://github.com/weibell/MiSyMo
cd MiSyMo/
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

Usage:
```bash
cd MiSyMo/
source venv/bin/activate
python3 misymo.py
```

Help:
```bash
python3 misymo.py --help
```
```
usage: misymo.py [-h] [-c] [-i {[0.1,30]}]

optional arguments:
  -h, --help            show this help message and exit
  -c, --continuous      do not re-use the same line as output (default: disabled)
  -i {[0.1,30]}, --interval {[0.1,30]}
                        update interval in seconds, between 0.1 and 30 (default: 1.0)
```

## Additional information
* Displays CPU, RAM, network and (hard) disk stats
* Default setings: update every second, non-continuous output (print output in same line = do not show history)
* Makes use of [psutil](https://github.com/giampaolo/psutil) to ensure cross-platform accessible system stats