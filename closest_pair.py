import operator
import math
def squared_distance(p, q):
    '''Returns the squared distance between points p and q'''
    (px, py), (qx, qy) = p, q
    return (px - qx)**2 + (py - qy)**2

def closest_pair(points):
    ''' 
    Input:  points | tuple of at least 2 points of the form (x, y)
    Output: smallest squared distance between any pair of points
    '''
    ##################
    # YOUR CODE HERE #
    ##################     
    return closest(sorted(points,key=operator.itemgetter(0,1)))

def closest(points):
    n=len(points)
    if(n==2):
        return squared_distance(points[0],points[1])
    if(n<=1):
        return 1e7
    dl=(closest_pair(points[:n//2]))
    dr=(closest_pair(points[n//2:]))
    delta=min(dl,dr)
    med=points[(n//2)][0]
    l=med-int(math.sqrt(delta))
    r=med+int(math.sqrt(delta))    
    ver_strip=[]
    for point in points:
        if(point[0]>=l and point[0]<=r):
            ver_strip.append(point)    
    dm=delta
    for i in range(0,len(ver_strip)):
        dist=1e7
        for j in range(1,10):
            if(i+j < len(ver_strip)):
                dist=min(dist,squared_distance(ver_strip[i],ver_strip[i+j]))            
        if(dist<dm):
            dm=dist
    return int(dm)

