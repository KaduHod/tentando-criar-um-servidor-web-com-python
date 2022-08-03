from controllers import exercicios

def handle(controller, method, argument):
    
    controllers = {
        "exercicios" : exercicios.controller
    }
    
    methods = {
        "" : exercicios.controller.index(),
        "list" : exercicios.controller.list()
    }
    
    if(method == None):
        fileText = exercicios.controller.index()
        return fileText
    
    return methods.get(method, "")

    
    