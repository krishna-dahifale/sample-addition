import tensorflow as tf
from flask import Flask,jsonify,request
import json
#import pandas as pd
app = Flask(__name__)
@app.route('/add',methods=['POST'])
def add():
        x=tf.placeholder(dtype=tf.int32)
        y=tf.placeholder(dtype=tf.int32)
#        c=tf.add(x,y)
#        print(c)
#       sess=tf.session()
        data=request.get_json()
#       query=json.dumps(data)
#       query=pd.DataFrame(data)
        a=data['x']
        b=data['y']
#        data=json.dumps(data,encoding='UTF-8',default=str)
        sess=tf.Session()
        results=tf.add(a,b)
#       results=tf.placeholder(dtype=tf.int32)
        return jsonify({'sum':str(sess.run(results)),'x':a,'y':b})
if __name__ == "__main__":
        app.run(host='0.0.0.0')