# -*- coding: utf-8 -*-


class ForumException(Exception):
    """ BlueKing Forum 异常基类 """
    pass


class InvalidOperationError(ForumException):
    """ 不合法操作错误, 常出现于业务逻辑错误 """
    pass
