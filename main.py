from fastapi import FastAPI, HTTPException
from auth import registrar_usuario, iniciar_sesion

app = FastAPI()

@app.post("/registrar")
def registrar(nombre_usuario: str, nombre: str, apellido: str, correo: str, contraseña: str):
    respuesta = registrar_usuario(nombre_usuario, nombre, apellido, correo, contraseña)
    if "error" in respuesta:
        raise HTTPException(status_code=400, detail=respuesta["error"])
    return respuesta

@app.post("/login")
def login(nombre_usuario: str, contraseña: str):
    respuesta = iniciar_sesion(nombre_usuario, contraseña)
    if "error" in respuesta:
        raise HTTPException(status_code=401, detail=respuesta["error"])
    return respuesta
