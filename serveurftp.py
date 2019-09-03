from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import argparse

def connect(host,port,user,password,pathroot):
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, pathroot, perm="elradfmwMT")
    authorizer.add_anonymous(".", perm="elradfmwMT")
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((host, port), handler)
    server.serve_forever()


if __name__ == '__main__':
	pars = argparse.ArgumentParser()
	pars.add_argument('host',type=str, help='Set your FTP Host')
	pars.add_argument('port',type=str,help='Set your FTP Port')
	pars.add_argument('user',type=str,help='Set your FTP User')
	pars.add_argument('password',type=str,help='Set your FTP Password')
	pars.add_argument('pathroot',type=str,help='Set your FTP Password')
	setall = pars.parse_args()
	connect(setall.host, setall.port, setall.user, setall.password, setall.pathroot)
