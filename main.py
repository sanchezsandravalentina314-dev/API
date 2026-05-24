from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI(
    title="MechApp",
    description="API básica para pruebas de middleware y manejo de errores",
    version="1.0"
)

@app.middleware("http")
async def registro_peticiones(request: Request, call_next):

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\n========== REGISTRO MECHAPP ==========")
    print(f"Ruta visitada : {request.url.path}")
    print(f"Método HTTP   : {request.method}")
    print(f"Fecha y hora  : {fecha_actual}")
    print("======================================")

    respuesta = await call_next(request)

    return respuesta



@app.exception_handler(HTTPException)
async def error_personalizado(request: Request, exc: HTTPException):

    hora_error = datetime.now().strftime("%H:%M:%S")

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "mensaje": "Ocurrió un problema en la solicitud",
            "detalle": exc.detail,
            "ruta": request.url.path,
            "hora": hora_error
        }
    )


@app.get("/")
def inicio():

    return {
        "aplicacion": "MechApp",
        "estado": "activa",
        "mensaje": "Servidor funcionando correctamente"
    }


@app.get("/api/correcta")
def api_bien():

    return {
        "error": False,
        "mensaje": "La petición fue procesada correctamente",
        "datos": {
            "empresa": "MechApp",
            "modulo": "Middleware",
            "estado": "OK"
        }
    }




@app.get("/api/incorrecta")
def api_mal():

    raise HTTPException(
        status_code=400,
        detail="No fue posible completar la operación"
    )



@app.get("/api/usuarios")
def listar_usuarios():

    usuarios = [
        {
            "id": 1,
            "nombre": "Valentina",
            "rol": "Administrador"
        },
        {
            "id": 2,
            "nombre": "Carlos",
            "rol": "Cliente"
        }
    ]

    return {
        "total_usuarios": len(usuarios),
        "usuarios": usuarios
    }