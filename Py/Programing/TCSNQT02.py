sender=[]
receiver=[]
amount=[]
time=[]
n=int(input())
for i in range(0,n):
    sender.append(input())
    receiver.append(input())
    amount.append(float(input()))
    time.append(int(input()))
for i in range(0,n):
    for j in range(i+1,n):
        if time[j]-time[i]<=60:
            if sender[i]==sender[j] and receiver[i]==receiver[j] and round(amount[i],2)==round(amount[j],2):
                print(f"{sender[j]} {receiver[j]} {amount[j]:.2f} {time[j]}")