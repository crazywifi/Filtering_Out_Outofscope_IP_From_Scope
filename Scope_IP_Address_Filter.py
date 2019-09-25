#/usr/bin/python

#Sometime we face a situation where we have the list of IP addresses but some IP addresses are not reachable and client tell to take it as out of scope.
#So, if the IP addresses in scope is 600+, filter out scope IP address is task.

ip = open("scope.txt","r")
ipread = ip.readlines()
print "Scope IP Addresses"
for data in ipread:
    outofscope = open("outofscope.txt","r")
    outofscoperead = outofscope.read()
    if data not in outofscoperead:
        print data.rstrip()


