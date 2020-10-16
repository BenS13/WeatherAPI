def sanatiseOutput(text):#Remove "(", ")", "'", "," from output
    data = (str(text)).replace("(","").replace(")","").replace("'","").replace(",","")
    print(data)

