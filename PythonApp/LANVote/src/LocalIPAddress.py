import os
import time

"""
@param netadapter
@param source = static | dhcp
@param addr  new ip address
@param mask  subnetwork num defaul value is 255.255.255.0
@param waittime 1s
"""
def reset_ip_addr(netadapter, static, addr, mask = '255.255.255.0', waittime = 1):
	source = 'static' if static else 'dhcp'
	commend = 'netsh interface ip set address name=%s source=%s ' % (netadapter, source)
	commend = commend if not static else (commend+"addr=%s mask=%s" % (addr,mask))

	os.system(commend)
	# os.system('netsh interface ip set address name="localInternet" source=dhcp')
    # os.system('netsh interface ip set dns name="localInternet" source=dhcp')
	time.sleep(waittime)

def test_reset_ip_addr():
	reset_ip_addr(netadapter="localInternet", static=True, addr="169.252.231.116", mask = '255.255.255.0', waittime = 1)
    
