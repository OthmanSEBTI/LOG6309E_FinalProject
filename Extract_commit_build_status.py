from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen
import json

fichiers = [f for f in listdir('Commits logs and build status')
            if isfile(join('Commits logs and build status', f))]

f = open('./Commits logs and build status/' +
         fichiers[fichiers.index('vscode')], "r", encoding='utf-8')
f1 = open('./Commits logs and build status/' +
          'vscode_statusbuild_added2', "w", encoding='utf-8')
lines = f.readlines()
result = []
for x in lines:
    url1 = 'https://api.github.com/repos/'+'microsoft/vscode' + \
        '/commits/' + x.split(',')[0]+'/status'
    request_gitapi = Request(url1, headers={
                             "authorization": "Bearer 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 "})
    url = urlopen(request_gitapi)
    data = json.load(url)
    f1.write(x.strip() + ',' + data["state"])
    if (data["state"] == "failure" or data["state"] == "sucess"):
        f1.write(' ,' + data["statuses"][0]["description"] + '\n')
    else:
        f1.write('\n')

f.close()
