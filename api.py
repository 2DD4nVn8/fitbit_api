import fitbit
import datetime
import pandas as pd
from ast import literal_eval

CLIENT_ID     = "22DDQY" # 自分のやつを入れる。
CLIENT_SECRET = "9abd51cb2f494de76842f1490d266dfe" # 自分のやつを入れる。
TOKEN_FILE    = "fitbit_token.txt"

tokens = open(TOKEN_FILE).read()
token_dict = literal_eval(tokens)
access_token = token_dict['access_token']
refresh_token = token_dict['refresh_token']

def updateToken(token):
    f = open(TOKEN_FILE, 'w')
    f.write(str(token))
    f.close()
    return

client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token = access_token, refresh_token = refresh_token, refresh_cb = updateToken)

#TODAY = datetime.date.today()
TODAY = "2018-12-12"

#データの取得
DATE = TODAY
#heart rate
data_hr_sec = client.intraday_time_series("activities/heart", DATE, detail_level="1sec")
hr_sec = data_hr_sec["activities-heart-intraday"]["dataset"]
resthr = data_hr_sec['activities-heart'] #resting heart rate
#step
data_act_sec = client.intraday_time_series('activities/steps', DATE, detail_level='1min') 
step_sec = data_act_sec['activities-steps-intraday']["dataset"]
print(data_act_sec['activities-steps'])
#Calories
data_cal_sec = client.intraday_time_series("activities/calories", DATE, detail_level="1min")
cal_sec = data_cal_sec['activities-calories-intraday']["dataset"]
print(data_cal_sec['activities-calories'])

#print(resthr)
#print(heart_sec[:10])
df_hr = pd.io.json.json_normalize(hr_sec)
df_hr = df_hr.rename(columns={'value':'hr'})
df_hr["time"] = DATE + "T" + df_hr["time"]
df_hr["time"] = pd.to_datetime(df_hr["time"])
df_hr = df_hr.set_index("time")

df_step = pd.io.json.json_normalize(step_sec)
df_step = df_step.rename(columns={'value':'step'})
df_cal = pd.io.json.json_normalize(cal_sec)
df_cal = df_cal.rename(columns={'value':'cal'})
df_all = pd.merge(df_cal, df_step, on='time', how='outer')
df_all["time"] = DATE + "T" + df_all["time"]
df_all["time"] = pd.to_datetime(df_all["time"])
df_all = df_all.set_index("time")

#print(df_all[:10])
df_all = df_all.resample('1S').interpolate()
df_hr = df_hr.resample('1S').interpolate()

#print(df_all[:10])

df_all = pd.merge(df_all, df_hr, on="time")
df_all = df_all.interpolate('linear')

#print(df_hr)
#print(df_step)
#print(df_cal)
print(df_all)
#df_hr.to_csv("fitbit-hr-" + DATE + ".csv")
#df_step.to_csv("fitbit-step-" + DATE + ".csv")
#df_cal.to_csv("fitbit-cal-" + DATE + ".csv")
df_all.to_csv("fitbit-hr-step-cal-" + DATE + ".csv")






