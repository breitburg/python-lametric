from base64 import b64encode
from requests import post, get, put, delete

class LaMetric:
    '''
    LaMetric device class.
    '''
    
    # properties
    model = ''
    id = ''
    name = ''
    serial_number = ''
    os_version = ''
    mode = ''
    audio = {}
    bluetooth = {}
    display = {}
    wifi = {}
    apps = {}

    adress = None # ip adress of the device
    __api_info__ = {} # information about device getted in the init

    def __clockrequest__(self, adress, body=None, type='get'):
        request_adress = self.adress + '/api/v' + str(self.__api_info__['version']) + adress
        request_headers = {'Authorization': 'Basic ' + str(b64encode(str.encode('dev:' + self.__api_info__['key']))).replace('b\'', '').replace('\'', '')}
        if type == 'get':
            return get(request_adress, headers=request_headers, data=(body if body == None else body.encode('utf-8'))).json()
        elif type == 'put':
            return put(request_adress, headers=request_headers, data=(body if body == None else body.encode('utf-8'))).json()
        elif type == 'post':
            return post(request_adress, headers=request_headers, data=(body if body == None else body.encode('utf-8'))).json()
        elif type == 'delete':
            return delete(request_adress, headers=request_headers, data=(body if body == None else body.encode('utf-8'))).json()

    def get_device(self):
        '''
        Returns dict with full
        device information.
        '''
        device_request = self.__clockrequest__('/device')
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
        return device_request

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

        return self.__clockrequest__('/device/display', body='{\"brightness\" : ' + ('0' if level == 'auto' else str(level)) + ', \"brightness_mode\" : \"' + ('auto' if level == 'auto' else 'manual') + '\"}', type='put')

    # Applications

    def switch_next_app(self):
        '''
        Switch to the next app on your LaMetric.
        '''
        return self.__clockrequest__('/device/apps/next', type='put')

    def interact_running_widgets(self, package, id):
        '''
        Using this endpoint you can control LaMetric Time apps. Each app provides its own set of actions you can use. For example, you can start or stop radio playback, start, pause, reset timers, configure alarm clock etc.
        '''
        return self.__clockrequest__('/device/apps/' + package + '/widgets/' + str(id) + '/actions', type='post')

    def activate_widget(self, package, id):
        '''
        Allows to make any widget visible using widget id.
        '''
        return self.__clockrequest__('/device/apps/' + package + '/widgets/' + str(id) + '/activate', type='put')

    def switch_prev_app(self):
        '''
        Switch to the previous app on your LaMetric.
        '''
        return self.__clockrequest__('/device/apps/prev', type='put')

    def get_app_details(self, package):
        '''
        Returns dict with app details.
        '''
        return self.__clockrequest__('/device/apps/' + package)

    def get_apps(self):
        '''
        Returns dict with apps info
        '''
        self.apps = self.__clockrequest__('/device/apps/')
        return self.apps

    # Notification

    def send_notification(self, text, icon='', priority='warning', icon_type='info', lifetime=5000):
        '''
        Sending notification to LaMetric.
        '''
        request_body = '{\"priority\" : \"' + priority + '\", \"icon_type\" : \"' + icon_type + '\", \"lifeTime\" : \"' + str(lifetime) + '\", \"model\" : {\"frames\" : [{\"icon\" : \"' + icon + '\", \"text\" : \"' + text + '\"}]}}'
        return self.__clockrequest__('/device/notifications', body=request_body, type='post')

    def get_notifications(self):
        '''
        Returns the list of all notifications in the queue. Notifications with higher priority will be first in the list.
        '''
        return self.__clockrequest__('/device/notifications', type='get')

    def remove_notification(self, id):
        '''
        Removes notification from the queue or in case if it is already visible - dismisses it.
        '''
        return self.__clockrequest__('/device/notifications/' + str(id), type='delete')
    
    # Audio

    def get_audio(self):
        '''
        Returns audio state such as volume.
        '''
        return self.__clockrequest__('/device/audio', type='get')

    def update_audio(self, volume_level):
        '''
        Updates audio state.
        '''
        return self.__clockrequest__('/device/audio', body='{\"volume\" : ' + str(volume_level) + '}', type='put')

    # Wifi

    def get_wifi(self):
        '''
        Returns Wi-Fi state.
        '''
        return self.__clockrequest__('/device/wifi', type='get')

    # Bluetooth

    def get_bluetooth(self):
        '''
        Returns Bluetooth state.
        '''
        return self.__clockrequest__('/device/bluetooth', type='get')

    def update_bluetooth(self, active, name):
        '''
        Updates Bluetooth state.
        '''
        return self.__clockrequest__('/device/bluetooth', body='{\"active\" : ' + str(active) + ', \"name\" : \"' + str(name) + '\"}', type='put')

    def __init__(self, adress, key):
        # setting adress
        if adress.startswith('http://') == False:
            adress = 'http://' + adress
        if adress.endswith(':8080') == False:
            adress = adress + ':8080'

        # setting properties
        self.__api_info__['version'] = 2
        self.adress = adress
        self.__api_info__['key'] = key
        
        # updating properties
        self.get_device()
        self.get_apps()
        