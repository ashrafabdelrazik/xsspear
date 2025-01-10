from urls import get_urls
from pars import get_parameters
from loop import loop
import argparse

def main(mode, url, sub, headers, c):
    if mode == 'url':
        parameters = get_parameters(url, headers)
        loop(parameters, headers, url)
    else:
        urls = get_urls(sub, exclude)
        for url in urls:
            c += 1
            parameters = get_parameters(url, headers)
            print("\033[96m[!] Remaining URLS: \033[33m" + str(len(urls) - c))
            loop(parameters, headers, url)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--mode", required=True, help="modes: url, sub")
    ap.add_argument("-u", "--url", required=False, help="mode")
    ap.add_argument("-s", "--sub", required=False, help="mode")
    ap.add_argument("-a", "--useragent", required=False, help="User Agent", nargs='?', const=1, default="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0")
    ap.add_argument("-c", "--cookies", required=False, help="Cookies", nargs='?', const=1, default="NULL")
    ap.add_argument("-x", "--exclude", required=False, help="Exclude lines that contains a string", nargs='?', const=1, default="h1ashrafabdelrazik")
    args = vars(ap.parse_args())
    headers = {'User-Agent': args["useragent"], 'Cookie': args["cookies"]}
    mode = args["mode"]
    url = args["url"]
    sub = args["sub"]
    exclude = args["exclude"]
    c = 1
    main(mode, url, sub, headers, c)
