try:
	with open("/usr/lib/libjudger.so", "rb") as f:
		print(f.read()[:10])
except Exception as e:
	print(e)
