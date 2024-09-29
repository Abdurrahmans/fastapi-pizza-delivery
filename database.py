from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




engine=create_engine('postgresql://odoo_15_dev:12345@localhost/pizza_delivery',
    echo=True
)

Base = declarative_base()
Session = sessionmaker()