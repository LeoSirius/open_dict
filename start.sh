source /root/venvs/open_dict/bin/activate
nohup uvicorn app:app --reload --host 0.0.0.0 --port 80 &>> /tmp/open_dict.log &
