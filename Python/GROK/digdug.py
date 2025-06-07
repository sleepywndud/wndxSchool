channelname = [] 
digcount = 0

while len(channelname) < 3:
    name = str(input("Channel name: "))
    if 'dig' in name.lower():
        channelname.append(name)

channelname.sort(reverse=True)
print(f"Proposals: {", ".join(channelname)}")
