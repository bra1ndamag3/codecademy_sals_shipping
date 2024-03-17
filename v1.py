#ground shipping
weight=41.5
cost=""
if weight>=10:
  cost=weight*4.75
elif weight>=6:
  cost=weight*4
elif weight>=2:
  cost=weight*3
else:
  cost=weight*1.5
print("Ground Shipping: ")
print(cost+20)
premium_shipping=125
print("Premium Shipping: ")
print(premium_shipping)
#drone shipping
if weight >= 10:
  cost=weight*14.5
elif weight >= 6:
  cost=weight*12
elif weight >=2:
  cost=weight*9
else:
  cost=weight*4.5
print("Drone Shipping Cost:")
print(cost)
  
