import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from webflask.db.db_conn import Db_coon
from webflask.utils.AES import prpcrypt
import webflask.utils.MD5
app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.get_data().decode('utf-8')
        header = request.headers
        dict1 = json.loads(a)
        print(dict1['data'])
        data = dict1['data']
        firm_no = data['firmNo']
        sql = 'select * from t_weal_integral_inf WHERE firm_no = ?'
        args = (firm_no.strip())
        result = Db_coon().select(sql,args)
        if result != None:
            print(result)
            md5_key = result['MD5_KEY'].strip()
            aes_key = result['AES_KEY'].strip()
            pc = prpcrypt(aes_key)
            print(data['orderNo'])
            order_no = pc.decrypt(data['orderNo'])
            print(order_no)
            return 'ok'
        else:
            return 'accept'
    else:
        return '<h1>只接受post请求！</h1>'
def checkToken():
    pass
@app.route('/user/<name>')
def user(name):
    return'<h1>hello, %s</h1>' % name

if __name__ =='__main__':
    app.run(debug=True,host='192.168.52.51')