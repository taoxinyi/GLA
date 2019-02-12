from pymongo import MongoClient
from gla import GLA
from classify import *

client = MongoClient('server_ip', "server_port")
gla = GLA('config.json', client['git']['commit'])
print(gla.analyze_total_code_churn(['2018-10-10', '2018-11-28'], Oss, os_classify, ['media_embargo']))
print(gla.analyze_group_code_churn_by_period('weekly', ['2018-49', '2018-51'], [['media_embargo/windows']]))
print(gla.analyze_group_total_code_churn(['2018-10-29', '2018-12-05'], [['media_driver'], ['media_embargo']]))
