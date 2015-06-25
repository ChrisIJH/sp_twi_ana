import pers_authe as authe
from twython import TwythonStreamer
import pandas as pd


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data
    
    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

sp = pd.read_table('sp500', header=None)
tickr = sp[0]
names = sp[1]

tmp = tickr[0]
for i in tickr[1:]:
    tmp = tmp + ', '  + i
#for i in names:
#    tmp = tmp + ', ' + i
#tmp = tmp.replace('.', '')

stream = MyStreamer(authe.consumer_key, authe.consumer_secret, authe.access_token, authe.access_token_secret)
stream.statuses.filter(track=tmp)
