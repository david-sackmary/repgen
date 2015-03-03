#!/usr/bin/python
# This is where all of our printout magic happens

import json
import markdown
import cruncher
import fn
import operator
import itertools
import time
import sys


def write_out(prefix, formt, content):
    engine = ''
    try:
        from xhtml2pdf import pisa
        engine = 'x2p'
    except:
        pass
    try:
        import pdfkit
        engine = 'pdfkit'
        print "Successfully initialized pdfkit."
    except:
        pass
    fullname = './outfiles/' + str(prefix)+'.'+str(formt)
    if formt == 'pdf':
        if engine == '':
            print '''\n\nERROR: No PDF rendering engines available.\n
            Supported engines: xhtml2pdf and pdfkit.\n
            Please change output format or install a supported rendering engine'''
            sys.exit(2)
        elif engine == 'x2p':
            r = open(fullname, 'w+b')
            pisa_status = pisa.CreatePDF(content, dest=r)
            r.close()
            if pisa_status == False:
                print "Bad stuff happened. PDF may not have been written"
            else:
                print fullname + " has been created using xhtml2pdf!"
        elif engine == 'pdfkit':
            try:
                pdfkit.from_string(content, fullname)
                print fullname + " has been created using pdfkit!"
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                print "Make sure you've installed wkhtmltopdf binaries and they're in your PATH!"
                sys.exit(2)
    else:
        f = open(fullname, 'w')
        f.write(content)
        f.close
        print "Wrote output file: " + fullname


def html(objex,prefix,formt,logo_url):
    raw_reports = {}
    tstamp = str(time.strftime("%Y-%m-%d %H:%M"))
    complete_contents = ''
    head = '''<html><head>
    <meta name="pdfkit-orientation" content="Landscape"/>
    <style>
    @page {size:letter landscape;
           margin: 2cm;
               }
    table {table-layout: fixed;
           width: 100%;}
    td    {border: 1px solid black;
           border-collapse: collapse;
           padding-left: 5px;
           padding-top: 5px;
           padding-right:5px;
           word-wrap:break-word;}
    p     {word-wrap:break-word;}
    body  {padding-left: 20px;}
    </style>
                </head><body>
                '''
    closer = '</body></html>'
    logo = '![Logo](' + logo_url + ')\n'
    masthead_firewall = "#Firewall Report\n##" +tstamp
    print "before cruncher"
    fw_summary, fw_detail = cruncher.all_server_stats(objex)
    print "after cruncher"
    summary_fw = str(generate_summary_content(firewall_summary))
    print "after summary"
    for s in objex:
        server = generate_server_content(s)
        complete_contents = complete_contents + str(str(server))
        
    

def generate_summary_content(firewall):
    ret_firewall =''
    fw_count = ''
    fw_name = ''
    s
    for entry in firewall:
        fw_count = entry['count']
        fw_name = fw_name + str('\n1. [' + str(entry['firewall_policies']['name']) +']')
        
    ret_firewall = str(fw_count) + str(fw_name)
    
    return ret_firewall

def generate_server_content(s):
    mdown_server = ''
    servername = s.name
    serverid= s.id
    serverlabel = s.label
    servergroup = s.group_name
    issues = s.issues #not sure if we need this
    
    mdown_server = mdown_server + '\n\n##Host Name: ' + str(servername) + '\n\n###Label:' + str(serverlabel) +'\n\n###Group' + str(servergroup)
    return mdown_server

    