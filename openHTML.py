
def returnHTML(path):
    file = open(path, 'r')
    lines = file.readlines()
    content = ""
    for line in lines :
        content += line
    
    file.close()
    return content


if __name__ == "__main__" :
    print(returnHTML())