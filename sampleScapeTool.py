from scapy.all import *

ap_list = []

def PacketHandler(pkt) :

  if pkt.haslayer(Dot11) :
            if pkt.type == 0 and pkt.subtype == 8 :
                if pkt.addr2 not in ap_list :
                            ap_list.append(pkt.addr2)
                            print ("AP MAC: {pkt.addr2} with SSID: {pkt.info} "

sniff(iface="mon0", prn = PacketHandler)
