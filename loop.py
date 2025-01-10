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

  q = "=xsspear<>&"
  out = open('xsspear.out', 'a+')

  print("\n\033[96m[!] Parameters: \033[33m%s" % math.trunc(len(p)))
  #print("\033[96m[!] Scanning: \033[33m%s" % url)

  o = set()

  async def main(p):
    async def get(c_url, session):
      print("\033[96m[!] Scanning: \033[33m%s" % c_url)
      try:
        async with session.get(c_url, headers=headers,timeout=60) as response:
          html = await response.text()
          if "xsspear<>" in html or re.search(r" \w+=xsspear", html) or re.search(r" \w+='xsspear", html) or re.search(r" \w+=\"xsspear", html) or re.search(r"var \w+ = 'xsspear", html):
            o.add(c_url)
            out.write("%s\n" % c_url)
      except:
        print("[-] Connection Failed!")

    async with aiohttp.ClientSession() as session:
      ret = await asyncio.gather(*[get(url + "?&" + p1 + q + p2 + q + p3 + q + p4 + q + p5 + q + p6 + q + p7 + q + p8 + q + p9 + q + p10 + q + p11 + q + p12 + q + p13 + q + p14 + q + p15 + q, session) for p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15 in zip(parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters,parameters)])

  loop = asyncio.get_event_loop()
  start = time.time()
  loop.run_until_complete(main(parameters))
  end = time.time()

  out.close()

  print("\033[96m[!] Duration: \033[33m%s\033[96ms" % math.trunc(end - start))
#  print("\033[96m[!] Reflections: \033[31m%s" %str(len(open('xsspear.out', 'r').readlines())))

  if len(o) == 0:
    print("\033[96m[!] \033[33mSecure")
  else:
    print("\033[96m[+] \033[31mInsecure")
#    message = EmailMessage()
#    message.set_content(
#        '<h3>URLS:</h3><br><code> ' + str(list(o)),
#        subtype='html')

#    message['Subject'] = '[XSSpear] Possible rXSS on ' + url
#    message['From'] = 'example@hotmail.com'
#    message['To'] = 'ashrafabdelrazik1996@gmail.com'
#    try:
#      server = smtplib.SMTP('smtp.office365.com', 587)
#      server.starttls()
#      server.login('example@hotmail.com', 'Password123!')
#      server.send_message(message)
#      server.quit()
#    except Exception as e:
#      print('Error sending email:', e)
