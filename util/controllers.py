from controllers import exercicios

def handle(controller, method, argument):
        
    methods = {
        "" : exercicios.controller.index(),
        "list" : exercicios.controller.list()
    }
    
    if method == None:
        fileText = exercicios.controller.index()
        return fileText

    if method == 'list' :
        fileText = exercicios.controller.list()
        return fileText
    
    return methods.get(method, "")

    
    