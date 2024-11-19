class Model:
    def __init__(self, host, mac_address, d_type):
        self._host = host
        self._mac_address = mac_address
        self._d_type = d_type


    @property
    def get_host(self):
        return self._host

    @property
    def get_mac_address(self):
        return self._mac_address

    @property
    def get_d_type(self):
        return self._d_type
