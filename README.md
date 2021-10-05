# OpenSeat

OpenSeat is a web scraper that searches for a class opening on McGill's Visual Schedule Builder website (VSB) and notifies the user by email/text when a seat for a specified class becomes available.

## Requirements

- Python 3.7
- [Selenium](https://selenium-python.readthedocs.io/)
- [Chrome WebDriver](https://chromedriver.chromium.org/downloads) (must match your Google Chrome version)
- A Proxy 
- Ubuntu (for Windows and MacOS)

## Installation

Clone the repository:
```
git clone https://github.com/zichzhang/OpenSeat.git
```
and naviguate into the `OpenSeat` directory:
```
cd OpenSeat
```
Install Selenium:
```
pip install Selenium
```
Download Chrome WebDriver and place it inside of the `OpenSeat` directory:

This can be done directly from the command line: 
```
cd OpenSeat
mv ~/Downloads/chromedriver .
```

## Usage

Run the `scraper.py` file from the command line:
```
python scraper.py
```
This will open up a chrome browser, check for class openings for the specified course, and notify the user by email if there are any seats available.

## Automation 

We will use cron to set up a crontab that automatically runs `scraper.py` every 30 minutes.

Open your Ubuntu or Linux terminal and naviguate into the `OpenSeat` directory:
```
cd ~/mnt/c/.../OpenSeat
```
Change the default editor to [vim](https://vim.rtorr.com/) (optional):
```
export EDITOR=vim
```
Create a new crontab:
```
crontab -e
```
In a single line, insert the [cron schedule expression](https://crontab.guru/) to be ran every 30 minutes followed by the absolute path of `scraper.py`.
```
*/30 * * * * /mnt/c/.../OpenSeat/scraper.py 
```
Save and exit your crontab and `scraper.py` is now scheduled to run automatically every 30 minutes.

