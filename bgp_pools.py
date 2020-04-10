from jnpr.junos import Device
from lxml import etree

def recursive_dict(element):
     return element.tag, dict(map(recursive_dict, element)) or element.text

def main():
    jdev = Device()
    jdev.open()
    rsp = jdev.rpc.walk_snmp_object(snmp_object_name='.1.3.6.1.4.1.2636.3.51.1.1.4.1.1')
    pre = {}
    c = 0
    for item in rsp:
        indexvalue = item.xpath("//snmp-object//index//index-value")[c].text
        tname = item.xpath("//snmp-object//name")[c].text
        value = item.xpath("//snmp-object//object-value")[c].text
        tname = tname.split(".")
        id = tname[1]
        name = tname[0].replace("jnxUserAAAAccessPool","")
        if id in pre:
                pre[id].update({name : value})
        else:
                pre[id] = {name : value}
        c = c + 1
    jdev.close()

    space = 18
    print "RoutingInstance".ljust(space) + "Pool Name".ljust(space) + "Network".ljust(space) + "AddressesInUse".ljust(space) + "AddressTotal".ljust(space) + "AddressUsageHigh".ljust(space) + "LinkName".center(space) + "OutOfAddresses".ljust(space) + "AddressUsageAbate".ljust(space)
    for t in pre:
        print pre[t]['RoutingInstance'].ljust(space) + pre[t]['Name'].ljust(space) + pre[t]['InetNetwork'].ljust(space) + pre[t]['AddressesInUse'].center(space) + pre[t]['AddressTotal'].center(space) + pre[t]['AddressUsageHigh'].center(space) + str(pre[t]['LinkName']).center(space) + pre[t]['OutOfAddresses'].center(space) + pre[t]['AddressUsageAbate'].center(space)

if __name__ == '__main__':
    main()
