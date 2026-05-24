from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="MECHAPP API",
    description="API del proyecto formativo MECHAPP",
    version="1.0"
)


class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str


class Propietario(BaseModel):
    id: int
    nombre_negocio: str
    direccion: str
    telefono: str


class Torneo(BaseModel):
    id: int
    nombre: str
    tipo: str
    nivel: str
    fecha: str
    cupos: int


class Inscripcion(BaseModel):
    id: int
    usuario: str
    torneo: str


class Pago(BaseModel):
    id: int
    usuario: str
    torneo: str
    valor: float
    estado: str


class Resultado(BaseModel):
    id: int
    torneo: str
    ganador: str
    puntos: int


usuarios = [
    {
        "id": 1,
        "nombre": "Valentina Sánchez",
        "correo": "vale@gmail.com",
        "rol": "jugador"
    }
]

propietarios = [
    {
        "id": 1,
        "nombre_negocio": "Cancha Elite",
        "direccion": "Bogotá",
        "telefono": "3001234567"
    }
]

torneos = [
    {
        "id": 1,
        "nombre": "Copa Verano",
        "tipo": "Fútbol",
        "nivel": "Intermedio",
        "fecha": "2026-06-15",
        "cupos": 16
    }
]

inscripciones = []

pagos = []

resultados = []

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a la API de MECHAPP"
    }

# GET
@app.get("/usuarios")
def obtener_usuarios():
    return usuarios


# GET POR ID
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):

    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# POST
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):

    for u in usuarios:
        if u["id"] == usuario.id:
            raise HTTPException(
                status_code=400,
                detail="El usuario ya existe"
            )

    usuarios.append(usuario.dict())

    return {
        "mensaje": "Usuario registrado correctamente",
        "usuario": usuario
    }


# PUT
@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario_actualizado: Usuario):

    for index, usuario in enumerate(usuarios):

        if usuario["id"] == usuario_id:

            usuarios[index] = usuario_actualizado.dict()

            return {
                "mensaje": "Usuario actualizado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# DELETE
@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):

    for usuario in usuarios:

        if usuario["id"] == usuario_id:

            usuarios.remove(usuario)

            return {
                "mensaje": "Usuario eliminado"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# GET
@app.get("/torneos")
def obtener_torneos():
    return torneos


# POST
@app.post("/torneos")
def crear_torneo(torneo: Torneo):

    torneos.append(torneo.dict())

    return {
        "mensaje": "Torneo creado correctamente",
        "torneo": torneo
    }


# PUT
@app.put("/torneos/{torneo_id}")
def actualizar_torneo(torneo_id: int, torneo_actualizado: Torneo):

    for index, torneo in enumerate(torneos):

        if torneo["id"] == torneo_id:

            torneos[index] = torneo_actualizado.dict()

            return {
                "mensaje": "Torneo actualizado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Torneo no encontrado"
    )


# DELETE
@app.delete("/torneos/{torneo_id}")
def eliminar_torneo(torneo_id: int):

    for torneo in torneos:

        if torneo["id"] == torneo_id:

            torneos.remove(torneo)

            return {
                "mensaje": "Torneo eliminado"
            }

    raise HTTPException(
        status_code=404,
        detail="Torneo no encontrado"
    )


# GET
@app.get("/inscripciones")
def obtener_inscripciones():
    return inscripciones


# POST
@app.post("/inscripciones")
def crear_inscripcion(inscripcion: Inscripcion):

    inscripciones.append(inscripcion.dict())

    return {
        "mensaje": "Inscripción realizada correctamente",
        "inscripcion": inscripcion
    }


# DELETE
@app.delete("/inscripciones/{inscripcion_id}")
def eliminar_inscripcion(inscripcion_id: int):

    for inscripcion in inscripciones:

        if inscripcion["id"] == inscripcion_id:

            inscripciones.remove(inscripcion)

            return {
                "mensaje": "Inscripción cancelada"
            }

    raise HTTPException(
        status_code=404,
        detail="Inscripción no encontrada"
    )

# =====================================================
# CRUD PAGOS
# =====================================================

# GET
@app.get("/pagos")
def obtener_pagos():
    return pagos


# POST
@app.post("/pagos")
def registrar_pago(pago: Pago):

    pagos.append(pago.dict())

    return {
        "mensaje": "Pago registrado correctamente",
        "pago": pago
    }

# GET
@app.get("/propietarios")
def obtener_propietarios():
    return propietarios


# POST
@app.post("/propietarios")
def crear_propietario(propietario: Propietario):

    propietarios.append(propietario.dict())

    return {
        "mensaje": "Propietario agregado correctamente",
        "propietario": propietario
    }


# GET
@app.get("/resultados")
def obtener_resultados():
    return resultados


# POST
@app.post("/resultados")
def registrar_resultado(resultado: Resultado):

    resultados.append(resultado.dict())

    return {
        "mensaje": "Resultado registrado correctamente",
        "resultado": resultado
    }


@app.get("/torneos/filtro/{nivel}")
def filtrar_torneos(nivel: str):

    lista_filtrada = []

    for torneo in torneos:

        if torneo["nivel"].lower() == nivel.lower():
            lista_filtrada.append(torneo)

    return {
        "torneos_filtrados": lista_filtrada
    }

@app.post("/login")
def login(correo: str):

    for usuario in usuarios:

        if usuario["correo"] == correo:

            return {
                "mensaje": "Login exitoso",
                "usuario": usuario
            }

    raise HTTPException(
        status_code=401,
        detail="Correo incorrecto"
    )