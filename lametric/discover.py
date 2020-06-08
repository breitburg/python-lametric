from upnpclient import discover as upnp_discover
from lametric.devices import Time, BaseDevice


def discover(key: str) -> list:
    """Discover LaMetric devices in the current connected network.

    Returns:
        list: Returns list with a devices objects
    """

    devices = list()

    for device in upnp_discover():
        if device.manufacturer == 'LaMetric Inc.':
            if device.model_name == 'LaMetric Time':
                devices.append(Time(address=device.location.split('/')[2].split(':')[0], key=key))

    return devices
