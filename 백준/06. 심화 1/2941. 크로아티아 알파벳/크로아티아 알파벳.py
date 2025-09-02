data = input()
count = len(data)

if data.count("c="):
    count -= data.count("c=")
if data.count("c-"):
    count -= data.count("c-")   
if data.count("d-"):
    count -= data.count("d-")
if data.count("lj"):
    count -= data.count("lj")      
if data.count("nj"):    
    count -= data.count("nj")
if data.count("s="):       
    count -= data.count("s=")
if data.count("z="):    
    if data.count("dz="):
        count -= data.count("dz=")   
    count -= data.count("z=")


print(count)