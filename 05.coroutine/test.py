# 协程


def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 ok'


def product(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()

c = consumer()
product(c)
