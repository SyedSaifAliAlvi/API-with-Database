import tornado.web
import tornado.ioloop
import asyncio
from get_users_data import get_users
from Post_User_data import insert_user
from get_user import get_user


class basicRequestHandler(tornado.web.RequestHandler):

    async def get(self):
        queryParameter = self.request.arguments
        if bool(queryParameter):
            try:
                uid = queryParameter.get('id', None)
                print(uid)
                if uid is None:
                    self.write("Empty not possible")
                else:
                    uid = uid[0].decode('utf-8')
                    user = get_user(uid)
                    self.write(user)
            except:
                self.write("queryParameter id is missing")
        else:
            current_users = get_users()
            self.write(current_users)

class staticRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('post-method.html')

    async def post(self):
        data = self.request.body
        data = ((data).decode('utf-8')).split('&')
        body={}
        for value in data:
            value = value.split('=')
            body[value[0]]=value[1]

        response = insert_user(body)
        self.write(response)




if __name__ == '__main__':
    app = tornado.web.Application([(r"/", basicRequestHandler),
                                   (r"/result",staticRequestHandler)])
    print("SERVER IS RUNNING.......")
    print("http://localhost:8887")
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8887, '127.0.0.1')
    server.start()
    asyncio.get_event_loop().run_forever()
