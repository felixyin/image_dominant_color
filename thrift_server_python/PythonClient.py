from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

from imagecolor import ImageColor

if __name__ == '__main__':
    print('client ...')
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = ImageColor.Client(protocol)

    # Connect!
    transport.open()

    color = client.getColor('sjklfdjk')
    print('color: ' + color)

    # Close!
    transport.close()
