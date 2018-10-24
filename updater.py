import subprocess
import os
import time

def update_repo():
	output = subprocess.run(['git','config','user.email' , "rajatthepagal@gmail.com"], stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(output)
	output = subprocess.run(['git','config','user.name' , 'rajatkb'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(output)
	output = subprocess.run(['git','pull'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(output)
	output = subprocess.run(['git','add','.'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(output)
	output = subprocess.run(['git','commit','-m', '"new stuff"'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(output)
	output = subprocess.run(['git','push'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(output)

def process():
	stamp = 0
	filename = 'README.md'
	while True:
		new_stamp = os.stat(filename).st_mtime
		if stamp != new_stamp:
			stamp = new_stamp
			print("log: file was changed")
			update_repo()
		time.sleep(500)

process()