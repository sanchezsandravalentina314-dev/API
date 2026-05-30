from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    correo = Column(String(100))
    contraseña = Column(String(100))
    edad = Column(Integer)
    rol = Column(String(30))


class Propietario(Base):
    __tablename__ = "propietarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_negocio = Column(String(100))
    direccion = Column(String(150))
    telefono = Column(String(20))
    correo = Column(String(100))


class Torneo(Base):
    __tablename__ = "torneos"

    id = Column(Integer, primary_key=True, index=True)
    nombre_torneo = Column(String(100))
    tipo = Column(String(50))
    nivel = Column(String(50))
    fecha = Column(String(20))
    cupos = Column(Integer)
    premio = Column(Float)


class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True, index=True)
    jugador = Column(String(100))
    torneo = Column(String(100))
    fecha_inscripcion = Column(DateTime)
    pago_realizado = Column(Boolean)


class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(100))
    monto = Column(Float)
    metodo_pago = Column(String(50))
    fecha_pago = Column(DateTime)


class Notificacion(Base):
    __tablename__ = "notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100))
    mensaje = Column(String(255))
    fecha_envio = Column(DateTime)


class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    torneo = Column(String(100))
    ganador = Column(String(100))
    puntos = Column(Integer)


class Cancha(Base):
    __tablename__ = "canchas"

    id = Column(Integer, primary_key=True, index=True)
    nombre_cancha = Column(String(100))
    ubicacion = Column(String(150))
    capacidad = Column(Integer)
    disponible = Column(Boolean)


class Reporte(Base):
    __tablename__ = "reportes"

    id = Column(Integer, primary_key=True, index=True)
    tipo_reporte = Column(String(100))
    fecha_generacion = Column(DateTime)
    descripcion = Column(String(255))