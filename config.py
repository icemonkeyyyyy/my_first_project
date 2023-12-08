from filters import ReplaceWhiteFilter, ContrastFiler, InverseFilter, WatterRippleFilter
import enum


class ConfigVariables(enum.Enum):
    # Словарь фильтров
    image_filters = {
        0: {
            'name': "Выход",
            'description': "Выходит из программы",
            'class': None
        },
        1: {
            'name': "Белый рандом",
            'description': "Заменить белый цвет на рандомный",
            'class': ReplaceWhiteFilter()
        },
        2: {
            'name': "Инверсия",
            'description': "Делает инверсию цветов для каждого пикселя",
            'class': InverseFilter()
        },
        3: {
            'name': "Повысить контраст",
            'description': "Делает изображение контрастнее",
            'class': ContrastFiler()
        },
        4: {
            'name': "Волна",
            'description': "Создает эффект волны",
            'class': WatterRippleFilter()
        }
    }

    agree_inputs = ['да', 'lf', 'da', 'yes']
    disagree_inputs = ['нет', 'ytn', 'net', 'no']
    correct_inputs = ['да', 'lf', 'da', 'yes', 'нет', 'ytn', 'net', 'no']

