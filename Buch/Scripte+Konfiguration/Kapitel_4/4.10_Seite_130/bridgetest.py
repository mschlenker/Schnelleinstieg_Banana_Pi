#!/usr/bin/python
import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient
key = "messwert"
brg = bridgeclient()
print brg.get(key)
