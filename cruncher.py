#!/usr/bin/python
# We use these functions for crunching data

from operator import itemgetter
from collections import OrderedDict

def all_server_stats(servers):
    all_cves = []
    all_crit_pkgs = []
    all_noncrit_pkgs = []
    retval_cve = {}
    retval_crit_pkg = {}
    retval_noncrit_pkg = {}
    for s in servers:
        try:
	    id = []
            firewall = s.issues['firewall_policies']
            print "dave"
            print firewall
            print "dave"
        except:
            continue
    return


