supportedLang = ['zh', 'en']


class l:
    LANGS = {
        'zh': 0,
        'en': 1,
    }
    n = None  # 当前使用的语言编号


import sys

if '--lang' in sys.argv:
    try:
        idx = sys.argv.index('--lang')
        lang = sys.argv[idx + 1]
        if lang in supportedLang:
            l.n = l.LANGS[lang]
    except:
        ...

if l.n is None:
    import locale

    if 'zh_CN' in locale.getdefaultlocale():
        l.n = l.LANGS['zh']
    else:
        l.n = l.LANGS['en']

def singleton(cls):
    instances = {}

    def get_instances():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instances


@singleton
class YamlRead:
    def __init__(self, file_path='config.yaml'):
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
        with open(self.file_path) as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_data(self):
        return self.data


def get(key):
    data = YamlRead().get_data()
    return data.get('config').get(key, None)