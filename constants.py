___all__ = ['UUIDS']


class Immutable(type):

    def __call__(*args):
        raise Exception("You can't create instance of immutable object")

    def __setattr__(*args):
        raise Exception("You can't modify immutable object")


class UUIDS(object):
    BASE = "0000%s-0000-1000-8000-00805f9b34fb"
    svc = {}

    svc['MIBAND1'] = BASE % 'fee0'
    svc['MIBAND2'] = BASE % 'fee1'

    svc['ALERT'] = BASE % '1802'
    svc['ALERT_NOTIFICATION'] = BASE % '1811'
    svc['HEART_RATE'] = BASE % '180d'
    svc['DEVICE_INFO'] = BASE % '180a'

    svc_by_uuid = {}
    for k in svc:
        svc_by_uuid[svc[k]] = k
    char = {}

    char['HZ'] = "00000002-0000-3512-2118-0009af100700"
    char['SENSOR'] = "00000001-0000-3512-2118-0009af100700"
    char['AUTH'] = "00000009-0000-3512-2118-0009af100700"
    char['HEART_RATE_MEASURE'] = "00002a37-0000-1000-8000-00805f9b34fb"
    char['HEART_RATE_CONTROL'] = "00002a39-0000-1000-8000-00805f9b34fb"
    char['ALERT'] = "00002a06-0000-1000-8000-00805f9b34fb"
    char['BATTERY'] = "00000006-0000-3512-2118-0009af100700"
    char['STEPS'] = "00000007-0000-3512-2118-0009af100700"
    char['LE_PARAMS'] = BASE % "ff09"
    char['REVISION'] = 0x2a28
    char['SERIAL'] = 0x2a25
    char['HRDW_REVISION'] = 0x2a27
    char['CONFIGURATION'] = "00000003-0000-3512-2118-0009af100700"
    char['DEVICEEVENT'] = "00000010-0000-3512-2118-0009af100700"

    char['CURRENT_TIME'] = BASE % '2a2b'
    char['AGE'] = BASE % '2a80'
    char['USER_SETTINGS'] = "00000008-0000-3512-2118-0009af100700"

    char_by_uuid = {}
    for k in char:
        char_by_uuid[char[k]] = k

    notif = {}
    notif['DESCRIPTOR'] = 0x2902


class AUTH_STATES(object):

    __metaclass__ = Immutable

    AUTH_OK = "Auth ok"
    AUTH_FAILED = "Auth failed"
    ENCRIPTION_KEY_FAILED = "Encryption key auth fail, sending new key"
    KEY_SENDING_FAILED = "Key sending failed"
    REQUEST_RN_ERROR = "Something went wrong when requesting the random number"


class ALERT_TYPES(object):

    __metaclass__ = Immutable

    NONE = b'\x00'
    MESSAGE = b'\x01'
    PHONE = b'\x02'


class QUEUE_TYPES(object):

    __metaclass__ = Immutable

    HEART = 'heart'
    RAW_ACCEL = 'raw_accel'
    RAW_HEART = 'raw_heart'
