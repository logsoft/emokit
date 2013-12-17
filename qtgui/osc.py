# coding=utf-8
__author__ = 'hpl'
import logging
import liblo


class OscSend(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.host = None
        self.port = None
        self.target = None


    def openport(self, adress):
        self.host, self.port = adress.split(':')
        try:
            self.target = liblo.Address(self.host, self.port)
            self.log.debug('opened osc target: host:%s, port:%s' % (self.host, self.port))
        except liblo.AddressError, err:
            self.log.error('OSC Port error: %s' % err)


    def closeport(self):
        self.target = None


    def sendpacket(self, packet):
        if self.target is None:
            return

        for key in packet:
            if key != 'Unknown':
                adress = '/emotiv/' + key
                liblo.send(self.target, adress, packet[key]['value'])
                #self.log.debug('send osc')


