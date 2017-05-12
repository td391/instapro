# instapro
professional instagram tool for developers 

Hi everyone. I tried to make an perfect instagram tool for developers and not the alpha version of this script has been released and i hope i will find interested developers to help me with it. I appreciate any help.

If you are not fluent with python it would be hard enough to use this scripts because there are no ready-to-go examples or clear documentation. 

The examples of usage you can find in examples folder. I recommend you to look in _notebooks/_ folder.


## Installation
Modify `instabot/config.py` as appropriate and execute
```
mkdir instabot/users 
virtualenv-3.5 venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
jupyter nbextension enable --py --sys-prefix widgetsnbextension
jupyter notebook
```

## Tests (working only for initial user)
```
python -m unittest test.py
```
