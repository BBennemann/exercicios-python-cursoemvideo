import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim n esta acessivel no momento')
else:
    print('Consegui acessar o site Pudim')