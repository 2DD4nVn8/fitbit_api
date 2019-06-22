import fitbit
import datetime
from ast import literal_eval

class fitbitActivities:

    def _updateToken(token):
        f = open(TOKEN_FILE, 'w')
        f.write(str(token))
        f.close()
        return

    def __init__(self,CLIENT_ID,CLIENT_SECRET,TOKEN_FILE):
        tokens = open(TOKEN_FILE).read()
        token_dict = literal_eval(tokens)
        self._access_token = token_dict['access_token']
        self._refresh_token = token_dict['refresh_token']
        self._client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token = self._access_token, refresh_token = self._refresh_token, refresh_cb = self._updateToken)

    def get_hr(self,date=datetime.date.today(),detail_time="15min"):
        self._data_hr = self._client.intraday_time_series("activities/heart", date, detail_level=detail_time)
        print(self._data_hr)
        return self._data_hr

    def get_step(self,date=datetime.date.today(),detail_time="15min"):
        self._data_step = self._client.intraday_time_series('activities/steps', date, detail_level=detail_time) 
        print(self._data_step)
        return self._data_step

    def get_Calories(self,date=datetime.date.today(),detail_time="15min"):
        self._data_cal = self._client.intraday_time_series("activities/calories", date, detail_level=detail_time)
        print(self._data_cal)
        return self._data_cal








