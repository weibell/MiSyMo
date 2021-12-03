# MiSyMo
A Minimal System Monitor for the command-line written in Python



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


## Additional information
* Displays CPU, RAM, network and (hard) disk stats
* Makes use of [psutil](https://github.com/giampaolo/psutil) to ensure cross-platform accessible system stats