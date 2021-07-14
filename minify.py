def minify_operation():
    with open('pretty.xml', 'r') as f:
        line = f.read().splitlines()


    file2 = open('minify.xml', 'w')
    print (line)

    for x in line:
        print(x.strip(), end="")
        file2.write(x.strip())

    file2.close()

