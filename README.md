# XSSpear (Cross Site Scripting Scanner)

### Install Dependencies:
`pip3 install -r requirements.txt`

### Example Usage:

Single Target URL
  
```bash
python3 main.py -m url -u "https://xss-game.appspot.com/level1/frame"
````

Subdomain:

```bash
python3 main.py -m sub -s "https://xss-game.appspot.com/"
```
