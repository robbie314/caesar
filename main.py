#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
    <h1>Caesar</h1>
"""

page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):


        encrypt_form ='''
        <form action="/encrypt" method="post">
            <label>Rotation Amount</label>
                <input type="text" name="rot"/><br>
            <label>Plain Text</label>
                <input type="text" name="plaintext"</input><br>
                <input type="submit" value="Encrypt"/>
        </form>
        '''
        response = page_header + encrypt_form + page_footer
        self.response.write(response)
    #    self.response.write(encrypt("aaa", 2))

class Encrypt(webapp2.RequestHandler):
    def post(self):
        rot=self.request.get("rot")
        plaintext=self.request.get("plaintext")
        encrypt_text=encrypt(plaintext, int(rot))
        response=page_header + encrypt_text + page_footer
        self.response.write(response)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/encrypt', Encrypt)
], debug=True)
