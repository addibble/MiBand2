import sys
import time
from base import MiBand2
from constants import ALERT_TYPES
from datetime import datetime

MAC = sys.argv[1]

band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")

if len(sys.argv) > 2:
    if band.initialize():
        print("Init OK")

band.authenticate()

#print 'getting data'
#print 'Soft revision:',band.get_revision()
#print 'Hardware revision:',band.get_hrdw_revision()
#print 'Serial:',band.get_serial()
#print 'Battery:', band.get_battery_info()
#print 'Time:', band.get_current_time()
#print 'Steps:', band.get_steps()

band.record_data()
