#!/usr/bin/python

import web
import json

ip = "0.0.0.0"
port = 8000

urls = (
    '/(.*)', 'greet'
)

class greet:
    def GET(self, name):
        if not name:
            name = 'world'
        data = json.dumps("Hello world")
        #return {'message': 'Hello, ' + name + '!'}
        return data

class MyApp(web.application):
    def run(self, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, (ip, port))

app = MyApp(urls, globals())

if __name__ == "__main__":
    app.run()
