#! /usr/bin/python3

from monitor import *
import time
import sys




def logTemp():
    count = len( sys.argv )
    print( "count=={}  sys.argv[0]={}".format( count, sys.argv[0] ))

    if count < 2 :
        filename = "log.csv"
    else:
        filename = sys.argv[1]

        
    if not filename.endswith( "csv" ) : filename = "%s.csv" % filename
    print( "Logging to %s, press Ctrl-C to stop logging..." % filename )

    # open for write and erase if it already exists...
    file = open( filename, "w+" )
    monitor = MonitorPi()

    try: 
        while True:
            clear()
            print( monitor.getStats() )
            text = "{}, {}\n".format( monitor.time, monitor.temp )
            file.write( text )
            time.sleep(2)        

    except KeyboardInterrupt:
        print( "\nDone." );

    finally:
        file.close()



logTemp()
    
