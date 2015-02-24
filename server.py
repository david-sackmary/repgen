
#!/usr/bin/python

class Server():
    def __init__(self, hostname, serverid, serverlabel, servergroupname):
        self.name = hostname
        self.id = serverid
        self.label = serverlabel
        self.group_name = servergroupname
        self.issues = ''
