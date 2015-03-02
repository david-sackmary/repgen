#!/usr/bin/python
# We use these functions for crunching data

from operator import itemgetter
from collections import OrderedDict
import json

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
	    firewall = s.issues
	    rules = s.details[1]
            print "dave"
            print firewall
            print "dave"
	    print json.dumps(rules, indent = 2)
        except:
            continue
    return firewall_summary, firewall_detail


