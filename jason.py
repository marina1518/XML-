def jason_function(NODES_LIST,name_list):
    # json_MARKED_LIST=[]
    repeated = []
    trial = []
    bracket = []
    duplicate = []
    bracket_end = []
    bracket_start = []
    split = []
    last_child = []
    ERROR_v = []
    MARKED_LIST_PRETTY= [0] * len(NODES_LIST)
    #print(NODES_LIST)

    # END_LIST=[] #END_TAGS
    children_len = 0
    done = 0
    write = True
    json_data = ''
    count_lastchild = 0
    for s in range(0, len(NODES_LIST)):
        if NODES_LIST[s][1] == 'n':
            # for c in range (len(NODES_LIST[s][0].children)-1,-1,-1) :
            for c in NODES_LIST[s][0].children:
                count_lastchild += 1
                if count_lastchild == len(NODES_LIST[s][0].children):
                    if c.ht in name_list:
                        last_child.append(c.ht.split()[0])

            count_lastchild = 0
            
    print("it's okai")
    print(last_child)
    print(name_list)

    

    ####################################################################################
    def xmltojson(x, level, count, write, print_json):
        ################ problem more one example
        global child
        child = ''
        global enter_value
        enter_value = 0
        global value
        value = ''
        global itr
        itr = 0
        global length
        for i in range(0, len(NODES_LIST)):
            if NODES_LIST[i][0].ht == x and MARKED_LIST_PRETTY[i] == 0:
                index = i
                #if NODES_LIST[i][1] == 's' :

                if NODES_LIST[i][1] == 'h' or  NODES_LIST[i][1] == 's' or NODES_LIST[i][1]=='c':
                    spaces = ' ' * level
                    if ('!' in NODES_LIST[i][0].ht) or NODES_LIST[i][1]=='c' : ##### comment
                       repeated.append(NODES_LIST[i][0].ht) 
                       #print(repeated)
                       disallowed_characters = "-!"
                       COMMENT_VALUE = NODES_LIST[i][0].ht
                       for character in disallowed_characters:
                           COMMENT_VALUE = COMMENT_VALUE.replace(character, "")

                       json_data = print_json + spaces +'"'+"#comment"+'"'+':'+'"'+COMMENT_VALUE+'"'+','+'\n'
                       print(spaces +'"'+"#comment"+'"'+':'+'"'+COMMENT_VALUE+'"'+',')   


                    if ('?' in NODES_LIST[i][0].ht or NODES_LIST[i][1] == 's' ) : #frame f_num="2"
                        if NODES_LIST[i][1] == 's' :
                           split = NODES_LIST[i][0].ht.split() 
                           NODES_LIST[i][0].ht= NODES_LIST[i][0].ht + 'special/'
                           print("#####check S")
                           print(NODES_LIST[i][0].ht)
                           repeated.append(NODES_LIST[i][0].ht)
                           #split = NODES_LIST[i][0].ht.split()
                        else :    
                         repeated.append(NODES_LIST[i][0].ht)   
                         HEAD_VALUE = NODES_LIST[i][0].ht
                         length = len(HEAD_VALUE)
                         HEAD_VALUE = HEAD_VALUE[:length - 1]  ####DONE ',' 
                         split = HEAD_VALUE.split()  # ?xml version='1.0' standalone='no'?
                 
                        for j in range(0, len(split)):
                             if j == 0 :
                                 json_data = print_json
                                 json_data = json_data + spaces +'"'+split[j]+'"'+':'+'{'
                                 print(spaces +'"'+split[j]+'"'+':'+'{') 
                                

                             if (j > 0):  # id=1

                               # print("J>0")
                                itr = 0
                                for k in split[j]:
                                    itr += 1
                            # print("k:")
                            # print(k)
                                    if (k != '='):
                                          if (enter_value == 0):
                                              child += k
                                          else:
                                              value += k
                                    else:
                                         json_data = json_data + spaces + '"' + '-' + child + '"' + ':'+'\n'
                                         print(spaces + '"' + '-' + child + '"' + ':', end='')
                                         child = ''
                                         enter_value = 1

                                    if (itr == len(split[j])):
                                        if value.count('"') == 2 or value.count("'") == 2:
                                            if '"' in value:
                                                json_data = json_data + value + ',' + '\n'
                                                print(value + ',')
                                            else:
                                                 json_data =json_data + spaces + '"' + value + '"' + ',' + '\n'
                                                 print('"' + value + '"' + ',')

                                            value = ''
                                            enter_value = 0
                                        else:
                                             value += ' '
                                             pass
                        if (NODES_LIST[i][1]=='h'):                    
                          length = len(json_data)
                          json_data = json_data[:length - 2]  ####DONE ','                    
                          json_data = json_data + '\n'+'}' + ',' + '\n'
                          print('}' + ',') 
                        else : #"-self-closing": "true"
                            json_data =  json_data + spaces +  ' "-self-closing": "true" '+ '\n' + '}' + '\n'
                            print(' "-self-closing": "true" '+ '\n' + '}' + '\n')

                        
                if NODES_LIST[i][1] == 'n':
                    repeated.append(NODES_LIST[i][0].ht.split()[0])
                    s = NODES_LIST[i][0].ht.split()[0]
                    count = repeated.count(s)
                    spaces = ' ' * level

                    if (count == 1 or NODES_LIST[i][0].ht.split()[0] not in duplicate):
                        json_data = print_json + spaces + '"' + NODES_LIST[i][0].ht.split()[0] + '"' + ':'
                        # print("error")
                        print(spaces + '"' + NODES_LIST[i][0].ht.split()[0] + '"' + ':', end='')
                    else:
                        json_data = print_json + ''
                    

                elif NODES_LIST[i][1] == 'v':
                    level -= 1
                    spaces = ' ' * level
                    if (NODES_LIST[i][0].ht in ERROR_v):
                        json_data = print_json + spaces + "#text:" + '"' + NODES_LIST[i][0].ht + '"' + '}' + ','
                        print('"' + NODES_LIST[i][0].ht + '"' + '}', end='')
                        # ERROR_v.remove('1')

                    elif (count > 1 or write == False):
                        if (done == 1):
                            json_data = print_json + '"' + NODES_LIST[i][0].ht + '"' + ','
                            print('"' + NODES_LIST[i][0].ht + '"' + ',', end='')
                            write = True
                        else:
                            json_data = print_json + '"' + NODES_LIST[i][0].ht + '"' + ','
                            print('"' + NODES_LIST[i][0].ht + '"' + ',', end='')
                    else:
                        json_data = print_json + '"' + NODES_LIST[i][0].ht + '"' + ',' + '\n'  # new line
                        print('"' + NODES_LIST[i][0].ht + '"' + ',')
                MARKED_LIST_PRETTY[i] = 1
                break

        count_rep = 0
        for j in NODES_LIST[index][0].children:
            trial.append(j.ht.split()[0])
            count_rep = trial.count(j.ht.split()[0])
            if (count_rep > 1):
                duplicate.append(j.ht.split()[0])
                # bracket.append(j.ht)
                bracket_start.append(j.ht.split()[0])
                bracket_end.append(j.ht.split()[0])
            
        trial.clear()

        if NODES_LIST[index][0].ht.split()[0] in bracket_start:
            json_data = json_data + '['
            print('[', end='')
            for f in range(0, bracket_start.count(NODES_LIST[index][0].ht.split()[0])):
                bracket_start.remove(NODES_LIST[index][0].ht.split()[0])

            write = False




