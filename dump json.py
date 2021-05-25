import json
pihu1={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",          
        } 
}
out_file = open("myfile.json", "w")
json.dump(pihu1, out_file, indent = 6)
out_file.close() 

 
