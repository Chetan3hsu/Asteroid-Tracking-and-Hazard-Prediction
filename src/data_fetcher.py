import requests , json
from datetime import datetime , date
req = requests.request('GET',
                        'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=4y5bdem1qhFwpRT2Uc0QwoPhHdelRDaBVk5FgLVr')
ourData=req.json()
with open('data.json' , 'w') as f:
    json.dump(ourData , f , indent=4)
asteriodList=[]
names=[]
diameter=[]
hazardous=[]
distance=[]
dateClosest=[]
velocity=[]
def additionalData(aste):
     newList=[]
     dict={}
     entry=aste.get("close_approach_data")
     for dt in entry:
          if datetime.strptime(dt.get('close_approach_date'), '%Y-%m-%d').date() > date.today():
            newList.append(dt)
     if newList:            
          dict=min(newList , key=lambda x: (x.get('miss_distance').get('astronomical'))) 
         
     return dict 
   
def fetchData():
   global asteriodList
   for ast in ourData.get('near_earth_objects'): 
     names.append(ast.get('name_limited' , "unkown"))
     diameter.append(float(ast.get('estimated_diameter').get('kilometers').get('estimated_diameter_max')))
     hazardous.append(ast.get('is_potentially_hazardous_asteriod' , False))
     dict=additionalData(ast)
     if dict != {}:
        dateClosest.append(dict.get('close_approach_date'))
        distance.append(float(dict.get('miss_distance').get('astronomical')))
        velocity.append(float(dict.get('relative_velocity').get('kilometers_per_second')))
     else:
        distance.append(0)
        dateClosest.append(None)
        velocity.append(0)
   for i in range(len(names)):
     finalData ={
         'asteriodID':i ,
         'name': names[i] ,
         'diameter': diameter[i] ,
         'hazardous': hazardous[i] ,
         'dateClosest': dateClosest[i] ,
         'velocity': velocity[i] ,
         'distance': distance[i]         
      }
     asteriodList.append(finalData)
fetchData()     
print(asteriodList)     
#converting to json format
with open("neededData.json" , 'w') as ft :
     json .dump(asteriodList , ft , indent=4)



   

