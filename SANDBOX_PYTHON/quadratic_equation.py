'''
ax1*2 + bx1 + c = y1
ax2*2 + bx2 + c = y2
ax3*2 + bx3 + c = y3

a(x1*2 - x2*2) + b(x1 - x2)= y1 - y2

a(x1 + x2) + b = (y1 - y2)/(x1 - x2)
a(x2 + x3) + b = (y2 - y3)/(x1 - x2)

a(x1 - x3)=  (y1 - y2)/(x1 - x2) - (y2 - y3)/(x1 - x2)
a = ((y1 - y2)/(x1 - x2) - (y2 - y3)/(x2 - x3))/x1 - x3

b= (y1 - y2)/(x1 - x2) - a(x1 + x2)

c = y1 - (ax1*2 + bx1)



'''

def fit_qudratic(data):
    m1=data[0][1] - data[1][1]
    m2= data[1][1] - data[2][1]
    m1 = (data[0][1] - data[1][1]) / (data[0][0] - data[1][0])
    m2 = (data[1][1] - data[2][1]) / (data[1][0] - data[2][0])

    a=((m1) - (m2))/(data[0][0] - data[2][0])
    b = m1 - a*(data[0][0] + data[1][0])
    c= data[0][1] - (a*(data[0][0]**2) +b*data[0][0])
    return [a,b,c]





def predict(model,x):
    a,b,c = model
    return a*x**2 + b*x + c

calibration_data = [[0,10], [1,15],[2,30]]
print(fit_qudratic(calibration_data))
model = fit_qudratic(calibration_data)
input = 3
print(predict(model,3))
print(predict(model,4))