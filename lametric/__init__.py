from base64 import b64encode
from requests import post, get, put

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

        return self.__clockrequest__(adress='/device/display', body='{\"brightness\" : ' + ('0' if level == 'auto' else str(level)) + ', \"brightness_mode\" : \"' + ('auto' if level == 'auto' else 'manual') + '\"}', type='put')

    # Applications

    def switch_next_app(self):
        '''
        Switch to the next app on your LaMetric.
        '''
        return self.__clockrequest__(adress='/device/apps/next', type='put')

    def switch_prev_app(self):
        '''
        Switch to the previous app on your LaMetric.
        '''
        return self.__clockrequest__(adress='/device/apps/prev', type='put')

    def get_app_details(self, package):
        '''
        Returns dict with app details.
        '''
        return self.__clockrequest__(adress='/device/apps/' + package)

    def get_apps(self):
        '''
        Returns dict with apps info
        '''
        self.apps = self.__clockrequest__(adress='/device/apps/')
        return self.apps

    # Notification

    def send_notification(self, text, icon='', priority='warning', icon_type='info', lifetime=5000):
        '''
        Sending notification to LaMetric.
        '''
        request_body = '{\"priority\" : \"' + priority + '\", \"icon_type\" : \"' + icon_type + '\", \"lifeTime\" : \"' + str(lifetime) + '\", \"model\" : {\"frames\" : [{\"icon\" : \"' + icon + '\", \"text\" : \"' + text + '\"}]}}'
        return self.__clockrequest__('/device/notifications', body=request_body, type='post')

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
        