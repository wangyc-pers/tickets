# coding=utf-8

import logging
import random
import time

from requests import Session

log = logging.getLogger(__name__)

class RequestSession(Session):
    def __init__(self, base_url, reqs, timeout=2, retry=1):
        super(RequestSession, self).__init__()
        self.base_url = base_url
        self.reqs = reqs
        self.timeout = timeout
        self.retry = retry if retry > 1 else 1
        self.set_default_header()

    def set_default_header(self):
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) 12306-electron/1.0.1 Chrome/59.0.3071.115 Electron/1.8.4 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        self.headers.update(header)

    def advance_request(self, req=None, **options):
        if isinstance(req, str):
            req = self.reqs.get(req, {})
        elif not isinstance(req, dict):
            req = {}
        if "params" in req and "params" in options:
            params = options.pop("params")
            req["params"].update(params)
        if "data" in req and "data" in options:
            data = options.pop("data")
            req["data"].update(data)
        req.update(options)
        if "path" in req:
            path = req.pop("path")
            url = self.base_url.rstrip("/") + "/" + path.lstrip("/")
        elif "url" in req:
            url = req.pop("url")
        else:
            log.error("url not found!")
            return
        if "timeout" not in req:
            req["timeout"] = self.timeout
        for _ in range(self.retry):
            try:
                resp = self.request(url=url, **req)
                if resp.ok:
                    return resp
            except Exception as ex:
                log.error("advance request error: %s", ex)
            time.sleep(random.random())
