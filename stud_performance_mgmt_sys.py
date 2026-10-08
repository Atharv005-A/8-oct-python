students={
    1:{"name":"Atharv","Scores":[98,99,98]},
    2:{"name":"Prithviraj","Scores":[88,89,88]},
    3:{"name":"Abhilasha","Scores":[91,92,93]},
    4:{"name":"Rochana","Scores":[78,79,78]},
    5:{"name":"Shruti","Scores":[68,69,68]},
    6:{"name":"Swarali","Scores":[58,59,58]}
}


#average
for sid,detail in students.items():
    avg=sum(detail["Scores"])/len(detail["Scores"])
    detail["average"]=avg
    detail["passed"]= avg>=50 #boolean flag

#printing name of students who are passed
print("students passed:")
for sid,detail in students.items():
    if detail["passed"]:
        print(detail["name"])  