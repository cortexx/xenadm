class VM:
    """ A simple class representing a VM"""
    id 		= "0000000"
    ip 		= "x.x.x.x"
    name 	= "x.x.x.x"
    status	= "x.x.x.x"

    def __init__(self, ip="0.0.0.0", name="vmname", status="status", id="0000000"):
        self.id = id
        self.ip = ip
        self.name = name
        self.status = status

