from app.extensions import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(30), unique=True, nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    categoria = db.column(db.String(60), nullable=False)
    costo_importacion = db.Column(db.Float, nullable=False)
    precio_venta = db.Column(db.Float, nullable=False)


    inventarios = db.relationship("Inventario", back_populates="producto")
    ventas = db.relationship("Venta", back_populates="producto")



