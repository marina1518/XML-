def pretty_file(NODES_LIST):
    #NODES_LIST, ERROR_BACKSLASH, ERROR_NAME, ERROR_MISSING = consistency
    MARKED_LIST_PRETTY = [0] * len(NODES_LIST)
    root = NODES_LIST[0][0].ht
    data_pretty = ''
    def pretty_xml(x, level, begin_data):
        ################ problem more one example
        for i in range(0, len(NODES_LIST)):
            if NODES_LIST[i][0].ht == x and MARKED_LIST_PRETTY[i] == 0:
                index = i
                if NODES_LIST[i][1] == 's':
                    spaces = ' ' * level
                    data_pretty = begin_data + spaces + '<' + NODES_LIST[i][0].ht + '/>' + '\n'
                    print(spaces + '<' + NODES_LIST[i][0].ht + '/>')

                elif NODES_LIST[i][1] == 'h':
                    spaces = ' ' * 0
                    level=-1
                    data_pretty = begin_data + spaces + '<' + NODES_LIST[i][0].ht + '>' + '\n'
                    print('<' + NODES_LIST[i][0].ht + '>')

                elif NODES_LIST[i][1] == 'c':
                    spaces = ' ' * level
                    data_pretty = begin_data + spaces + '<' + NODES_LIST[i][0].ht + '>' + '\n'
                    print('<' + NODES_LIST[i][0].ht + '>')


                elif NODES_LIST[i][1] == 'n':
                    spaces = ' ' * level
                    data_pretty = begin_data + spaces + '<' + NODES_LIST[i][0].ht + '>' + '\n'
                    print(spaces + '<' + NODES_LIST[i][0].ht + '>')


                elif NODES_LIST[i][1] == 'v':
                    #level -= 1
                    spaces = ' ' * level
                    data_pretty = begin_data + spaces + NODES_LIST[i][0].ht + '\n'
                    print(spaces + NODES_LIST[i][0].ht)
                MARKED_LIST_PRETTY[i] = 1
                break
            else:
                data_pretty = begin_data + ''

        if NODES_LIST[index][0].children:
            level += 1

        for j in NODES_LIST[index][0].children:
            new = j.ht
            begin_data = pretty_xml(new, level, data_pretty)
            data_pretty = begin_data

        if NODES_LIST[i][1] == 'n':
            level -= 1
            spaces = ' ' * level
            data_pretty = data_pretty + spaces + '</' + NODES_LIST[i][0].ht.split()[0] + '>' + '\n'
            print(spaces + '</' + NODES_LIST[i][0].ht.split()[0] + '>')

        return data_pretty

    data_modified = pretty_xml(root, 0, '')
    #print(data_pretty)
    file3 = open('pretty.xml', 'w')
    file3.write(data_modified)
    file3.close()
    #return data_modified