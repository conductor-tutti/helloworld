from google.appengine.api import users


import webapp2


#this code defines one request handler, MainPage, mapped to the root URL(/)
class MainPage(webapp2.RequestHandler):
    def get(self):
        #checks for active Google account session
        user = users.get_current_user()
        if user:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.write("Hello! " + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
