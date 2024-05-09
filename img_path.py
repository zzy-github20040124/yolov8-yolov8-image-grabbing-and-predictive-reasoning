import requests
import time
import os
def get_now(need):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&oq=%E7%BE%8E%E5%A5%B3&rsp=-1',
        'Cookie':'BIDUPSID=9ED5C7B6BC24B75BAD7DD3602364168F; PSTM=1661178555; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221101761423610%22%2C%22first_id%22%3A%22183b711ec27b46-0f1ed9021e66da-7b555471-1327104-183b711ec28134a%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22183b711ec27b46-0f1ed9021e66da-7b555471-1327104-183b711ec28134a%22%7D; __bid_n=184284f1165a3daef64207; FEID=v10-20f7261b52dc1396cb1f0c5c997df5aad2d90f09; __xaf_fpstarttimer__=1672850008453; __xaf_thstime__=1672850008722; __xaf_fptokentimer__=1672850008779; FPTOKEN=V9NZL6oWaAbRWew1MlNsgtgCcGiVR6LCtGdOCbdDGlFFiI/2EpNPVXuT44hARLp6KKwb2UZcmXaz6/1r0sq6e4lXXmwzOdoxx9fmpVn3U2y6xKFLPkkqE1/NYRT0tm/lpSNR32zmfBcp+cqCqFp2JmTExJyyoTyYRTaeEoRPgotIxTWywkX59Ax4b06XZvh3jhUMUSDgtmbYzXqRl+ZD9LKu+7rXTfOjYxPnNejJ6FB558HqF4L1gIWhPXnRPbxUxZXRFxloK6tkTZ9AwzbopMzhUbcvar0pIZ9OMkJyK0edROm+oXtevSrBjpEmPUxbZPJxsTJc/mZIYDzEVhIAb2/VEi8EvtaCbaW7pLwJQN6xBOeJEpET/9uzbUyvARTFS2TzovvbOFe2iwdsc6X8Fw==|GwC+Pi3t/1cSJk/Cb/4riop3IO4jxtErLNh0cfbNFz8=|10|1094dbe5f1442c82ea2ead692792d74c; BAIDUID=737E381665C4701DF1DB195FC03CBFE0:FG=1; BAIDUID_BFESS=737E381665C4701DF1DB195FC03CBFE0:FG=1; newlogin=1; BDUSS=5seThmWFhHeWZmT3FFQk1PalBJblB5UmlTbzRRT1JmeEVoZ3VDd1VIem9UQjFsSVFBQUFBJCQAAAAAAAAAAAEAAAA5HKN~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOi~9WTov~Vkbk; BDUSS_BFESS=5seThmWFhHeWZmT3FFQk1PalBJblB5UmlTbzRRT1JmeEVoZ3VDd1VIem9UQjFsSVFBQUFBJCQAAAAAAAAAAAEAAAA5HKN~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOi~9WTov~Vkbk; RT="z=1&dm=baidu.com&si=006fdf16-7663-472a-9c11-bdd221f15f3e&ss=lm6bpcgm&sl=1&tt=tu&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=3e3jpyf1&cl=1cg&ld=1vg&ul=l5e&hd=l5r"; ZD_ENTRY=bing; BA_HECTOR=2g2hag052l8ka5010g8ka5a01ifoebl1p; ZFY=8Ec79sb:BnS8L5DuhnjaAZL7VIFVd5xnOM07UA3k823E:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; delPer=0; H_PS_PSSID=39313_39227_39280_39222_39097_39198_39294_39261_39268_39240_39233_39141_26350_39239_39225; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
        'Sec-Ch-Ua-Platform':'Windows',
        'Host':'image.baidu.com',
        'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    }

    params = {
        'tn': 'resultjson_com' ,
        'logid': '8035140459874478269' ,
        'ipn': 'rj' ,
        'ct': '201326592' ,
        'is': '',
        'fp': 'result' ,
        'fr':'' ,
        'word': '{}'.format(need),
        'cg': '',
        'queryWord': '{}'.format(need) ,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8' ,
        'adpicid': '',
        'st': '',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '',
        'istype':'',
        'qc': '',
        'nc': '1',
        'expermode': '',
        'nojc': '',
        'isAsync':'',
        'pn': '60',
        'rn': '30',
        'gsm': '3c',
        '1694251392841': '',
    }

    time_1 = time.localtime()

    time_now = time.strftime("\%Y-%m-%d-%H_%M_%S",time_1)

    path = 'img_datas' + time_now
    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path + '创建成功')
    else:
        print('gg')

    res = requests.get('https://image.baidu.com/search/acjson',headers = headers,params=params)
    img_list = []
    for i in range(0,30):
        img_list.append(res.json()['data'][i]['middleURL'])

    img_downlode = []

    for i in img_list:
        asd = requests.get(i).content
        img_downlode.append(asd)

    number = 1
    for i in img_downlode:
        with open('{}/{}.jpg'.format(path,number),'wb') as f:
            f.write(i)
            number = number + 1

    print('爬取成功')
    return path
