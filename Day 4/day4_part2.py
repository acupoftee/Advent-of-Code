import hashlib

key = 'iwrupvqb'
n = 0

while True:
	h = hashlib.new('md5')
	h.update("%s%d" % (key, n))
	if h.hexdigest()[:6] == '000000':
		break
	n += 1
print n