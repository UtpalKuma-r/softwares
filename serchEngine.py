import time


sentences = ["python python python python", "python", "python is not python snake", "python python python", "python python python python python python python python python python","python python python python"]

                                    #getting Query 
query = input("Enter your Quary: ")

init = time.time()                  #inetiating time

                                    #finding the relevent data
relevence = []
for item in sentences:
    if query.lower() in  item.lower():
        relevence.append(item)

                                    #sorting the data
relevence.sort(reverse=True)

                                    #printing result
tt = time.time() - init
print(f"{len(relevence)} results in {tt}")
for item in relevence:
    print(item)
