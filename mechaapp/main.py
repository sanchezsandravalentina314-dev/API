from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import (
    Usuario, Propietario, Torneo, Inscripcion,
    Pago, Notificacion, Resultado, Cancha, Reporte
)

from schemas import UsuarioCreate, UsuarioResponse, TorneoCreate, TorneoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ---------------- DB ----------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ================= USUARIOS =================

@app.post("/usuarios", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo = Usuario(**usuario.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/usuarios", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


# ================= TORNEOS =================

@app.post("/torneos", response_model=TorneoResponse)
def crear_torneo(torneo: TorneoCreate, db: Session = Depends(get_db)):
    nuevo = Torneo(**torneo.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/torneos", response_model=list[TorneoResponse])
def listar_torneos(db: Session = Depends(get_db)):
    return db.query(Torneo).all()


# ================= PROPIETARIOS =================

@app.post("/propietarios")
def crear_propietario(propietario: dict, db: Session = Depends(get_db)):
    nuevo = Propietario(**propietario)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/propietarios")
def listar_propietarios(db: Session = Depends(get_db)):
    return db.query(Propietario).all()


# ================= INSCRIPCIONES =================

@app.post("/inscripciones")
def crear_inscripcion(inscripcion: dict, db: Session = Depends(get_db)):
    nuevo = Inscripcion(**inscripcion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/inscripciones")
def listar_inscripciones(db: Session = Depends(get_db)):
    return db.query(Inscripcion).all()


# ================= PAGOS =================

@app.post("/pagos")
def crear_pago(pago: dict, db: Session = Depends(get_db)):
    nuevo = Pago(**pago)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/pagos")
def listar_pagos(db: Session = Depends(get_db)):
    return db.query(Pago).all()


# ================= NOTIFICACIONES =================

@app.post("/notificaciones")
def crear_notificacion(notificacion: dict, db: Session = Depends(get_db)):
    nuevo = Notificacion(**notificacion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/notificaciones")
def listar_notificaciones(db: Session = Depends(get_db)):
    return db.query(Notificacion).all()


# ================= RESULTADOS =================

@app.post("/resultados")
def crear_resultado(resultado: dict, db: Session = Depends(get_db)):
    nuevo = Resultado(**resultado)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/resultados")
def listar_resultados(db: Session = Depends(get_db)):
    return db.query(Resultado).all()


# ================= CANCHAS =================

@app.post("/canchas")
def crear_cancha(cancha: dict, db: Session = Depends(get_db)):
    nuevo = Cancha(**cancha)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/canchas")
def listar_canchas(db: Session = Depends(get_db)):
    return db.query(Cancha).all()


# ================= REPORTES =================

@app.post("/reportes")
def crear_reporte(reporte: dict, db: Session = Depends(get_db)):
    nuevo = Reporte(**reporte)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/reportes")
def listar_reportes(db: Session = Depends(get_db)):
    return db.query(Reporte).all()