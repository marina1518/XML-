def compress():
    with open('pretty.xml', 'r') as f:
        uncompressed = f.read()
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])

    with open('compressed.txt', 'w') as f:
        for item in result:
            f.write("%s" % item)

    return result


def decompress(compress):
    compressed=compress
    dict_size = 256
   
    dictionary = {i: chr(i) for i in range(dict_size)}

    w = result = chr(compressed.pop(0))
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry

        
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    #return result

    file = open("decompressed.txt", "w")
    file.write(result)
    file.close()

#compressed = compress(data)
#print (compressed)



#decompressed = decompress(compressed)
#print (decompressed)
