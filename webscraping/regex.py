import re

base_products = {
    'xiaomi redmi 11': [
        re.compile('.*xiaomi\s*11.*'),
    ],
    'poco m5': [
        re.compile('.*poco\s*m5.*'),
    ],
    'poco f4': [
        re.compile('.*poco\s*f4.*'),
    ],
    'xiaomi redmi note 11': [
        re.compile('.*redmi\s*note\s*11.*'),
        re.compile('.*xiaomi\s*redmi\s*note\s*11.*'),
        re.compile('.*xiaomi\s*note\s*11.*'),
    ],
    'xiaomi redmi 10': [
        re.compile('.*redmi\s*10.*'),
    ],
    'poco m4': [
        re.compile('.*poco\s*m4.*'),
    ],
    'poco x4': [
        re.compile('.*poco\s*x4.*'),
    ],
    'xiaomi redmi a1': [
        re.compile('.*redmi\s*a1.*'),
    ],
    'xiaomi redmi 12': [
        re.compile('.*xiaomi\s*12.*'),
    ],
    'xiaomi redmi 9': [
        re.compile('.*redmi\s*9.*'),
    ],
}