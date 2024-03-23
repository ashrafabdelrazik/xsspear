import subprocess

def get_urls(target, exclude):
    subdomain = target.partition("://")[2].partition("/")[0]
    print("\033[96m[!] Gathering URLs: \033[33m%s" %target)
    getURLS = subprocess.getoutput("wget -O - \"https://web.archive.org/cdx/search/cdx?url=%s&matchType=domain&fl=original&collapse=urlkey\" | grep -v 'css\|jpg\|png\|gif\|eot\|js\|woff2\|otf\|woff' | grep -v '%s' | awk -F '?' '!seen[$1]++' | uro > %s.txt" %(subdomain,exclude,subdomain))
    urls = open(subdomain+'.txt','r').read().splitlines()
    print("\033[96m[!] URLs: \033[33m%s" %len(urls))
    return urls
