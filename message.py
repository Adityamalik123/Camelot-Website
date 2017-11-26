from twilio.rest import TwilioRestClient
import random,string
import os
from urlparse import urlparse

from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

proxy_url = os.environ.get("http_proxy")
host, port = urlparse(proxy_url).netloc.split(":")
Connection.set_proxy_info(host, int(port), proxy_type=PROXY_TYPE_HTTP)
def regText(number):
        account_sid = "AC309b4529097a4a869e2da0f1d426eec4"
        auth_token  = "b5c368bc47462020e67b74ceeb3eb7e6"
        Client = TwilioRestClient(account_sid, auth_token)
        otp=''.join(random.choice(string.digits) for x in xrange(4))
        message = Client.messages.create(to="+918586002816", from_="+13366523452", body=" "+otp+" " )
        print(message.sid)
        return otp
