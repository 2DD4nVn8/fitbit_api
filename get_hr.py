import fitbit_api

client_id= "222DR2Z" 
secret = "e7f4ba034ca83d9e0de1b04e1b5c38a5" 
tokenfile = "fitbit_token_qol1.txt"

qol1 = fitbit_api.fitbitActivities(CLIENT_ID = client_id ,CLIENT_SECRET = secret, TOKEN_FILE = tokenfile)
hr = qol1.get_hr()
print(hr)




