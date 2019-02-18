import datetime
import time
import os

past_time = datetime.datetime.now()
delta = datetime.timedelta(days=-1)
past_time = past_time + delta
cur_dir = os.getcwd()
workspace_path = '..\\..\\..\\..\\..\\'
os.chdir(workspace_path)
workspace_dir = os.getcwd()

while True:
    now_time = datetime.datetime.now()
    print(now_time)
    if (now_time - past_time).days > 0:
        time_str = now_time.strftime('%Y-%m-%d')
        print('Get the Latest Workspace ' + time_str + '\n')
        os.chdir(workspace_dir)
        os.system('dt workspace sync --branch comp/media --latest')
        print('Finish Synchronize Workspace\n')
        os.chdir(cur_dir)
        print('Static Analysing...... \n')
        os.system('get_data.bat')
        print('Send Data to Server')
        os.system('send_data.bat ' + time_str)
        past_time = now_time
    else:
        time.sleep(3600)
