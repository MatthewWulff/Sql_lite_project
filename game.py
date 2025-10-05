def build_inverted_index(sentences):
    obj = {}
    
    for i in range(len(sentences)):
        sentence = sentences[i].split()
        for word in set(sentence):
            if word in obj:
                obj[word].append(i)
            else:
                obj[word] = [i]
    return obj

    
    
        
            


       
      
    
 
      
