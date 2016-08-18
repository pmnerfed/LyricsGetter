import json
import requests
import time
import sys


header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'                                                                                                    
            }
cookies = {
            'appver': '1.5.2'                
        }







def id_get(json_data):
    ##data = json.load(json_data);
    #print(json_data);

    ob = json_data.get("result",{}).get("songs",{})
    for i in ob:

        print(i.get("name",{}))
        for ar in i.get("artists", {}):
            print(ar.get("name", {}))
        print(str(i.get("id", {})))
        return i.get("id", {})


def httpRequest(method, action, query=None, urlencoded=None, callback=None, default_timeout=None):    
    if(method == 'GET'):
        url = action if (query == None) else (action + '?' + query)
        connection = requests.get(url, headers=header, timeout=default_timeout)

    elif(method == 'POST'):
        connection = requests.post(
                        action,
                        data=query,
                        headers=header,
                        timeout=default_timeout                                                                                                                
                        )
        #print("here")
        #connection,json()
    connection.encoding = "UTF-8"
    #print(connection.text)
    connection = json.loads(connection.text)
    return connection






def search(s, stype=1, offset=0, total='true', limit=3):
            action = 'http://music.163.com/api/search/get/'
            data = {
                    's': s,
                    'type': stype,
                    'offset': offset,
                    'total': total,
                    'limit': limit                                                                            
                    }
            #print("here2")
            p = httpRequest('POST', action, data)
            return p




def getLyrics(id):
    url_lyric = "http://music.163.com/api/song/lyric?id="+str(id)+"&lv=1"
    
    p = httpRequest('GET', url_lyric)
    return p.get('lrc', {}).get('lyric', {})





#val = search("still alive jonathan")
val = search("hips dont lie shakira")
ID = id_get(val)

lyrics_data = getLyrics(ID)
arr = lyrics_data.split('\n')
#print(lyrics_data)
while(True):
    try:
        p = arr[1].split(']',1)
    except:
        arr=arr[1:]
        continue
    
    init_time_str =p[0][1:-4]
    try :
        init_time = time.mktime(time.strptime(init_time_str, "%M:%S"))
        break
    except:
        arr=arr[1:]



lyr =[]

for l in arr[1:-1]:
    b = l.split(']', 1)
    #print(b)

    #print(l.split(']'))
    secT, garbage = b[0][1:].split('.')
    mytime = time.mktime(time.strptime(secT,"%M:%S"))
    elapse = mytime - init_time
    #print(mytime.strftime() + "   :    " + b)
    #tmm = '-'.join(str(x) for x in list(mytime))
    tup =(elapse, b[-1])
    lyr.append(tup)


#for l in lyr:

    #for char in b:
    #    sys.stdout.write(char)
    #    sys.stdout.flush()
    #    time.sleep(0.1)

    #print(elapse)
    

diff_lyr=[]

for t in range(0,len(lyr)-1):
    tm=0
    if (t==len(lyr)):
        tm = lyr[t][0]
    else:
        tm = lyr[t+1][0]-lyr[t][0]
    diff_lyr.append((tm,lyr[t][-1]))

#for i in diff_lyr:
 #   print('\r'), print(i[1])
  #  time.sleep(i[0])

for i in diff_lyr:
    print('\r'), 
    for char in i[1]:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(i[0]/len(i[1]))
    #time.sleep(i[0])



