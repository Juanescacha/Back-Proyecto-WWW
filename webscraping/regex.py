import re

base_products = {
    'xiaomi redmi 11': [
        re.compile('.*xiaomi\s*11.*'),
        re.compile('.*redmi\s*11.*'),
        re.compile('.*xiaomi\s*redmi\s*11.*'),
    ],
    'poco m5': [
        re.compile('.*poco\s*m5.*'),
        re.compile('.*xiaomi\s*poco\s*m5.*'),
    ],
    'poco f4': [
        re.compile('.*poco\s*f4.*'),
        re.compile('.*xiaomi\s*poco\s*f4.*'),
    ],
    'xiaomi redmi note 11': [
        re.compile('.*redmi\s*note\s*11.*'),
        re.compile('.*xiaomi\s*redmi\s*note\s*11.*'),
        re.compile('.*xiaomi\s*note\s*11.*'),
    ],
    'xiaomi redmi 10': [
        re.compile('.*redmi\s*10.*'),
        re.compile('.*xiaomi\s*redmi\s*10.*'),
        re.compile('.*xiaomi\s*10.*'),
    ],
    'poco m4': [
        re.compile('.*poco\s*m4.*'),
        re.compile('.*xiaomi\s*poco\s*m4.*'),
    ],
    'poco x4': [
        re.compile('.*poco\s*x4.*'),
        re.compile('.*xiaomi\s*poco\s*x4.*'),
    ],
    'xiaomi redmi a1': [
        re.compile('.*redmi\s*a1.*'),
        re.compile('.*xiaomi\s*redmi\s*a1.*'),
        re.compile('.*xiaomi\s*a1.*'),
    ],
    'xiaomi redmi 12': [
        re.compile('.*xiaomi\s*12.*'),
        re.compile('.*xiaomi\s*redmi\s*12.*'),
        re.compile('.*redmi\s*12.*'),
    ],
    'xiaomi redmi 9': [
        re.compile('.*redmi\s*9.*'),
        re.compile('.*xiaomi\s*redmi\s*9.*'),
        re.compile('.*xiaomi\s*9.*'),
    ],
    #iphone's
    'iphone 5': [
        re.compile('.*iphone\s*5.*'),
    ],
    'iphone 7': [
        re.compile('.*iphone\s*7.*'),
    ],
    'iphone 8': [
        re.compile('.*iphone\s*8.*'),
    ],
    'iphone 11': [
        re.compile('.*iphone\s*11.*'),
    ],
    'iphone 12': [
        re.compile('.*iphone\s*12.*'),
    ],
    'iphone 13': [
        re.compile('.*iphone\s*13.*'),
    ],
    'iphone 14': [
        re.compile('.*iphone\s*14.*'),
    ],
    'iphone se': [
        re.compile('.*iphone\s*se.*'),
    ],
    'iphone x': [
        re.compile('.*iphone\s*x.*'),
    ],
    #samsung
    'samsung galaxy s10': [
        re.compile('.*samsung\s*galaxy\s*s\s*10.*'),
        re.compile('.*samsung\s*s\s*10.*'),
        re.compile('.*galaxy\s*s\s*10.*'),
    ],
    'samsung galaxy s20': [
        re.compile('.*samsung\s*galaxy\s*s\s*20.*'),
        re.compile('.*samsung\s*s\s*20.*'),
        re.compile('.*galaxy\s*s\s*20.*'),
    ],
    'samsung galaxy s21': [
        re.compile('.*samsung\s*galaxy\s*s\s*21.*'),
        re.compile('.*samsung\s*s\s*21.*'),
        re.compile('.*galaxy\s*s\s*21.*'),
    ],
    'samsung galaxy s22': [
        re.compile('.*samsung\s*galaxy\s*s\s*22.*'),
        re.compile('.*samsung\s*s\s*22.*'),
        re.compile('.*galaxy\s*s\s*22.*'),
    ],
    'samsung galaxy tab s7': [
        re.compile('.*samsung\s*galaxy\s*tab\s*s\s*7.*'),
        re.compile('.*samsung\s*tab\s*s\s*7.*'),
        re.compile('.*galaxy\s*tab\s*s\s*7.*'),
    ],
    'samsung galaxy note 10': [
        re.compile('.*samsung\s*galaxy\s*note\s*10.*'),
        re.compile('.*samsung\s*note\s*10.*'),
        re.compile('.*galaxy\s*note\s*10.*'),
    ],
    'samsung galaxy note 20': [
        re.compile('.*samsung\s*galaxy\s*note\s*20.*'),
        re.compile('.*samsung\s*note\s*20.*'),
        re.compile('.*galaxy\s*note\s*20.*'),
    ],
    'samsung galaxy z flip': [
        re.compile('.*samsung\s*galaxy\s*z\s*flip.*'),
        re.compile('.*samsung\s*z\s*flip.*'),
        re.compile('.*galaxy\s*z\s*flip.*'),
    ],
    'samsung galaxy z fold': [
        re.compile('.*samsung\s*galaxy\s*z\s*fold.*'),
        re.compile('.*samsung\s*z\s*fold.*'),
        re.compile('.*galaxy\s*z\s*fold.*'),
    ],
    'samsung galaxy a01': [
        re.compile('.*samsung\s*galaxy\s*a01.*'),
        re.compile('.*samsung\s*a01.*'),
        re.compile('.*galaxy\s*a01.*'),
    ],
    'samsung galaxy a03': [
        re.compile('.*samsung\s*galaxy\s*a03.*'),
        re.compile('.*samsung\s*a03.*'),
        re.compile('.*galaxy\s*a03.*'),
    ],
    'samsung galaxy a12': [
        re.compile('.*samsung\s*galaxy\s*a12.*'),
        re.compile('.*samsung\s*a12.*'),
        re.compile('.*galaxy\s*a12.*'),
    ],
    'samsung galaxy a13': [
        re.compile('.*samsung\s*galaxy\s*a13.*'),
        re.compile('.*samsung\s*a13.*'),
        re.compile('.*galaxy\s*a13.*'),
    ],
    'samsung galaxy a22': [
        re.compile('.*samsung\s*galaxy\s*a22.*'),
        re.compile('.*samsung\s*a22.*'),
        re.compile('.*galaxy\s*a22.*'),
    ],
    'samsung galaxy a32': [
        re.compile('.*samsung\s*galaxy\s*a32.*'),
        re.compile('.*samsung\s*a32.*'),
        re.compile('.*galaxy\s*a32.*'),
    ],
    'samsung galaxy a33': [
        re.compile('.*samsung\s*galaxy\s*a33.*'),
        re.compile('.*samsung\s*a33.*'),
        re.compile('.*galaxy\s*a33.*'),
    ],
    'samsung galaxy a53': [
        re.compile('.*samsung\s*galaxy\s*a53.*'),
        re.compile('.*samsung\s*a53.*'),
        re.compile('.*galaxy\s*a53.*'),
    ],
    'samsung galaxy a72': [
        re.compile('.*samsung\s*galaxy\s*a72.*'),
        re.compile('.*samsung\s*a72.*'),
        re.compile('.*galaxy\s*a72.*'),
    ],
    'samsung galaxy m12': [
        re.compile('.*samsung\s*galaxy\s*m12.*'),
        re.compile('.*samsung\s*m12.*'),
        re.compile('.*galaxy\s*m12  .*'),
    ],
    'samsung galaxy m13': [
        re.compile('.*samsung\s*galaxy\s*m13.*'),
        re.compile('.*samsung\s*m13.*'),
        re.compile('.*galaxy\s*m13.*'),
    ],
    'samsung galaxy m32': [
        re.compile('.*samsung\s*galaxy\s*m32.*'),
        re.compile('.*samsung\s*m32.*'),
        re.compile('.*galaxy\s*m32.*'),
    ],
}