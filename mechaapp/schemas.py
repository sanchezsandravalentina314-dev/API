from pydantic import BaseModel, EmailStr
from datetime import datetime


# -------- USUARIO --------

class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr
    contraseña: str
    edad: int
    rol: str


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    edad: int
    rol: str

    class Config:
        from_attributes = True


# -------- TORNEO --------

class TorneoCreate(BaseModel):
    nombre_torneo: str
    tipo: str
    nivel: str
    fecha: str
    cupos: int
    premio: float


class TorneoResponse(BaseModel):
    id: int
    nombre_torneo: str
    tipo: str
    nivel: str
    fecha: str
    cupos: int
    premio: float

    class Config:
        from_attributes = True