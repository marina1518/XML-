from minify import *
from Compression_new import *
from pretify import *
from jason import *

class Node(object):
    def __init__(self, data):
        self.ht = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def import_url(url): #has url
    with open(url, 'r') as f:
        data = f.read()
    return data

def consistency(import_url): #has import url attribute
    data = import_url
    stack = []  # STACK FOR NODES
    NODES_LIST = []  # NODES LIST
    ERROR_BACKSLASH = []
    ERROR_MISSING = []
    ERROR_NAME = []
    #INDEX_LIST = []
    single_list = []
    NAME_LIST=[]
    INDEX_BACKSLASH = []  ###### LIST CONTAIN BACKSLACH
    INDEX_MISSING = []  ############# LIST CONTAIN INDEX MISSING
    INDEX_NAME = []  ############# LIST CONTAIN INDEX NAME
    #NODES_LIST_COPY=[]


    ENTER_CHAR = False  # flag for enter node <name>
    END_TAG = False  # flag for end tag flag </name>
    #COUNTER_NODE = 0
    TAG_FLAG = False  # flag for enter tag_value marina
    last_item_error = False
    repeated_end = False


    for x in data:  # in (import url)
        if x == '<':
            ENTER_CHAR = True
            END_TAG = False
            if TAG_FLAG == True:
                if tag != " "*len(tag) and tag != "" and tag != "\n" and len(stack)>0:
                    v = Node(tag)
                    #COUNTER_NODE += 1
                    #repeated_end = True
                    NODES_LIST.append([v, 'v'])
                    #NODES_LIST_COPY.append([v, 'v'])
                    single_list.append(tag)
                    parent = stack[-1]
                    for i in range(len(NODES_LIST) - 1, -1, -1):
                        if NODES_LIST[i][0].ht == parent:
                            NODES_LIST[i][0].add_child(v)
                            break
                    '''for i in range(len(NODES_LIST_COPY) - 1, -1, -1):
                        if NODES_LIST_COPY[i][0].ht == parent:
                            NODES_LIST_COPY[i][0].add_child(v)
                            break'''
                TAG_FLAG = False
            tag = ''
            word = ''
        elif x == '>':
            ENTER_CHAR = False
            # TRIAL
            TAG_FLAG = True
            ####### special format <name/>

            if '/' is word[len(word) - 1]:
                END_TAG = True
                special = word.replace('/', '')
                n = Node(special)
                #repeated_end=False
                #COUNTER_NODE += 1
                NODES_LIST.append([n, 's'])  # no need to put on stack
                p = stack[-1]
                # ADD_CHILD
                for i in range(len(NODES_LIST)-1,-1,-1):
                    if NODES_LIST[i][0].ht == p:
                        NODES_LIST[i][0].add_child(n)  ##### n ------> to
                        break

            #while len(stack)>2 and ('--' in stack[-1].split()[0]  or '?' in stack[-1].split()[0]):
                #stack.pop()

            if '/' is word[0] and len(stack)>0:

                END_TAG = True
                different = word.replace('/', '')
                TRIAL = stack[-1].split()
                if (different == TRIAL[0] and different != ''):
                    repeated_end=True
                    stack.pop()
                    # pass
                else:
                    print(different,"???")
                    print("stack1", stack)
                    split_stack = list(stack)
                    for j in range(0, len(split_stack)):
                        split_stack[j] = split_stack[j].split()[0]
                    print("split", split_stack)

                    if (different in split_stack):  # note id=0
                        index = split_stack.index(different)
                        stack.remove(stack[index])
                        repeated_end=True
                        print("stack2", stack)

                    elif(repeated_end==True): #for ending without beginning
                        #word=word.replace('/','')
                        word='!--'+word+'--'
                        n=Node(word)
                        NODES_LIST.append([n,'c'])
                        p = stack[-1]
                        # ADD_CHILD
                        for i in range(len(NODES_LIST) - 1, -1, -1):
                            if NODES_LIST[i][0].ht == p:
                                NODES_LIST[i][0].add_child(n)  ##### n ------> to
                                break
                    else:
                        ERROR_NAME.append(stack[-1])
                        repeated_end=True
                        count_element = single_list.count(stack[-1])  ##### count in nodes list
                        ############get index of error
                        count_top = 0
                        for l in range(0, len(NODES_LIST)):
                            if NODES_LIST[l][0].ht == stack[-1]:
                                count_top += 1  #####count examples 2
                                if count_top == count_element:
                                    index = l
                                    break

                        INDEX_NAME.append([stack[-1], index])
                        f = stack[-1].split()
                        print('/' + f[0])
                        print("NOT THE SAME NAME")
                        stack.pop()

                # TAG_FOUND = False

            if END_TAG == False:
                repeated_end=False
                #word = word.replace('!', '')
                n = Node(word)
                # COUNT_OPEN += 1

                #COUNTER_NODE += 1
                #if(counter_node>1)

                if (len(stack) > 0):
                    p = stack[-1]
                    count_element = single_list.count(p)
                    # print(p)
                    for i in range(len(NODES_LIST)-1,-1,-1):
                        if NODES_LIST[i][0].ht == p :

                            if n.ht == NODES_LIST[i][0].ht.split()[0] and ("!--" not in n.ht and "?" not in n.ht):
                                f = stack[-1].split()


                            else:
                                NODES_LIST[i][0].add_child(n)  ##### n ------> to
                                f = stack[-1].split()
                                #ref = i
                                break

                    '''for i in range(len(NODES_LIST_COPY)-1,-1,-1):
                        if NODES_LIST_COPY[i][0].ht == p :

                            if n.ht == NODES_LIST_COPY[i][0].ht.split()[0]:
                                f = stack[-1].split()


                            else:
                                NODES_LIST_COPY[i][0].add_child(n)  ##### n ------> to
                                f = stack[-1].split()
                                #ref = i
                                break'''

                if ((len(stack) > 0) and (word == f[0]) and "!--" not in word and "?" not in word):
                    ERROR_BACKSLASH.append(stack[-1])
                    count_element = single_list.count(stack[-1])  ##### count in nodes list
                    ############### get index of error
                    count_top = 0
                    for l in range(0, len(NODES_LIST)):
                        if NODES_LIST[l][0].ht == stack[-1]:
                            count_top += 1  #####count examples 2
                            if count_top == count_element:
                                index = l
                                break

                    INDEX_BACKSLASH.append([stack[-1], index])
                    print('/' + f[0])
                    # END_LIST.append(f[0])
                    print("backslash error")
                    stack.pop()

                else:
                    if ((word[0]=='?' and word[-1]=='?')):
                        NODES_LIST.append([n, 'h'])
                        if(len(stack)==0):
                            stack.append(word)

                    elif(('!--' in word and word[-1]=='-')):
                        NODES_LIST.append([n, 'h'])

                    else:
                        stack.append(word)
                        NODES_LIST.append([n, 'n'])
                        NAME_LIST.append(word)
                        #NODES_LIST_COPY.append([n, 'n'])
                        single_list.append(word)

                word = ''


        elif TAG_FLAG == True and x != '>' and x != '\n':
            tag += x


        elif ENTER_CHAR == True and x != '<':
            word += x




    #print(stack)
    if (len(stack) > 0):
        x=0
        while len(stack)>0:
            if ('!--' in stack[-1].split()[0] or '?' in stack[-1].split()[0]):
                stack.pop()

            #elif(NODES_LIST[5][0].children == NULL):


            else:
                ERROR_MISSING.append(stack[-1])
                count_element = single_list.count(stack[-1])  ##### count in nodes list

                count_top = 0
                ##########GET INDEX OF ERROR
                for l in range(0, len(NODES_LIST)):
                    if NODES_LIST[l][0].ht == stack[-1]:
                        count_top += 1  #####count examples 2
                        if count_top == count_element:
                            index = l
                            break

                INDEX_MISSING.append([stack[-1], index])
                f = stack[-1].split()
                print('/' + f[0])
                print('NOT ENDED')
                stack.pop()
            x+=1

    #print(NODES_LIST_COPY)
    #JASON(NODES_LIST_COPY)
    #if(last_item_error==True):
        #NODES_LIST=NODES_LIST.remove(NODES_LIST[-1])
    return NODES_LIST,ERROR_BACKSLASH,ERROR_NAME,ERROR_MISSING,INDEX_NAME,INDEX_BACKSLASH,INDEX_MISSING,NAME_LIST

