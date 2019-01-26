![](https://i.imgur.com/Qju3dvw.png)  

## Todo
Current development status:

| Title             | State |
|-------------------|:-----:|
| Device Discovery  |   ⛔️  |
| Device            |   ✅  |
| Apps              |   ✅  |
| Notifications     |   ✅  |
| Display           |   ✅  |
| Audio             |   ✅  |
| Bluetooth         |   ✅  | 
| Wi-Fi             |   ✅  |

✅ – Working
☢️ – Working, but not all functions are ready
⛔️ – In development

## Requirements

- Python 3
- Pip

## Installation

- Installation from sources
    1. Clone repository using `git`
        ```sh
        git clone http://github.com/ketsu8/python-lametric/
        ```
    2. Install through [setuptools](https://github.com/pypa/setuptools)
        ```sh
        python setup.py install
        ```

- Installation using [pip](https://github.com/pypa/pip)
    1. Open terminal and type
    ```sh
    pip install lametric
    ```

## Example

Device key you can get [here](https://developer.lametric.com/user/devices).

```python
from lametric import LaMetric

clock = LaMetric(adress='192.168.0.199', key='dla7or4bcb680cff1887b1fcf60b2a66cfe51c46f53bbd8651a73e961f98p2a6')

# getting properties
print('Clock name is ' + clock.name)

# setting brightness
clock.set_brightness(100)

# switching apps
clock.switch_next_app()
clock.switch_prev_app()

# sending notifications
clock.send_notification(text='Hello from Python!', icon='24675')

# getting notifications
notifications = clock.get_notifications()

# removing all notifications
for notification_dict in notifications:
    clock.remove_notification(notification_dict['id'])

```
