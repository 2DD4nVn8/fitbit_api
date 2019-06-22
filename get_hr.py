import fitbit_api

client_id= "*****" 
secret = "******" 
tokenfile = "fitbit_token.txt"

hr_data = fitbit_api.fitbitActivities(CLIENT_ID = client_id ,CLIENT_SECRET = secret, TOKEN_FILE = tokenfile)
hr = hr_data.get_hr()
print(hr)




