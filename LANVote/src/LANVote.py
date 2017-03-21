#!/usr/bin/env python
# coding=utf8 
############################################################################################# 
# This file used for send some request for target html
# This programe using the character that target proxy connetion internet with dynamic IP,
# e.g:SEU bras
# using this script to update ip address automation and vote with different ip addr.
#############################################################################################
import httplib, urllib

class LANVote(object):
    # TODO:
    # add a connection mornator or add an trigger which will reconnect after lost connection with host
    def __init__(self, hostname, port = 80, timeout = 10):
        self.httpClientConnection = self.__httpClientConnetion(hostname, port, timeout)
        self.params = dict()
        self.request_headers = dict()

    def add_params(self, key, value):
        self.params[key] = value

    def set_headers(self, _headers = dict()):
        self.request_headers = _headers

    def __httpClientConnetion(self, hostname, port = 80, timeout = 10):
        try:
            return httplib.HTTPConnection(hostname, port, timeout)
        except httplib.InvalidURL:
            print "Connection to host:%s failed, \nplease reset a correct connection information " % (hostname)
            return None

    @property
    def request_params(self):
        return urllib.urlencode(self.params)

    def send_request(self, request_url,request_type = 'POST', params = None, headers = None, ):
        try:
            self.httpClientConnection.request(request_type, request_url, 
                                            params if params else self.request_params, 
                                            headers if headers else self.request_headers)
            return self.httpClientConnection.getresponse()
        except httplib.CannotSendRequest:
            print "Cannot Send Request to Target Server"
        except urllib2.URLError,e:
            print "The url cannot opened"
        except Exception,e:
            print e
        finally:
            return None
    def __del__(self):
        if self.httpClientConnection:
            self.httpClientConnection.close()

