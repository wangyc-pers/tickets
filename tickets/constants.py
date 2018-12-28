# coding=utf-8

BASE_URL = "https://kyfw.12306.cn/"
PATHS = {
    "auth": {
        "path": "/passport/web/auth/uamtk",
        "method": "post",
    },
    "login": {
        "path": "/passport/web/login",
        "method": "post",
    },
    "left_ticket_init": {
        "path": "/otn/leftTicket/init",
        "method": "post",
    },
    "login_check": {
        "path": "/passport/captcha/captcha-image64",
        "method": "get",
        "params": {"login_site": "E", "module": "login", "rand": "sjrand"},
    },
    "order_check": {
        "path": "/passport/captcha/captcha-check",
        "method": "post",
    },
    "login_init": {
        "path": "/otn/login/init",
        "method": "get",
    },
    "user_info": {
        "path": "/otn/index/initMy12306",
        "method": "get",
    },
    "user_login": {
        "path": "/otn/login/userLogin",
        "method": "get",
    },
    "uamauth_client": {
        "path": "/otn/uamauthclient",
        "method": "post",
    },
    "init_dc": {
        "path": "/otn/confirmPassenger/initDc",
        "method": "get",
    },
    "get_js": {
        "path": "/otn/HttpZF/GetJS",
        "method": "get",
    },
    "odxmfwg": {
        "path": "/otn/dynamicJs/odxmfwg",
        "method": "get",
    },
    "rider_info": {
        "path": "/otn/confirmPassenger/getPassengerDTOs",
        "method": "get",
    },
    "ticket_query": {
        "path": "/otn/ticketQuery",
        "method": "get",
    },
    "user_check": {
        "path": "/otn/login/checkUser",
        "method": "post",
    },
    "order_submit": {
        "path": "/otn/leftTicket/submitOrderRequest",
        "method": "post",
    },
    "order_info": {
        "path": "/otn/confirmPassenger/checkOrderInfo",
        "method": "post",
    },
    "ticket_remain": {
        "path": "/otn/confirmPassenger/getQueueCount",
        "method": "post",
    },
    "order_queue": {
        "path": "/otn/confirmPassenger/confirmSingleForQueue",
        "method": "post",
    },
    "order_verify": {
        "path": "/otn/passcodeNew/getPassCodeNew",
        "method": "post",
        "params": {"module": "passenger", "rand": "randp"}
    },
    "order_wait": {
        "path": "/otn/confirmPassenger/queryOrderWaitTime",
        "method": "get",
        "params": {"tourFlag": "dc", "_json_att": ""}
    },
    "order_query": {
        "path": "/otn/queryOrder/queryMyOrderNoComplete",
        "method": "post",
    },
    "order_list": {
        "path": "/otn/queryOrder/initNoComplete",
        "method": "post",
    },
    "order_cancel": {
        "path": "/otn/queryOrder/cancelNoCompleteMyOrder",
        "method": "post",
    },
    "order_autocommit": {
        "path": "/otn/confirmPassenger/autoSubmitOrderRequest",
        "method": "post",
    },
    "order_async_list": {
        "path": "/otn/confirmPassenger/getQueueCountAsync",
        "method": "post",
    },
    "order_async_queue": {
        "path": "/otn/confirmPassenger/confirmSingleForQueueAsys",
        "method": "post"
    }
}