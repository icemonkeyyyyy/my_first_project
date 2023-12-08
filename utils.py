from PIL import Image
import filters


def save_image(img: Image.Image, image_filter: filters.Filter, path_to_save: str) -> bool:
    """
    Применяет фильтр и сохраняет изображение
    :param img: Объект изображения
    :param image_filter: Фильтр для изображения
    :param path_to_save: Путь куда сохранить
    :return: Удалось ли сохранить True - Успешно, False - Неудачно
    """
    try:
        # Применяем фильтр и сохраняем изображение
        image_filter.apply_to_image(img)
        img.save(path_to_save)
        return True
    except ValueError:
        # При неудачном сохранении
        return False
