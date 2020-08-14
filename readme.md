![](https://i.imgur.com/Qju3dvw.png)  

Unofficial LaMetric Time API wrapper written on Python.

## Usage
> You can get device key [here](https://developer.lametric.com/user/devices).

Example of automatic discovery:

```python
from lametric.discovery import discover

device = discover(key='****************************************************************')
```

Example of sending notification:

```python
from lametric.model.enum import NotificationPriorities, SoundCategories, Sounds, IconTypes
from lametric.model.frame import Text
from lametric.model.sound import Sound

device.notify(
    priority=NotificationPriorities.info,
    icon_type=IconTypes.alert,
    seconds=3,
    frames=[
        Text(text='Hello, world')
    ],
    sound=Sound(
        category=SoundCategories.notification,
        identifier=Sounds.cat
    )
)
```

All other available methods:

| Method                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Time.api_call(route: str, method: str = 'GET', body: dict)`                                                | Basic API call that used for all methods                                                                                                                                                                                                                                                                                                                                          |
| `Time.app_list()`                                                                                           | Returns apps currently installed on LaMetric Time. Each app is identified by package name. Device can run multiple instances of an app. These instances are called widgets. There are at least one widget (instance) running for each app.                                                                                                                                        |
| `Time.get_app(identifier: str)`                                                                             | Returns information about currently installed app identified by the package.                                                                                                                                                                                                                                                                                                      |
| `Time.scroll(direction: str)`                                                                               | Allows to switch to the next or previous app on LaMetric Time. App order is controlled by the user via LaMetric Time app.                                                                                                                                                                                                                                                         |
| `Time.interact(package_identifier: str, widget_identifier: str, parameters: dict, activate: bool)`          | Using this method you can control LaMetric Time apps. Each app provides its own set of actions you can use. For example, you can start or stop radio playback, start, pause, reset timers, configure alarm clock etc. To execute an action just send an Action object in the body of the request to the endpoint like this:                                                       |
| `Time.activate(package_identifier: str, widget_identifier: str)`                                            | Allows to make any widget visible using widget id.                                                                                                                                                                                                                                                                                                                                |
| `Time.notify(priority: str, icon_type: str, seconds: float, frames: list, sound: model.Sound, cycles: int)` | Sends notification to the device.                                                                                                                                                                                                                                                                                                                                                 |
| `Time.notification_list()`                                                                                  | Returns the list of all notifications in the queue. Notifications with higher priority will be first in the list.                                                                                                                                                                                                                                                                 |
| `Time.dismiss_notification(identifier: int)`                                                                | Removes notification from the queue or in case if it is already visible - dismisses it.                                                                                                                                                                                                                                                                                           |
| `Time.get_display()`                                                                                        | Returns information about the display like brightness, mode and size in pixels. Since version 2.1.0 returns information about screen saver settings.                                                                                                                                                                                                                              |
| `Time.set_display(brightness: int, brightness_mode: str, screensaver: model.Screensaver)`                   | Updates display state. It is possible to change brightness, mode and screen saver settings. If brightness_mode is set to “auto”, brightness value still can be changed but this will not affect the actual brightness of the display. Brightness will be changed as soon as brightness_mode is set to “manual”. Since API 2.1.0 it is possible to configure screensaver settings. |
| `Time.get_audio()`                                                                                          | Returns audio state such as volume.                                                                                                                                                                                                                                                                                                                                               |
| `Time.set_audio(volume: int)`                                                                               | Updates audio state.                                                                                                                                                                                                                                                                                                                                                              |
| `Time.get_bluetooth()`                                                                                      | Returns Bluetooth state.                                                                                                                                                                                                                                                                                                                                                          |
| `Time.set_bluetooth(activate: bool, name: str)`                                                             | Updates Bluetooth state.                                                                                                                                                                                                                                                                                                                                                          |
| `Time.get_wifi()`                                                                                           | Returns Wi-Fi state.                                                                                                                                                                                                                                                                                                                                                              |
| `Time.get_status()`                                                                                         | Returns information about the device like name, serial number, version of the firmware, model etc. Response also contains state of audio, display, bluetooth and wi-fi.                                                                                                                                                                                                           |

## Installation

- Installation using [pip](https://github.com/pypa/pip)
    1. Open terminal and execute
    ```bash
    $ pip install lametric
    ```

- Installation and building from sources
    1. Clone repository using `git`
        ```bash
        $ git clone https://github.com/breitburg/python-lametric/
        ```
    2. Install through [setuptools](https://github.com/pypa/setuptools)
        ```bash
        $ python setup.py install
        ```

## Changelog

**Release 2.0.0** (Aug 14, 2020)

Fully refactored architecture and implementation of all newest LaMetric API features. Also added device discovery.

**Release 1.0.0** (Nov 30, 2018)

Initial release.