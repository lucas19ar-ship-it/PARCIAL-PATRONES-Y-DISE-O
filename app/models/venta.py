from datetime import datetime

from app.extensions import db 

class Venta(db.Model):
    __tablename__ = "ventas"

    id = db.Column(db.Integer, primary_Key=True)
    filial_id = db.Column(db.Integer, db.ForeignKey("filiales.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now, nullable=False)

    filial = db.relationship("Filial", back_populates="ventas")
    producto = db.relationship("Producto", back_populates="ventas")
    
    