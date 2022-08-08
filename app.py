from flask import Flask
import requests
import configparser

print('Rainfall Service started')

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

url=config['InputSection']['URL']
location=config['InputSection']['LOCATION']
print('URL:' + url)
print('LOCATION:' + location)

#print Location, Time, Rainfall Amount, Raining/Not Raining
r = requests.get(url)
stations = r.json()['metadata']['stations']
items = r.json()['items']
readings=r.json()['items'][0]['readings']
reading_type=r.json()['metadata']['reading_type']
reading_unit=r.json()['metadata']['reading_unit']

@app.route('/')
def rainfall():
    name=''
    timestamp=''
    raining=0
    result=''
    for i in stations:
        if i['id'] == location:
         name=i['name']
    for j in items:
        timestamp=j['timestamp']
    for k in readings:
        if k['station_id'] == location:
            raining=int(k['value'])
    if raining ==0:
        result = name + ' ' + timestamp + ' '+ 'NOT Raining'
        #print(name, timestamp,'NOT Raining')
        return result
    else:
        result = name + ' ' + timestamp + ' ' + 'Raining'
        return result
        #print(name, timestamp,'Raining')       
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
    