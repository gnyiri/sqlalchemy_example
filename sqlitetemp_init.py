from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Network(Base):
    __tablename__ = "network"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Host(Base):
    __tablename__ = "host"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    ip = Column(String(255), nullable=False)
    network_id = Column(Integer, ForeignKey('network.id'))
    network = relationship(Network)

class DeviceServer(Base):
    __tablename__ = "device_server"

    id = Column(Integer, primary_key=True)
    device_class = Column(String(255), nullable=False)
    instance = Column(String(255), nullable=False)
    host_id = Column(Integer, ForeignKey('host.id'))
    host = relationship(Host)


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    device_server_id = Column(Integer, ForeignKey('device_server.id'))
    device_server = relationship(DeviceServer)


engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)
