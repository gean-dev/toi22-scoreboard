import json

scores = json.load(open('combined/scores_day1'))
history=json.load(open('combined/history_day1'))

with open('day2.csv') as f:
    t1,t2,t3=f.readline().strip().split(",")[2:]
    for e in f.readlines():
        user,team,p1,p2,p3=e.strip().split(",")
        if user not in scores:
            scores[user]=dict()
        scores[user][t1]=float(p1)
        scores[user][t2]=float(p2)
        scores[user][t3]=float(p3)

        history.append([user,t1,1777426860,float(p1)])
        history.append([user,t2,1777426860,float(p2)])
        history.append([user,t3,1777426860,float(p3)])
    
json.dump(scores, open('combined/scores', 'w'))
json.dump(history,open('combined/history', 'w'))