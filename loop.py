from pars import p
from tqdm import tqdm
import asyncio
import aiohttp
import math
import time
from email.message import EmailMessage
import smtplib
import re


def loop(parameters, headers, url):

  q = "=xsspear<>"
  out = open('spear.out', 'a+')

  print("\n\033[96m[!] Requests: \033[33m%s" % len(p))
  print("\033[96m[!] Scanning: \033[33m%s" % url)

  with tqdm(total=len(p),
            desc="\033[96m[!] RXSS Scan",
            bar_format="\033[33m{l_bar}{bar}") as pbar:
    o = set()

    async def main(p):

      async def get(c_url, session):
        try:
          async with session.get(c_url, headers=headers,
                                 timeout=60) as response:
            html = await response.text()
            if "xsspear<>" in html or re.search(r" \w+=xsspear", html) or re.search(r" \w+='xsspear", html) or re.search(r" \w+=\"xsspear", html) or re.search(r"var \w+ = 'xsspear", html):
              o.add(c_url)
              out.write("%s\n" % c_url)
            pbar.update(1)
        except:
          pbar.update(1)

      async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(
            *[get(url + "?&" + p + q, session) for p in parameters])

    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(main(parameters))
    end = time.time()

  out.close()

  print("\033[96m[!] Duration: \033[33m%s\033[96ms" % math.trunc(end - start))
  print("\033[96m[!] Reflections: \033[31m%s" %
        str(len(open('spear.out', 'r').readlines())))

  if len(o) == 0:
    print("\033[96m[!] \033[33mSecure")
  else:
    print("\033[96m[+] \033[31mInsecure")
    message = EmailMessage()
    message.set_content(
        '<h3>URLS:</h3><br><code> ' + str(list(o)),
        subtype='html')

    message['Subject'] = '[XSSpear] Possible rXSS on ' + url
    message['From'] = 'null'
    message['To'] = 'null'
    try:
      server = smtplib.SMTP('smtp.office365.com', 587)
      server.starttls()
      server.login('null', 'null')
      server.send_message(message)
      server.quit()
    except Exception as e:
      print('Error sending email:', e)
