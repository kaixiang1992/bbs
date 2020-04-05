from flask import jsonify


class HttpCode(object):
    ok = 200  # TODO: 响应成功
    paramserror = 400  # TODO: 参数错误
    autherror = 401  # TODO: 鉴权失败
    servererror = 500  # TODO: 服务器错误


def ResponseUntil(code, message="", data={}):
    return jsonify({"code": code, "message": message, "data": data})


# TODO: 响应成功
def success(message="", data={}):
    return ResponseUntil(code=HttpCode.ok, message=message, data=data)


# TODO: 参数错误
def params_error(message="参数错误", data={}):
    return ResponseUntil(code=HttpCode.paramserror, message=message, data=data)


# TODO: 鉴权失败
def auth_error():
    return ResponseUntil(code=HttpCode.autherror)


# TODO: 服务器错误
def server_error(message="服务器错误", data={}):
    return ResponseUntil(code=HttpCode.servererror, message=message, data=data)
