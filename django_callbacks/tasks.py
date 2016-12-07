'''
Created on 2016年12月7日

@author: xumingze
'''

import logging

from django.core import signals

from celery import app

logger = logging.getLogger("default")


class CallbackTask(object):

    def __init__(self):
        self.times = 0

    def add_task(self, *func, **kwargs):
        if not func:
            return False
        self.func = func
        self.kwargs = kwargs
        return True

    @app.task
    def start_task(self):
        try:
            print("start")
            signals.request_started.send(self)
            self.func(**self.kwargs)
        except BaseException as exc:
            logger.exception(exc)
            print("task.retry")
            if self.times < 20:
                # 如果self.func执行失败，延时5*times秒再次执行一次
                raise self.func.retry(countdown=5 * self.times, exc=exc)
                self.times = self.times + 1
            logger.exception('无法连接服务器...')
        finally:
            signals.request_finished.send(self)
            print("end")
