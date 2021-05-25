# import json 
# pihu={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
# }
# print(json.dumps(pihu,indent=4,sort_keys=True))

import json
pihu='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
print(pihu)
pihu= json.loads(pihu)
print(pihu)
