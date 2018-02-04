import requests
import csv
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def get_one_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                  ,'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
                  }
    html = None
    cookies = dict(JSESSIONID='8054DADE59CD040AE0C483D720765A57,4F973D83F15EBBBD3AA8742CFD8767DF', loginUrl="https://fuligoldtest-flg.fuligold.com", mz_id='mptmd0dN2sK7',Hm_lvt_4332290e1b22394a7fe70c20ae4bc828='1507533888,1507603814,1507603835,1507617016', Hm_lpvt_4332290e1b22394a7fe70c20ae4bc828='1507621334',FTFLGSID='FTFLGSRV2')
    d = {'orderNo':'092132931196','chnlNo':'fwp_app             ','key':'629f2f14f8deb311f5760c5c566b0d29','busiCd':'FL01','payResult':'0000'}
    try:
        response = requests.post(url,data=d,headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('network exception')
            return None
    except RequestException as  e:
         print('network exception')
         print(e)
         return None

def parse_page(html,**kw):
# def parse_page(html):
    bs4_html =BeautifulSoup(html,'lxml')
    base_info = bs4_html.find_all(class_='but')
    content_dic = {}
    for child in base_info:
        child_id = child['href'][1:]
        if(child_id not in content_dic):
            # print(bs4_html.find(id=child_id))
            content_dic[child_id] = bs4_html.find(id=child_id)
            if child_id == 'jibenxinxi':
                strjx = ''
                # print(child.string+";\n")
                for cl in bs4_html.find(id=child_id)('p'):
                    # print(cl.span.string + cl.b.string)
                    strjx = strjx+cl.span.string + cl.b.string+ '\n'
                strjx = child.string+";\n" + strjx
                print(strjx)
                kw['base_inf'] = strjx
                print("===========================")
            if child_id == 'tequan':
                strtq = ''
                # print(child.string+";\n")
                for tq in bs4_html.find(id=child_id)('li'):
                    if tq.contents[1] != '\n' and tq.contents[3] != '\n':
                        # print(tq.contents[1].img['alt']+':\n'+str(tq.contents[3]).replace('<p>','').replace('</p>','').replace('<br>','').replace('<br/>',''))
                        strtq = strtq + tq.contents[1].img['alt']+':\n'+str(tq.contents[3]).replace('<p>','').replace('</p>','').replace('<br>','').replace('<br/>','')+'\n'
                strtq = child.string+";\n" + strtq
                print(strtq)
                # print('===========')
                kw['privilege'] = strtq
                print("===========================")
            if child_id == 'feiyong':
                strfy = ''
                # print(child.string+";\n")
                for fy in bs4_html.find(id=child_id)('p'):
                    # print(fy.span.string+fy.b.string)
                    strfy = strfy + fy.span.string+fy.b.string+'\n'
                print(bs4_html.find(class_='feilv_tittle'))
                if bs4_html.find(class_='feilv_tittle') == None:
                    length = 0
                    strfy = strfy + bs4_html.find(class_='feilv').span.string + bs4_html.find(class_='feilv').contents[1].string.strip()+'\n'
                else:
                    length = len(bs4_html.find(class_='feilv_tittle')('b'))
                for i in range(length):
                    # print(bs4_html.find(class_='feilv_tittle')('b')[i].string+':'+bs4_html.find(class_='feilv_number')('b')[i].string+',')
                    strfy = strfy + bs4_html.find(class_='feilv_tittle')('b')[i].string+':'+bs4_html.find(class_='feilv_number')('b')[i].string+','+'\n'
                strfy = child.string+";\n" + strfy
                print(strfy)
                kw['related_const'] = strfy
                print("===========================")
    return kw

if __name__ == '__main__':
    # html = get_one_page('https://www.rong360.com/credit/card/49a0649072ec35f5e4b96b44255ce09f')
    # html = get_one_page('https://www.rong360.com/credit/card/dd7109c8bbfedddc02499b619c0ad615')
    html = get_one_page('https://www.rong360.com/credit/card/b2645a25f6215e6a627c173f1c918bbd')
    # html = get_one_page('https://www.rong360.com/credit/card/61548a734be709e2036b5d2b28804c7c')
    # html = get_one_page('https://www.rong360.com/credit/card/b2645a25f6215e6a627c173f1c918bbd')
    # html = get_one_page('https://www.rong360.com/credit/card/762a48de86c757af29bbdaeb33d37bdb')
    if html != None:
        parse_page(html)