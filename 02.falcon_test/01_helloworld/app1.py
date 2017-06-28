# coding=utf-8
import falcon
from waitress import serve


class Hello():
    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200


api = application = falcon.API()

# 增加路由
api.add_route('/hello', Hello())

if __name__ == '__main__':
    serve(api, host="0.0.0.0", port=8000)
