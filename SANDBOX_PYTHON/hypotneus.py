import nthroot
'''
Calculate 2-d hypotneus
'''
coordinates= [[1,30], [2,35]]
def calc2d_hypptneus(coordinates):
    
    base=coordinates[0][0] - coordinates[1][0]
    height=coordinates[0][1] - coordinates[1][1]
    hypotneus=nthroot.nthrt(2,base**2+height**2,0.001)
    return hypotneus


print(calc2d_hypptneus(coordinates))