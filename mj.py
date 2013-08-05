def readData( file, col=[0, 1], sep=" ", plot=False, v=False ):
    import numpy as np
    x=[]
    y=[]
    print "Reading", file, "...",

    file_data=open( file ,"r")
    for line in file_data.readlines():
        data = line.split( sep );
        if v==True:
            print data
            
        x.append( float(data[col[0]]) )
        y.append( float(data[col[1]]) )
    
    file_data.close()
    print "Done."

    if plot==True:
        print "Plotting", file, "...",
        import matplotlib.pyplot as plt
        plt.plot(x,y,label=file)
        plt.legend()
        plt.show()
        print "Done."

    return [ np.array(x), np.array(y) ]

def interp( x, y, step, plot=False ):
    from scipy import interpolate
    import numpy as np
    print "Interpolating:",
    xmin = np.min(x)
    xmax = np.max(x)
    print " range(", xmin,"-",xmax,") step(",step,")",
    xint = np.arange( xmin, xmax, step )
    f = interpolate.interp1d( x, y )
    yint = f( xint )
    print "Done."
    if plot==True:
        print "Plotting interpolation ...",
        import matplotlib.pyplot as plt
        plt.plot(x,y,".",label="data")
        plt.plot(xint,yint,"-",label="interpolation")
        plt.legend()
        plt.show()
        print "Done."

    return [ np.array(xint), np.array(yint), f ]

def simpleIntegrate( x, y ):
    import numpy as np
    print "Simple integration:",
    step=x[1]-x[0]
    print " step(", step, ")",
    sum = 0
    for i in y:
        sum += i
        
    int = sum*step
    print " value(", int, ") Done." 
    return float(int)

def simpleIntegrateWBorders( x, y, x_min, x_max ):
    import numpy as np
    print "Simple integration:",
    step=x[1]-x[0]
    print " step(", step, ")",
    sum = 0
    for i in range(len(x)):
        if x[i] > x_min and x[i] < x_max:
            sum += y[i]
        
    int = sum*step
    print " value(", int, ") Done." 
    return float(int)

def plotData( x, y, style="-" ):
    print "Plotting ...",
    import matplotlib.pyplot as plt
    plt.plot(x,y,style)
    plt.show()
    print "Done."
    
def normalize( x ):
    import numpy as np
    print "Normalize data ...",
    return np.array(x)/np.max(x)
    print "Done."

def cutData( x, y, xmin, xmax ):
    import numpy as np
    print "Extracting data in range (",xmin,"-",xmax,") ... ",
    _x=[]
    _y=[]
    for ii in range(len(x)):
        if x[ii] > xmin and x[ii] < xmax:
            _x.append( x[ii] )
            _y.append( y[ii] )

    print "Done."
    return [ np.array(_x), np.array(_y) ]

#np.savetxt("nsb_gapd_folded.dat",np.transpose(np.vstack([x,folded])))
