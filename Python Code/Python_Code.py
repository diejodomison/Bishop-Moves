start=input()
end=input()
x1=start[0]
x2=start[1]
y1=end[0]
y2=end[1]
x2=int(x2)
y2=int(y2)
if x1==("a") or x1==("A"):
    x1=1
elif x1==("b") or x1==("B"):
    x1=2
elif x1==("c") or x1==("C"):
    x1=3
elif x1==("d") or x1==("D"):
    x1=4
elif x1==("e") or x1==("E"):
    x1=5
elif x1==("f") or x1==("F"):
    x1=6
elif x1==("g") or x1==("G"):
    x1=7
elif x1==("h") or x1==("H"):
    x1=8
if y1==("a") or y1==("A"):
    y1=1
elif y1==("b") or y1==("B"):
    y1=2
elif y1==("c") or y1==("C"):
    y1=3
elif y1==("d") or y1==("D"):
    y1=4
elif y1==("e") or y1==("E"):
    y1=5
elif y1==("f") or y1==("F"):
    y1=6
elif y1==("g") or y1==("G"):
    y1=7
elif y1==("h") or y1==("H"):
    y1=8
while x1<9 and x2<9 and y1<9 and y2<9:

    if start==end:
        print("NO")
    elif x1==y1:
        print("NO")
    elif x2==y2:
        print("NO")
    elif abs(x1-y1)==abs(x2-y2):
        print("YES")
    else:
        print("NO")
    break


