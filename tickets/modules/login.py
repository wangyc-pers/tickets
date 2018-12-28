# coding=utf-8
import logging
import time
import base64

log = logging.getLogger(__name__)

class Auth(object):
    def __init__(self, session):
        self.session = session
    
    def left_ticket_init(self):
        resp = self.session.advance_request("left_ticket_init")
        log.debug("request left_ticket_init %s", "success!" if resp else "faild!")

    def get_verify_code(self):
        params = {
            int(time.time()*1000): "",
        }
        resp = self.session.advance_request("login_check", params=params)
        data = resp.json()
        if data["result_code"] == "0":
            img = base64.decodestring(data["image"])
            return img
        else:
            raise Exception("get verify code failed!")

    