# coding=utf-8
import json
import falcon
from waitress import serve

_BOOK_DICT = {"init_book": "the init book", "init_book2": "the init book2"}


class BookShelfList(object):
    def on_get(self, req, resp):
        resp.body = json.dumps(_BOOK_DICT)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        raw_data = req.stream.read()
        data = json.loads(raw_data)
        print data
        if data and len(data) == 1:
            _BOOK_DICT.update(data)
            resp.body = 'success\n'
            resp.status = falcon.HTTP_200
        else:
            resp.body = '{"message": "error data:%s"}' % (raw_data)
            resp.status = falcon.HTTP_400


class BookShelf(object):
    def on_get(self, req, resp, book_key):
        if book_key not in _BOOK_DICT:
            resp.body = '{"message": "error key."}'
            resp.status = falcon.HTTP_400
        else:
            resp.body = '{"%s": "%s"}' % (book_key, _BOOK_DICT.get(book_key))
            resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, book_key):
        if book_key not in _BOOK_DICT:
            resp.body = '{"message": "error key."}'
            resp.status = falcon.HTTP_400
        else:
            _BOOK_DICT.pop(book_key)
            resp.body = '{deleted key: "%s"}' % book_key
            resp.status = falcon.HTTP_200


if __name__ == '__main__':
    api = application = falcon.API()
    api.add_route('/bookshelf', BookShelfList())
    api.add_route('/bookshelf/{book_key}', BookShelf())
    serve(api, host="0.0.0.0", port=8000)
