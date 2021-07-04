from base64 import b64encode as _b64encode

from munch import munchify as _munchify, Munch as _Munch
from requests import Request as _Request, Session as _Session

from lametric.model.sound import Sound as _Sound
from lametric.model.screensaver import Screensaver as _Screensaver


class Time:
    """Class that represents LaMetric device
    """

    def __init__(self, address: str, key: str, version: str = 'v2'):
        self._key = _b64encode(s=f'dev:{key}'.encode()).decode()

        self._address = address
        self._api_address = f'http://{self._address}:8080/api/{version}'

    def api_call(self, route: str, method: str = 'GET', body: dict = None) -> dict:
        request = _Request(method=method, url=self._api_address + route, json=body,
                           headers={'Authorization': 'Basic ' + self._key})
        response = _Session().send(request=request.prepare()).json()
        if 'errors' in response:
            raise Exception('Response with errors: ' + str(response['errors']))

        return response

    # Apps

    def app_list(self) -> list:
        return [_munchify(x=application) for application in self.api_call(route='/device/apps').values()]

    def get_app(self, identifier: str) -> _Munch:
        return _munchify(x=self.api_call(route=f'/device/apps/{identifier}'))

    def scroll(self, direction: str) -> None:
        self.api_call(route=f'/device/apps/{direction}', method='PUT')

    def interact(self, package_identifier: str, widget_identifier: str, parameters: dict = None,
                 activate: bool = True) -> None:
        self.api_call(route=f'/device/apps/{package_identifier}/widgets/{widget_identifier}/actions', method='POST',
                      body={
                          'id': widget_identifier, 'params': parameters if parameters else {}, 'activate': activate
                      })

    def activate(self, package_identifier: str, widget_identifier: str) -> None:
        self.api_call(route=f'/device/apps/{package_identifier}/widgets/{widget_identifier}/activate', method='PUT')

    # Notifications

    def notify(self, priority: str, icon_type: str, seconds: float, frames: list, sound: _Sound, cycles: int = 1) -> _Munch:
        return _munchify(x=self.api_call(route='/device/notifications', method='POST', body={
            'priority': priority,
            'icon_type': icon_type,
            'lifeTime': seconds * 1000,
            'model': {
                'frames': [frame.to_json() for frame in frames],
                'sound': sound.to_json()
                'cycles': cycles
            }
        }))['success']

    def notification_list(self) -> list:
        return [_munchify(x=notification) for notification in self.api_call(route='/device/notifications')]

    def dismiss_notification(self, identifier: int) -> None:
        self.api_call(route=f'/device/notifications/{identifier}', method='DELETE')

    # Display

    def get_display(self) -> _Munch:
        return _munchify(x=self.api_call(route='/device/display'))

    def set_display(self, brightness: int, brightness_mode: str, screensaver: _Screensaver) -> None:
        target_body = dict()

        if brightness:
            target_body['brightness'] = brightness

        if brightness_mode:
            target_body['brightness_mode'] = brightness_mode

        if screensaver:
            target_body['screensaver'] = screensaver.to_json()

        self.api_call(route='/device/display', method='PUT', body=target_body)

    # Audio

    def get_audio(self) -> _Munch:
        return _munchify(x=self.api_call(route='/device/audio'))

    def set_audio(self, volume: int) -> None:
        self.api_call(route='/device/audio', method='PUT', body={'volume': volume})

    # Bluetooth

    def get_bluetooth(self) -> _Munch:
        return _munchify(x=self.api_call(route='/device/bluetooth'))

    def set_bluetooth(self, activate: bool, name: str) -> _Munch:
        return _munchify(x=self.api_call(route='/device/bluetooth', method='PUT', body={'activate': activate, 'name': name}))['success']['data']

    # Wi-Fi

    def get_wifi(self) -> _Munch:
        return _munchify(x=self.api_call(route='/device/wifi'))

    # Status

    def get_status(self) -> _Munch:
        return _munchify(x=self.api_call(route='/device'))
