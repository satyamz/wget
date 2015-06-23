from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
import threading
import socket

class StoppableFTPServer(FTPServer):
    def server_conf(self, filelist, conf_dict):
        self.server_configs = conf_dict
        self.fileSys = filelist

class _FTPHandler(FTPHandler):
    def pre_process_command(self, line, cmd, arg):
        """
        Overriding method to remove filesystem dependencies
        """
        if self.proto_cmds[cmd]['perm'] :
            if cmd == 'CWD':
                arg = "/"
            elif cmd == 'LIST':
                arg = "/"
            else:
                arg = "/"

        self.process_command(cmd,arg)


class FTPd(threading.Thread):
    server_class = StoppableFTPServer
    handler = _FTPHandler
    handler.use_sendfile = False

    def __init__(self, addr=None):
        #home = self.server_class.filelist
        #authorizer = DummyAuthorizer()
        #authorizer.add_anonymous(home)
        #handler.authorizer = authorizer
        threading.Thread.__init__(self)
        if addr is None:
            addr = ('localhost',0)
            self.server_inst = self.server_class(addr,self.handler)
            self.server_address = self.server_inst.socket.getsockname()[:2]
		
    def run(self):
        self.server_inst.serve_forever()
	
    def server_conf(self, file_list, server_rules):
        self.server_inst.server_conf(file_list, server_rules)
