
import fdb
from flask import Flask, jsonify, json
from flask_restful import Resource, Api

app = Flask('__name__')
api = Api(app)

class FormasPago(Resource):
    def get(self):
        con = fdb.connect( dsn='192.168.1.252:W:\STECCS_MGV.FDB',
                           user='sysdba',
                           password='masterkey',
                           charset='UTF8')
        cur = con.cursor()
        results = cur.execute("select * from FORMAS_DE_PAGO")
        print (results)
        items = []
        for result in results:
            i = 0
            items.append(str([cur.description][fdb.DESCRIPTION_NAME][i][i]))
            i += 1
        con.close()
        return results

api.add_resource(FormasPago, '/formaspago/')

app.run(port=5000)
