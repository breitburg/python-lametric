![](https://i.imgur.com/Qju3dvw.png)  

## Todo
Current development status:

| Title         | State |
|---------------|:-----:|
| Device        |   ✅  |
| Apps          |   ☢️  |
| Notifications |   ⛔️  |
| Display       |   ✅  |
| Audio         |   ⛔️  |
| Bluetooth     |   ⛔️  |
| Wi-Fi         |   ⛔️  |

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
    pip install python-lametric
    ```

## Example

```python
from lametric import LaMetric
from time import sleep

time = LaMetric(adress='192.168.0.199', key='dla7or4bcb680cff1887b1fcf60b2a66cfe51c46f53bbd8651a73e961f98p2a6')

# getting properties
print('Hello from ' + time.name)

# setting brightness
time.set_brightness(100)

# switching apps
time.switch_next_app()
sleep(1)
time.switch_prev_app()
```