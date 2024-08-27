import os, ast, re, json, requests
from parsel import Selector


BASE_DIR = os.path.abspath(os.path.join(__file__, '..', '..'))
lawDict = ast.literal_eval(open(os.path.join(BASE_DIR, "res/lawDict.txt"), "r", encoding='utf-8').read())
lawNameDict = open(os.path.join(BASE_DIR, "res/lawName.txt"), "r", encoding='utf-8').readlines()
lawNameDict = {i.split()[0]: i.split()[1] for i in lawNameDict}

# Get the intersection of the 2 value list from 2 dict
lawValue = set(lawDict.values())
lawNameValue = set(lawNameDict.values())
lawValue &= lawNameValue

# Get the whole lawcode
r = requests.get('https://law.moj.gov.tw/api/data/chlaw.json')
r.encoding = 'utf-8-sig'
s = json.loads(r.text)["Laws"]
laws = [law for law in s if law["LawURL"][-8:] in lawValue]
for law in laws:
    print(law["LawName"], law["LawModifiedDate"])

