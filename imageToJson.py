import json
import base64

data = {}
with open('1.png', mode='rb') as file:
    img = file.read()
data['img'] = base64.encodebytes(img).decode("utf-8")

print(json.dumps(data))
