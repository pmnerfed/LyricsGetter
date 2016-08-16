import json
import requests




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
    #data = json.load(json_data);
    #print(json_data);

    ob = json_data.get("result",{}).get("songs",{})
    for i in ob:

        print(i.get("name",{}))
        for ar in i.get("artists", {}):
            print("        "+ar.get("name", {}))
        print("            "+str(i.get("id", {})))



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
        print("here")
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
            print("here2")
            p = httpRequest('POST', action, data)
            return p






val = search("still alive jonathan")
id_get(val)
    
