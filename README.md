# FTP-Python v1

A simple ftp server and ftp client in python

You must have the pyftpdlib and ftplib modules installed

# HOW TO CONFIGURE :

firstly you have to install the modules. For that you can use :

# pip install -r requirements.txt

secondly, set your ftp server, the ftp server requires several parameters:

the host, the port, the username, the password and the pathroot.

Exemple :

Linux :

# python3 serverftp.py localhost 21 root pass .

Windows :

# py serverftp.py localhost 21 root pass .

next, set your ftp client, like the ftp server, the ftp client requires several parameters :

the host, the username and the password.

Exemple :

Linux :

# python3 clientftp.py localhost root pass

Windows :

# py clientftp.py localhost root pass

# HOW TO USE :

you can download and upload files remotely with the client

upload <file>
download <file>
