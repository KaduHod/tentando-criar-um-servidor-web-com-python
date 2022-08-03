def handlePath(path):
    splitString = path.split('/')
    controller  = splitString[1]
    method      = None
    argument    = None
    if len(splitString) > 2 :
        method = splitString[2]
        
    if len(splitString) > 3 :
        argument = splitString[3]
    
    return {
        "controller" : controller,
        "method"     : method,
        "argument"   : argument
    }