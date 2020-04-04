# importing the module 
import json 
  
# Opening JSON file 
with open('sample.json') as json_file: 
    data = json.load(json_file) #converting json value into a dictionary

    #assigning some dummy values into dictionary keys
    data['name'] = 'mur'
    data['value'] = 42
    data['abc'] = 0.365
    data['xyz'] = (10,32,11)
    data['mno'] = [43,65,22]
    data['mur'] = ''
    data['count'] = 2

    #creating item with item dict in a list
    item = []
    if data['count'] > 0:
        for i in range(0,data['count']):
            d = {}
            d['x_axis'] = 12.45
            d['y_axis'] = 33.78
            d['h_axis'] = 45.21
            d['w_axis'] = 95.36
            item.append(d)
    #assigning item to dict item
    data['item'] = item
    #finally converting it into json and printing it
    print(json.dumps(data))

    #instead of printing, v can also write the json into same input file
    
    
