from upnpclient import discover as _upnp_discover

from lametric.device import Time as _Time


def discover(key: str) -> _Time:
    for device in _upnp_discover():
        if device.manufacturer == 'LaMetric Inc.':
            if device.model_name == 'LaMetric Time':
                return _Time(address=device._url_base.replace(':443', '').replace('https://', ''), key=key)
