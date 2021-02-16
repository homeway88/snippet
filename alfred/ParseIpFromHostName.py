# encoding=utf8

# Parse ip from hostname
# Input params like 'mtee3011141031033.pre.oc27'
# which format is `${appName}${ip}.${env}.${region}`
# we can extract ip info from it
import re
import sys

demo_input = 'uniface011141031033.online.china'

if len(sys.argv) >= 2:
    input_str = sys.argv[1].strip()
else:
    input_str = demo_input

m = re.compile('(\\d{12})\.').search(input_str)
if m:
    g = m.group(1)
    seg1 = int(g[0:3])
    seg2 = int(g[3:6])
    seg3 = int(g[6:9])
    seg4 = int(g[9:12])
    ip = "{}.{}.{}.{}".format(seg1, seg2, seg3, seg4)
    sys.stdout.write(ip)
else:
    sys.stdout.write(input_str)
