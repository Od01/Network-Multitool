import os
import dns.resolver

def DNSCall(record_type, server):
    # clears the screen
    os.system('clear')

    while record_type == "A" or record_type == "NS" or record_type == "MX" or record_type == "TXT":
        record_type = record_type

        # define your functions for record lookups
        def dns_rec(record_type):
            domain = server # raw_input("Please put in a domain ")
            answers = dns.resolver.query(domain, record_type)

            for servers in answers:
                print servers

        # if statement for input
        if record_type == "A":
            return dns_rec(record_type == "A")
        if record_type == "NS":
            return dns_rec(record_type == "NS")
        if record_type == "MX":
            return dns_rec(record_type == "MX")
        if record_type == "TXT":
            return dns_rec(record_type == "TXT")
        else:
            "Please check your answer and make sure it matches one of the options above"

    else:
        print "Oops you typed in something incorrectly, try again."
        sys.exit()
