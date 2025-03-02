'''
Designing thermometer
when current 1, the teperature was 30
when currrent 2, the temperature was 35
when current will be 3, what would be the temperature 40
current = 4, temp = 45
current 2.1, temp = 35.5
''' 
'''
Given two points are lineraly dependent, it couls be a linear equation 
like y=mx+c

Given two points in the line, we can find the equation of the line
as below

mx1 + c = y1
mx2 + c = y2

m(x1 -x2) = y1 -y2

m= (y1-y2)/(x1-x2)

c= y1 - mx1

'''
calibration_data = [[1,30], [2,35]]
def tell_temp(calibration_data, current):
    
    y1,y2=calibration_data[0][1],calibration_data[1][1]
    x1,x2=calibration_data[0][0],calibration_data[1][0]

    m= (y2-y1)/(x2-x1)

    c= y1-m*x1
    temperature=(m*current) + c
    
    return temperature

print(tell_temp(calibration_data,4))
print(tell_temp(calibration_data,2.1))