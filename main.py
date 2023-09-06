import platform, time, requests, os, wget

session = requests.Session()
machine = platform.uname().machine
path = os.path.join(os.curdir, "runtah")
if not os.path.exists(path):
	os.mkdir(path)

def get_size(number_size):
	for memeg in ["B", "KB", "MB", "GB", "TB"]:
		if number_size < 1024.0:
			return "%3.1f %s" % (number_size, memeg)
		number_size /= 1024.0

def donlot(url="https://raw.githubusercontent.com/Mark-Zugbreg/stfu/main/filekrek/", block_size=1024, baru=0):
	res = session.get((lambda i: url + i + "bit/run")("64" if machine == 'aarch64' else "32"), stream=True)
	_file_size = int(res.headers["Content-Length"])
	if os.path.exists(path + "/run") is True:
		if os.path.getsize(path + "/run") == _file_size:
			os.system(f"mv {path}/run .")
			os.system(f"rm -rf {path}")
			os.system("chmod 775 run")
			print(f" [*] jalankan ulang {__file__.split('/')[-1]}")
			exit(os.system(f'''echo '__import__("os").system("./run")' > {__file__}'''))
		#session.headers["Range"] = f"bytes={os.path.getsize('run')}-{_file_size}"
	#os.system(f'wget {(lambda i: url + i + "bit/run")("64" if machine == "aarch64" else "32")} -O run'); donlot()
	wget.download((lambda i: url + i + "bit/run")("64" if machine == "aarch64" else "32"), out="runtah"); donlot()
	if session.headers.get("Range"):
		res = session.get((lambda i: url + i + "bit/run")("64" if machine == 'aarch64' else "32"), stream=True)
	file_size = int(res.headers["Content-Length"])
	print("\n sorry ya cuy, sizenya bengkak coeg:'v\n\n")
	with open("run", "ab" if session.headers.get("Range") else "wb") as f:
		for memek in res.iter_content(block_size):
			baru += len(memek)
			for s in ["|","/","-","\\","*","?"]:
				print(f"\r [{s}] download {int(baru / file_size * 100)}% ({get_size(baru)}) ({get_size(file_size)})", end="")
				time.sleep(0.1)
			f.write(memek)
		f.close()
	if os.path.getsize("run") == _file_size:
		exit(os.system(f"echo 'import os\nos.system('./run)' > {__file__}"))
	donlot()

if __name__ == "__main__":
	donlot()
