import json
obj={"Skanda":12,"Boy":2012}
obx=["Skanda",12,2012,"boy"]
oby=("Skanda",12,2012,"boy")
obz="Skanda"
y=12
z=21.25
result=json.dumps(obj)
resultwo=json.dumps(obx)
resulthree=json.dumps(oby)
resultfour=json.dumps(obz)
resultfive=json.dumps(y)
resultsix=json.dumps(z)

print(result,resultwo,resulthree,resultfour,resultfive,resultsix)

