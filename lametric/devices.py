from base64 import b64encode
from requests import post, get, put, delete
from json import dumps


class BaseDevice:
    def __init__(self, address, key):
        if not address.startswith('http://'):
            address = 'http://' + address
        if not address.endswith(':8080'):
            address = address + ':8080'

        self.address = address
        self.__api_info__ = dict(version=2, key=key)

    def __api_call__(self, address, body=None, type='get'):
        request_address = self.address + '/api/v' + str(self.__api_info__['version']) + address
        request_headers = {
            'Authorization': 'Basic ' + str(b64encode(str.encode('dev:' + self.__api_info__['key']))).replace('b\'',
                                                                                                              '').replace(
                '\'', '')}

        if type == 'get':
            function = get
        elif type == 'put':
            function = put
        elif type == 'post':
            function = post
        elif type == 'delete':
            function = delete

        return function(request_address, headers=request_headers,
                        data=(body if body is None else body.encode('utf-8'))).json()


class Time(BaseDevice):
    """LaMetric Time device object represents all functions and properties.

    Args:
        address (str): Device address in local network
        key (str): Device API-key from `developer.lametric.com/user/devices`

    Attributes:
        address (str): Device address in local network
        id (str): Id of the device on the cloud
        name (str): User specified name of the device
        serial_number (str): Device serial number
        os_version (str): Software version in format <major>.<minor>.<patch>
        model (str): Model number
        mode (str): Current device mode. Can be one of “auto”, “manual” or “kiosk”
        model (:obj:`int`, optional): Description of `attr2`.
    """

    def __init__(self, address, key):
        super().__init__(address=address, key=key)

        # Getting properties
        device_request = self.__api_call__('/device')
        self.model = device_request['model']
        self.id = device_request['id']
        self.name = device_request['name']
        self.serial_number = device_request['serial_number']
        self.os_version = device_request['os_version']
        self.mode = device_request['mode']
        self.audio = device_request['audio']
        self.bluetooth = device_request['bluetooth']
        self.display = device_request['display']
        self.wifi = device_request['wifi']

        # updating properties
        self.get_device()
        self.get_apps()

    def get_device(self):
        '''
        Returns dict with full
        device information.
        '''

    # Display

    def set_brightness(self, level):
        '''
        Set the brightness of your LaMetric.

        int level - Brightness level
        or string 'auto' if you want
        set auto mode.
        '''
        if level == 'auto':
            self.display['brightness'] == 0
        else:
            self.display['brightness'] = level
        self.display['brightness_mode'] = ('auto' if level == 'auto' else 'manual')

        return self.__api_call__('/device/display', body='{\"brightness\" : ' + (
            '0' if level == 'auto' else str(level)) + ', \"brightness_mode\" : \"' + (
                                                             'auto' if level == 'auto' else 'manual') + '\"}',
                                 type='put')

    # Applications

    def switch_next_app(self):
        '''
        Switch to the next app on your LaMetric.
        '''
        return self.__api_call__('/device/apps/next', type='put')

    def interact_running_widgets(self, package, id):
        '''
        Using this endpoint you can control LaMetric Time apps. Each app provides its own set of actions you can use. For example, you can start or stop radio playback, start, pause, reset timers, configure alarm clock etc.
        '''
        return self.__api_call__('/device/apps/' + package + '/widgets/' + str(id) + '/actions', type='post')

    def activate_widget(self, package, id):
        '''
        Allows to make any widget visible using widget id.
        '''
        return self.__api_call__('/device/apps/' + package + '/widgets/' + str(id) + '/activate', type='put')

    def switch_prev_app(self):
        '''
        Switch to the previous app on your LaMetric.
        '''
        return self.__api_call__('/device/apps/prev', type='put')

    def get_app_details(self, package):
        '''
        Returns dict with app details.
        '''
        return self.__api_call__('/device/apps/' + package)

    def get_apps(self):
        '''
        Returns dict with apps info
        '''
        self.apps = self.__api_call__('/device/apps/')
        return self.apps

    # Notification

    def send_notification(self, text, icon='', priority='warning', icon_type='info', lifetime=5000):
        '''
        Sending notification to LaMetric.
        '''
        request_body = '{\"priority\" : \"' + priority + '\", \"icon_type\" : \"' + icon_type + '\", \"lifeTime\" : \"' + str(
            lifetime) + '\", \"model\" : {\"frames\" : [{\"icon\" : \"' + icon + '\", \"text\" : \"' + text + '\"}]}}'
        return self.__api_call__('/device/notifications', body=request_body, type='post')

    def get_notifications(self):
        '''
        Returns the list of all notifications in the queue. Notifications with higher priority will be first in the list.
        '''
        return self.__api_call__('/device/notifications', type='get')

    def remove_notification(self, id):
        '''
        Removes notification from the queue or in case if it is already visible - dismisses it.
        '''
        return self.__api_call__('/device/notifications/' + str(id), type='delete')

    # Audio

    def get_audio(self):
        '''
        Returns audio state such as volume.
        '''
        return self.__api_call__('/device/audio', type='get')

    def update_audio(self, volume_level):
        '''
        Updates audio state.
        '''
        return self.__api_call__('/device/audio', body='{\"volume\" : ' + str(volume_level) + '}', type='put')

    # Wifi

    def get_wifi(self):
        '''
        Returns Wi-Fi state.
        '''
        return self.__api_call__('/device/wifi', type='get')

    # Bluetooth

    def get_bluetooth(self):
        '''
        Returns Bluetooth state.
        '''
        return self.__api_call__('/device/bluetooth', type='get')

    def update_bluetooth(self, active, name):
        '''
        Updates Bluetooth state.
        '''
        return self.__api_call__('/device/bluetooth',
                                 body='{\"active\" : ' + str(active) + ', \"name\" : \"' + str(name) + '\"}',
                                 type='put')
