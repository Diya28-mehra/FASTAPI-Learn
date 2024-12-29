from fastapi import FastAPI  #import 
app = FastAPI() #instance 


@app.get('/') #path(decorator)
def index(): #function 
    return {'data':{'name':'dia'}}  

@app.get('/about')
def about():
    return {'data':{'about':'page'}}  