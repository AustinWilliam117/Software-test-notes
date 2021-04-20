import requests
from dict_params import params

params.header_params('page=2&count=12&keywords=')

article_list = 'http://182.92.178.83:8081/admin/article/all'

dict_params = {'page': '1', 'count': '6', 'keywords': ''}

headers = {'cookie':'JSESSIONID=04FBF0C552F10AA7961F9585B94213E4',
            'Content-Type':'application/json;charset=UTF-8',
            }

keywords_list = ['mengxun','12','江南一点雨']

for keyword in keywords_list:
    print("-------------------------------------")
    dict_params['keywords'] = keyword
    article_list_get = requests.get(article_list,headers=headers,params=dict_params)
    print(article_list_get.json())