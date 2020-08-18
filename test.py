from pymemcache.client import base

client = base.Client(('localhost',11211))

foo = client.get('domain-macx.work')

print(foo)
