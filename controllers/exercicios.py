import json

class controller : 
    def __init__(self):
        teste = "teste"
        
    def index():
        file = open("./views/index.html",'r')
        lines = file.readlines()
        content = ""
        for line in lines :
            content += line
        return content       
    
    def list():
        #open exercicio-list
        file = open("./exercicios.json")
        jsonFile = json.load(file)
        
        
        for exercicse in jsonFile :
            print(exercicse)
        
        return jsonFile
    
    def create():
        #open exercicio-create
        return 1