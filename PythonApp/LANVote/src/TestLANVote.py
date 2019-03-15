#!/usr/bin/env python
# coding=utf8 
from LocalIPAddress import reset_ip_addr
from LANVote import LANVote
import time

def testVote():
    # prepare the request information
    # params = {'event_group_id':'710'}

    headers = dict()
    headers["Content-type"] ="application/x-www-form-urlencoded"
    headers["Accept"]= "text/html"

    voteClient = LANVote(hostname = "www.iarchis.com", port = 80, timeout = 10)
    voteClient.set_headers(headers)
    voteClient.add_params(  key = 'event_group_id',
                            value = '710')

    response = voteClient.send_request(request_type = 'POST',
                        request_url = "/index.php?m=event&a=comments_num")

    del voteClient
    return response

def vote_with_loop(_totlecount = 1000, trytime = 5):
    totlecount = 0
    while totlecount < _totlecount:
        reset_ip_addr(netadapter="localInternet", static=True, addr="169.252.231.116", mask = '255.255.255.0', waittime = 1)
        time.sleep(1)
        response = testVote()
        if response!=None:
            print "data:", response.read()
            print response.getheaders() #获取头信息
            totlecount += 1
        else:
            print "Response Error"

if __name__ == '__main__':
    vote_with_loop()