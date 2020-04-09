from redis import Redis

# TODO: 初始化redis
cache = Redis(host='192.168.184.128', port=6379, password='ceshi1')


# TODO: 设置
def set(key, value, ex=60):
    return cache.set(name=str(key), value=str(value))


# TODO: 读取
def get(key):
    return cache.get(name=key)


# TODO: 删除
def delete(key):
    return cache.delete(key)
