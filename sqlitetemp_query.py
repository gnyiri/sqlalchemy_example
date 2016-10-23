from sqlitetemp_init import Network, Host, DeviceServer, Device
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)
session = DBSession()
networks = session.query(Network).all()

for network in networks:
    hosts = session.query(Host).filter(Host.network == network)
    for host in hosts:
        device_servers = session.query(DeviceServer).filter(DeviceServer.host == host)
        for device_server in device_servers:
            devices = session.query(Device).filter(Device.device_server == device_server)
            for device in devices:
                print(network.name + ":" + host.name + ":" + device_server.device_class +
                "/" + device_server.instance + "/" + device.name)
