import os, ast, re, json, requests
from parsel import Selector
from docx import Document


BASE_DIR = os.path.abspath(os.path.join(__file__, '..', '..'))
lawDict = ast.literal_eval(open(os.path.join(BASE_DIR, "res/lawDict.txt"), "r", encoding='utf-8').read())
lawNameDict = open(os.path.join(BASE_DIR, "res/lawName.txt"), "r", encoding='utf-8').readlines()
lawNameDict = {i.split()[0]: i.split()[1] for i in lawNameDict}

# Get the intersection of the 2 value list from 2 dict
lawValue = set(lawDict.values())
lawNameValue = set(lawNameDict.values())
lawValue &= lawNameValue

# Get the whole lawcode
if os.path.exists(os.path.join(BASE_DIR, "res/law.txt")):
    with open(os.path.join(BASE_DIR, "res/law.txt"), "r", encoding='utf-8') as f:
        r = f.read()
else:
    r = requests.get('https://law.moj.gov.tw/api/data/chlaw.json')
    r.encoding = 'utf-8-sig'
    r = r.text
    with open(os.path.join(BASE_DIR, "res/law.txt"), "w", encoding='utf-8') as f:
        f.write(r)
s = json.loads(r)["Laws"]
laws = {law["LawName"]: law for law in s if law["LawURL"][-8:] in lawValue}

# Laws: {LawLevel, LawName, LawURL, LawCategory, LawMotifiedDate, LawArticle:{ArticleType, ArticleNo, ArticleContent}}
print('Laws is ready!')
queryString = "民法"
if queryString in laws:
    queryLaw = laws[queryString]
    articles = queryLaw["LawArticles"]
    ans = ""
    for article in articles:
        if article["ArticleType"] == "C":
            ans += article["ArticleContent"].replace("第一節", "第 一 節").replace("第二節", "第 二 節").replace("第三節", "第 三 節").strip() + "\n"
        elif article["ArticleType"] == "A":
            ans += article["ArticleNo"] + " " + article["ArticleContent"] + "\n"
        else: pass
else:
    print('No such law!')

print(ans)


