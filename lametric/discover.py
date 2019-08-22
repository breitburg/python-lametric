from upnpclient import discover as upnp_discover


def discover() -> list:
    """Discover LaMetric devices in the current connected network.

    Returns:
        list: Returns list with a devices objects
    """
    devices = []

    for device in upnp_discover():
        if device.manufacturer == 'LaMetric Inc.':
            devices.append(device)

    return devices
