from haishoku.haishoku import Haishoku
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

from imagecolor import ImageColor


class ImageColorHandler:
    def __init__(self):
        self.log = {}

    def getColor(self, imagePath):
        dominant = Haishoku.getDominant(imagePath)
        color = dominant.__str__().replace('(', '').replace(')', '')
        print('--------------------> getColor(%s) = %s' % (imagePath, color))
        return color


if __name__ == '__main__':
    handler = ImageColorHandler()
    processor = ImageColor.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server')
    server.serve()
    print('done')

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
