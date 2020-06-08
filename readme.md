![](https://i.imgur.com/Qju3dvw.png)  

## Requirements

- Python 3
- Pip

## Installation

- Installation from sources
    1. Clone repository using `git`
        ```sh
        git clone https://github.com/breitburg/python-lametric/
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

## Usage

Device key you can get [here](https://developer.lametric.com/user/devices).

```python
from lametric import discover
time = discover(key='4bcb680cff14bcb680cff14bcb680cff14bcb680cff1')[0]

# Setting brightness
time.set_brightness(100)

# Switching apps
time.switch_next_app()
time.switch_prev_app()

# Sending notifications
time.send_notification(text='Hello from Python!', icon='24675')

# Setting notifications
notifications = time.get_notifications()

# Removing all notifications
for notification_dict in notifications:
    time.remove_notification(notification_dict['id'])
```