from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import json
import pandas as pd

ListOfFailedMerges = ['4129bb21c985bfe611f2d8cf52b3ac0ed598cabe']


def extract_failed_merged_features(ListOfFailedMerges, Repo):
    SHA_list = ListOfFailedMerges
    message = []
    total = []
    additions = []
    deletions = []
    for SHA in ListOfFailedMerges:
        url_commit = 'https://api.github.com/repos/' + \
            Repo + '/commits/' + SHA
        request_nbofchanges = Request(url_commit, headers={
            "authorization": "Bearer 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 "})
        url = urlopen(request_nbofchanges)
        data = json.load(url)
        message.append(data["commit"]["message"])
        total.append(data["stats"]["total"])
        additions.append(data["stats"]["additions"])
        deletions.append(data["stats"]["deletions"])
    dataframe = pd.DataFrame({'SHA': SHA_list, 'Message': message, 'Additions': additions, 'Deletions': deletions,
                             'Total': total}, columns=['SHA', 'Message', 'Additions', 'Deletions', 'Total'])
    return dataframe


print(extract_failed_merged_features(ListOfFailedMerges, 'microsoft/vscode'))
