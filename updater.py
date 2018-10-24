import subprocess

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


