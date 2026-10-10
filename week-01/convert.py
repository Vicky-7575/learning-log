import math

x = input("Enter RPM: ")
fx = float(x)
radius = 0.4572  # in meters

def rpm_rds(rpm):
    rad = rpm * ((2 * math.pi) / 60)
    return(rad) 
def rpm_kmph(rpm):
    kil = (3/25) * math.pi * radius * rpm
    return(kil)


xr = round(rpm_rds(fx),2)
xk = round(rpm_kmph(fx),2)
print(xr, "rd/s")
print(xk, "km/h")



