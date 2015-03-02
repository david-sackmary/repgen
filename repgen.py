#!/usr/bin/python
# Report generator
import api
import fn
import sys
import dumper

def main(argv):
    config = {}
    config["usagetext"] = ("repgen.py (-s SEARCHPREFIX|-a) [-c CONFIGFILE]\n"+
            "  This script generates a report for all servers if -a is used,\n"+
            "or just the servers with SEARCHPREFIX in the server label if -s is used.\n\n"+
            "Make sure you correctly configure config.conf.\n"+
            "you can use -c to specify a different configuration file.  Otherwise, ./config.conf is assumed.\n\n"
            "In config.conf: search_field will determine the metadata field that SEARCHPREFIX is applied to\n"+
            "  to create the list of servers that will be reported on.\n"+
            "The output configuration value  will determine the output format for the information.\n"+
            "  Text is mainly for debugging and may not produce as much meaningful information as html or pdf.\n"+
            "  HTML and PDF files are placed in the ./outfile folder.  If it doesn't exist, the script will fail.")
    config["configfile"] = "config.conf"
    serverolist = []
    config = fn.set_config_items(config,argv)
    serverolist = fn.build_server_list(config['host'], config['authtoken'], config['search_string'], config['search_field'], config['prox'])
    serverolist = fn.enrich_server_data(config['host'], config['authtoken'], serverolist, config['prox'])



#    for s in serverolist:
#        print s.issues





# Here we re-write the config if the logo file is on the local filesystem, because relative paths don't work well with PDF rendering.
    if fn.where_is_img(config['logo_url'])[0] == 'local' and config['output'] == 'pdf':
        try:
            config['logo_url'] = fn.where_is_img(config['logo_url'])[1]
        except:
# Here we empty that field in case the data was bad...
            config['logo_url'] = ''
    fn.handle_output(config, serverolist)

if __name__ == "__main__":
    print sys.argv[1:]
    main(sys.argv[1:])
