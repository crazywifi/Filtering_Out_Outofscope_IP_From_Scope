import pyfiglet
from pyfiglet import fonts
import sys
import argparse
from termcolor import colored
from colorama import init

init()
G  = '\033[32m' 
O  = '\033[33m' 
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

#Sometime we face a situation where we have the list of IP addresses but some IP addresses are not reachable and client tell to take it as out of scope.
#So, if the IP addresses in scope is 600+, filter out scope IP address is task.

def banner():
    print (colored(pyfiglet.figlet_format("Scope IP Address Filter", font="standard"), "red"))
    print (G+BOLD+"By Rishabh Sharma [Follow: https://lazyhacker22.blogspot.com]\n"+END)

def scopefilter(scope2,outofscope2):
    ip = open(scope2,"r")
    ipread = ip.readlines()
    finalscope1 = open("Finalscope.txt","a")
    print ("Scope IP Addresses")
    for data in ipread:
        outofscope = open(outofscope2,"r")
        outofscoperead = outofscope.read()
        if data not in outofscoperead:
            print (data.rstrip())
            finalscope1.write(data)
    finalscope1.close()

def main():
    banner()
    parser = argparse.ArgumentParser(description='Filter out scope IP address from IP address list when you have out of scope IP address list')
    parser.add_argument('IPAddresslist', help='Scope IP address list which include all IP address (scope + out of scope)')
    parser.add_argument('outofscopelist', help='Out of scope IP address list')
    args = parser.parse_args()
    scope2 = args.IPAddresslist
    outofscope2 = args.outofscopelist
    scopefilter(scope2,outofscope2)
    
    
    
    
if __name__ =='__main__':
    main()
