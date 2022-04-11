import json
with open("exer1-interface-data.json", 'r') as file:
    data = json.load(file)
    print("DN                                                Description              Speed    MTU")
    print("------------------------------------------------- ------------------------ ------- -----")
    for i in range(400):
        for key in data["imdata"][i]["l1PhysIf"]["attributes"]:
            if key == "dn":
                dn = data["imdata"][i]["l1PhysIf"]["attributes"][key]
            if key == "descr":
                descr = data["imdata"][i]["l1PhysIf"]["attributes"][key]
            if key == "speed":
                speed = data["imdata"][i]["l1PhysIf"]["attributes"][key]
            if key == "mtu":
                mtu = data["imdata"][i]["l1PhysIf"]["attributes"][key]
        print("{}                 {}               {}   {}".format(dn, descr, speed, mtu))
    file.close()
