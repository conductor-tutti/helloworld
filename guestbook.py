import cgi
import webapp2
from google.appengine.api import users


MAIN_PAGE_HTML = """\
<html>
    <body>
        <form action="/sign" method="post">
            <div><textarea name="content" cols="60" rows="3"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
        </form>
    </body>
</html>
"""


#this code defines one request handler, MainPage, mapped to the root URL(/)
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write("<html><body>You wrote:<pre>")
        self.response.write(cgi.escape(self.request.get("content")))
        self.response.write("</pre></body></html>")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
