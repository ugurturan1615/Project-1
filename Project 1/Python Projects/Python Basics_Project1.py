l=[[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
new_l=[]
def flatten(x):
    for i in x:
        if isinstance(i, list):
            flatten(i)
        else:
            new_l.append(i)
flatten(l)
print(new_l)