#EasyString Python
#By Tabernacle8

f = open("string.txt", "r")
strings = f.read().split("\n")

for string in strings:
    result = ""

    for place in range(string.count("{")):
        parse = string.split("{",1)[1].split("}",1)[0]
        #print(parse)


        if("+" in parse):
            ints = parse.split("+")
            index = 0
            for variable in ints:
                
                ints[index] = "int("+variable+")+"
                index = index+1

                
            ints[-1] = ints[-1].replace("+","")

            totalIntString = ""
            for thing in ints:
                totalIntString = totalIntString + thing
            
            string = string.replace("{","\"+str("+totalIntString,1).replace("}",")+\"",1).replace(parse,"",1)

        else:
            string = string.replace("{","\"+str(",1).replace("}",")+\"",1)
        

    print("\n\n\n\n"+"\""+string+"\""+"\n\n\n\n")
