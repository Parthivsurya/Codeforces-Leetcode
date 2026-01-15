def interval_partition(lectures):
    lectures.sort(key=lambda x: x[0])  
    print(lectures) # Step 1
    halls = []                
    assigneded=[]          # h = 0 (no halls initially)
    for lecture in lectures:            # Step 3
        print(lecture)
        start, finish = lecture
        assigned = False
        for i in range(len(halls)): 
            print("!")    # Step 4
            if start >= halls[i]:
                halls[i] = finish       # Step 5
                assigneded.append((lecture, i+1)) # Assign lecture to hall i+1
                assigned = True
                break
        if not assigned:                # Step 6
            halls.append(finish)       # Step 7,8
            assigneded.append((lecture, len(halls)))
            print(assigneded)                   # Assign lecture to new hall
    return assigneded , len(halls)                   # number of halls
lectures = [(0, 30),(30,60), (5, 10),(15, 20)]
assigned,lect = interval_partition(lectures)
for lecw,hall in assigned:
    print(f"Lecture {lecw} assigned to Hall {hall}")    