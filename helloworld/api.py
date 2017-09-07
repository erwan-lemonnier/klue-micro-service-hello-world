import logging
from klue.swagger.apipool import ApiPool


log = logging.getLogger(__name__)


def do_hello():
    return ApiPool.helloworld.model.Hello(message='Hello world!')


def do_crash():
    raise Exception("OH! NO! I JUST DIED!!")
