from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlitetemp_init import Network, Host, DeviceServer, Device

engine = create_engine('sqlite:///database.db')

Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# network
network_bt_controller = Network(name='bt_controller')
session.add(network_bt_controller)
# network
network_laser_controller = Network(name='laser_controller')
session.add(network_laser_controller)

# host
host_bt_controller = Host(name='bt_controller', ip='1.1.1.1', network=network_bt_controller)
session.add(host_bt_controller)
host_bt_simulator = Host(name='bt_simulator', ip='1.1.1.2', network=network_bt_controller)
session.add(host_bt_simulator)
# host
host_laser_controller = Host(name='laser_controller', ip='1.1.2.1', network=network_laser_controller)
session.add(host_laser_controller)
host_laser_simulator = Host(name='laser_controller', ip='1.1.2.2', network=network_laser_controller)
session.add(host_laser_simulator)

# device_server
device_server_BT_A = DeviceServer(device_class='BT_A', instance='1', host=host_bt_controller)
session.add(device_server_BT_A)
# device_server
device_server_BT_B = DeviceServer(device_class='BT_B', instance='1', host=host_bt_simulator)
session.add(device_server_BT_B)
# device_server
device_server_LC_A = DeviceServer(device_class='LC_A', instance='1', host=host_laser_controller)
session.add(device_server_LC_A)
# device_server
device_server_LC_B = DeviceServer(device_class='LC_B', instance='1', host=host_laser_simulator)
session.add(device_server_LC_B)

device_BT_A_a1 = Device(name='bt/a/1', device_server=device_server_BT_A)
session.add(device_BT_A_a1)
device_BT_B_a1 = Device(name='bs/a/1', device_server=device_server_BT_B)
session.add(device_BT_B_a1)
device_LC_A_a1 = Device(name='lc/a/1', device_server=device_server_LC_A)
session.add(device_LC_A_a1)
device_LC_B_a1 = Device(name='ls/a/1', device_server=device_server_LC_B)
session.add(device_LC_B_a1)

session.commit()
