!/usr/bin/env python
import os
import os
import sys
 
ip = '127.0.0.1'
sock = socket.socket()
sock.bind((ip, 9090))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "composeexample.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
