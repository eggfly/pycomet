#! /usr/bin/env python3
from conf import HOST
import urllib.request
import time

URL_ASYNC = HOST + "async"


def get_loop_url(channel_id):
    return "%s/loop/%s" % (HOST, channel_id)


def request(url):
    t = time.time()
    while True:
        print("before open")
        fp = urllib.request.urlopen(url)
        print("opened")
        content = fp.read()
        fp.close()
        code = fp.getcode()
        print("HTTP code: %s, time %s, content: \n%s" % (code, time.time() - t, content))
        if content:
            break
        else:
            print("next call")


if __name__ == '__main__':
    request(get_loop_url("b87ac12f-d04c-4f3a-8521-2d6ab1fc1a4f"))