def show_file(consistency):
    mydata = ''
    FLAG_ERROR = False
    NODES_LIST,ERROR_BACKSLASH,ERROR_NAME,ERROR_MISSING,INDEX_NAME,INDEX_BACKSLASH,INDEX_MISSING,NAME_LIST = consistency
    root = NODES_LIST[0][0].ht
    MARKED_LIST = [0] * len(NODES_LIST)
    print(NODES_LIST,"show")
    #if last_item_error==True:
        #node_it=len(NODES_LIST)-1
    #else:
        #node_it=len(NODES_LIST)

    def print_xml(x, please, counter):
        ###### problem more one example
        tharwota=counter

        for i in range(0, len(NODES_LIST)):
            FLAG_ERROR=False
            if NODES_LIST[i][0].ht == x and MARKED_LIST[i] == 0:
                index = i

                if NODES_LIST[i][1] == 's':
                    mydata = please + '<' + NODES_LIST[i][0].ht + '/>' + '\n'
                    print('<' + NODES_LIST[i][0].ht + '/>')

                elif NODES_LIST[i][1] == 'c':
                    tharwota+=1
                    mydata = please + '<!--' + NODES_LIST[i][0].ht + '-->' +" ------>open tag not found"+ '\n'
                    print('<!--' + NODES_LIST[i][0].ht + '-->' +" ------>open tag not found" )


                elif NODES_LIST[i][1] == 'h':
                    mydata = please + '<' + NODES_LIST[i][0].ht + '>' + '\n'
                    print('<' + NODES_LIST[i][0].ht + '>')



                elif NODES_LIST[i][1] == 'n':
                    mydata = please + '<' + NODES_LIST[i][0].ht + '>' + '\n'
                    print('<' + NODES_LIST[i][0].ht + '>')

                elif NODES_LIST[i][1] == 'v':
                    mydata = please + NODES_LIST[i][0].ht + '\n'
                    # print('new'+mydata)
                    print(NODES_LIST[i][0].ht)
                MARKED_LIST[i] = 1
                break

            else:
                mydata = please + ''

        for j in NODES_LIST[index][0].children:
            new = j.ht

            please, counter = print_xml(new, mydata, tharwota)
            mydata = please
            tharwota = counter

        if NODES_LIST[i][1] == 'n':

            if ('!' == NODES_LIST[i][0].ht[0] or '?' == NODES_LIST[i][0].ht[0] or NODES_LIST[i][0].ht[-1] == '/'):
                pass


            else:

                if (NODES_LIST[i][0].ht in ERROR_BACKSLASH):

                    for m in range(0, len(INDEX_BACKSLASH)):

                        if NODES_LIST[i][0].ht == INDEX_BACKSLASH[m][0] and i == INDEX_BACKSLASH[m][1]:
                            print(i)

                            mydata = mydata + '</' + NODES_LIST[i][0].ht.split()[0] + '>' + "-----> BACKSLASH_ERROR" + '\n'

                            print('</' + NODES_LIST[i][0].ht.split()[0] + '>', "-----> BACKSLASH_ERROR")

                            tharwota += 1

                            FLAG_ERROR = True

                            break

                if (NODES_LIST[i][0].ht in ERROR_NAME):

                    for m in range(0, len(INDEX_NAME)):

                        if NODES_LIST[i][0].ht == INDEX_NAME[m][0] and i == INDEX_NAME[m][1]:
                            mydata = mydata + '</' + NODES_LIST[i][0].ht.split()[0] + '>' + "-----> WRONG_NAME_ERROR" + '\n'

                            print('</' + NODES_LIST[i][0].ht.split()[0] + '>', "-----> WRONG_NAME_ERROR")

                            tharwota += 1

                            FLAG_ERROR = True

                            break

                if (NODES_LIST[i][0].ht in ERROR_MISSING):

                    for h in range(0, len(INDEX_MISSING)):

                        if NODES_LIST[i][0].ht == INDEX_MISSING[h][0] and i == INDEX_MISSING[h][1]:
                            mydata = mydata + '</' + NODES_LIST[i][0].ht.split()[0] + '>' + "-----> MISSING_CLOSE_TAG_ERROR" + '\n'

                            print('</' + NODES_LIST[i][0].ht.split()[0] + '>', "-----> MISSING_CLOSE_TAG_ERROR")

                            tharwota += 1

                            FLAG_ERROR = True

                            break

                if FLAG_ERROR == False:
                    #print('why')

                    mydata = mydata + '</' + NODES_LIST[i][0].ht.split()[0] + '>' + '\n'

                    print('</' + NODES_LIST[i][0].ht.split()[0] + '>')

        return mydata, tharwota


    my, counter_error = print_xml(root, '', 0)
    # saving file

    print("error number", counter_error)
    file2 = open('consistency.xml', 'w')
    file2.write("ERROR NUMBER: "+str(counter_error)+'\n')
    file2.write(my)
    file2.close()

    #write data_pretty

    pretty_file(NODES_LIST)


    #write minify
    minify_operation()

    #write compression
    compress()

    #write decompression
    decompress(compress())

    #wrie_jason
    jason_function(NODES_LIST,NAME_LIST)


    return counter_error

def send_error(show_file):
    counter_error=show_file
    return counter_error

#show_file(consistency(import_url()))