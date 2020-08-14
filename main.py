from lametric.device import Time
from lametric.model.enum import NotificationPriorities, SoundCategories, Sounds, IconTypes
from lametric.model.frame import Text
from lametric.model.sound import Sound

device = Time(address='192.168.1.118', key='df3f14bcb680cff1887b1fcf60b2a0deee51c46f53bbd8651a73e961f987ded1')

device.notify(priority=NotificationPriorities.info, icon_type=IconTypes.alert, seconds=3,
              frames=[Text(text='bitch')],
              sound=Sound(category=SoundCategories.notification, identifier=Sounds.cat))
