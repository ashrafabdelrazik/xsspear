import requests
import re

p = set()

def get_parameters(url, headers):
    r = requests.get(url, headers=headers, timeout=20)
    for l in r:
        l1 = re.sub(' |\\\|`|!|@|#|\$|%|\^|\&|\*|\(|\)|\+|\{|\}|\[|\]|\>|\,|\<|\*|\;|\'|\~|\.|\"|\:|/|\?|(["|"])|\=', r'\n', l.decode('utf-8', 'ignore'), flags = re.M)
        l2 = re.sub('\n\s*\n', r'\n', l1, flags = re.M)
        l3 = re.sub('\s+', r'\n', l2, flags = re.M)
        l4 = re.sub('-|_', r'\n', l3, flags = re.M)
        l3_parameters = l3.splitlines()
        l4_parameters = l4.splitlines()
        for par in l3_parameters:
            if par not in p:
                p.add(par)
            else:
                pass
        for par in l4_parameters:
            if par not in p:
                p.add(par)
            else:
                pass

    parameters = iter(p)

    return parameters
