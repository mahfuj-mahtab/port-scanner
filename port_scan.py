from optparse import OptionParser
import socket

def port_scan(trgtsite, port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((trgtsite, port))
        print('%d port is open' %(port))
    except:
        port=port+1
    finally:
        sock.close() 




def main():
    parser=OptionParser('Uasges : -i <Ip address> \n -F <Fast scan>')
    parser.add_option('-i', '--ip', dest='trgtsite', type='string', help='Please type your target website')
    (options, args)=parser.parse_args()
    trgtsite=options.trgtsite

    if(trgtsite == None):
        print(parser.usage)
    else:
        for port in range(1,65635):
            port_scan(trgtsite,port)


main()
