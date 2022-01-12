# basic-fit_autobooked

This repository is a booking automation for my favorite gym "Basic-fit".
Powered by Selenium (python3)
Using Firefox, and customize for my personal gym club

## Prerequisites
### INSTALLATION PYTHON3 ET PIP
```
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 --version
```


### INSTALLATION SELENIUM
```
python3 -m pip install selenium
```

### INSTALLATION DRIVER FIREFOX
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xf geckodriver-v0.30.0-linux64.tar.gz
cp geckodriver /usr/bin/
cp geckodriver /usr/local/bin/
rm -rf geckodriver-v0.30.0-linux64.tar.gz
rm -rf geckodriver
```

## How to 

- Clone this repository
- Create the file variables.txt at the root of the repository, and add your login and reservation schedule. (follow the example "exvariables.txt")
```
python3 main.py -v
```
