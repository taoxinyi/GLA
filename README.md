# gla
Git Log Analyzer
## Usage
```python
from pymongo import MongoClient
from gla import GLA
from classify import *

client = MongoClient('server_ip', "server_port") #change it to mongo ip and port
gla = GLA('config.json', client['git']['commit'])
print(gla.analyze_total_code_churn(['2018-10-10', '2018-11-28'], Oss, os_classify, ['media_embargo']))
print(gla.analyze_group_code_churn_by_period('weekly', ['2018-49', '2018-51'], [['media_embargo/windows']]))
print(gla.analyze_group_total_code_churn(['2018-10-29', '2018-12-05'], [['media_driver'], ['media_embargo']]))
```
## Functions
### analyze_total_code_churn
folder(s)'s loc, files, commit times and regression times, categorized by `Platform` from 2018-10-01 to 2018-11-01
### analyze_code_churn_by_period
folder(s)'s weekly loc, files, commit times and regression times,categorized by `Platform` from 2018-42 to 2018-48
### analyze_group_total_code_churn
Multiple groups's loc, files, commit times and regression times in 2018-10-01 to 2018-11-01
### analyze_group_code_churn_by_period
Multiple groups's weekly loc, files, commit times and regression times from 2018-42 to 2018-48

## MongoDB
MongoDB are used to store the git log and regressions