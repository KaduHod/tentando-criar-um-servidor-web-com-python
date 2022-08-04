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
        
        
        tabelaExercicios ="" 
        for exercicio in jsonFile : 
            newLine = f"<tr><td>{exercicio['nome']}</td><td>{exercicio['descricao']}</td></tr>"
            tabelaExercicios += newLine
            
                    
        view = open('./views/exercise-list.html')
        lines = view.readlines()
        
        content = ""
        for line in lines:
            content += line
        
        content = content.replace("<change>",tabelaExercicios)
                
        return content
            
    def create():
        #open exercicio-create
        return 1