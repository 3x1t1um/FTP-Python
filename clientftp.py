#-*- coding:utf-8 -*-
"""
By 3x1t1um

ftp client

"""

import os
from ftplib import FTP
from ftplib import FTP_TLS
import argparse
import sys

def main(ftphost, ftpuser, ftppass):
	log = FTP(ftphost)
	log.login(ftpuser, ftppass)

	while 1:
		command = input('ftp@root ~# ')

		if command[0:6]== 'upload':
			file = command[7:]
			checkfile = os.path.exists(file)
			if checkfile == False:
				print('>> Error !')
			else:
				try:
					fileop = open(file,'rb')
					log.storbinary('STOR '+file, fileop)
					fileop.close()
					print('>> Succes !')
				except Exception as errorul:
					print(errorul)

		elif command[0:8] == 'download':
			try:
				file = command[9:]
				fileop = open(file, 'wb')
				log.retrbinary('RETR ' +file, fileop.write)
				fileop.close()
				print('>> Succes !')
			except Exception as errordl:
				print(errordl)

		elif command == 'exit':
			log.quit()
			sys.exit(1)


if __name__ == '__main__':
	pars = argparse.ArgumentParser()
	pars.add_argument('host',type=str, help='Set your FTP Host')
	pars.add_argument('user',type=str,help='Set your FTP User')
	pars.add_argument('password',type=str,help='Set your FTP Password')
	setall = pars.parse_args()

	main(setall.host, setall.user, setall.password)

