# coding=utf-8
import os
import time
import uuid
import falcon
from waitress import serve


def _media_type_to_ext(media_type):
    # 剥离'images/'前缀
    return media_type[6:]


def _ext_to_media_type(ext):
    return 'image/' + ext


def _generate_id():
    return str(uuid.uuid4())


class ImageResource(object):
    def __init__(self, storage_path="./images"):
        self.storage_path = storage_path

    def on_post(self, req, resp):
        image_id = _generate_id()
        ext = _media_type_to_ext(req.content_type)  # content_type: image/jpeg
        filename = image_id + '.' + ext

        image_path = os.path.join(self.storage_path, filename)
        with open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break
                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + image_id


class Item(object):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp, name):
        ext = os.path.splitext(name)[1][1:]
        resp.content_type = _ext_to_media_type(ext)

        image_path = os.path.join(self.storage_path, name)
        resp.stream = open(image_path, 'rb')
        resp.stream_len = os.path.getsize(image_path)


if __name__ == '__main__':
    api = application = falcon.API()
    api.add_route('/images', ImageResource())
    serve(api, host="0.0.0.0", port=8000)
