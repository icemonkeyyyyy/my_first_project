from PIL import Image
from random import randint
import numpy as np


class Filter:
    """
    Базовый класс фильтров
    """

    def apply_to_pixel(self, pixel: int) -> int:
        """
        Применяет фильтр к одному пикселю
        :param pixel: кортеж RGB цветов пикселя
        :return: кортеж RGB цветов нового пикселя
        """
        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: Объект изображения
        :return: Объект изображения
        """
        for i in range(img.width):
            for j in range(img.height):
                pixel = img.getpixel((i, j))

                new_pixel = self.apply_to_pixel(pixel)

                img.putpixel((i, j), new_pixel)
        return img


class ContrastFiler(Filter):
    """
    Фильтр, делающий изображение контрастнее
    """

    # Метод приватный, чтобы нельзя было вызвать вне класса
    # Так как у нас нет фильтров к пикселю, след и метод можно сделать приватным
    @staticmethod
    def __apply_to_pixel(pixel: tuple) -> tuple:
        """
        Применяет фильтр к одному пикселю
        :param pixel: кортеж RGB цветов пикселя
        :return: кортеж RGB цветов нового пикселя
        """
        new_pixel = []
        for color in pixel:
            if 255 - color > color:
                new_pixel.append(max(color // 2, 0))
            else:
                new_pixel.append(min(color * 2, 255))

        new_pixel = tuple(new_pixel)

        return new_pixel

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: Объект изображения
        :return: Объект изображения
        """
        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))
                new_pixel = self.__apply_to_pixel(pixel)

                img.putpixel((x, y), new_pixel)
        return img


class InverseFilter(Filter):
    @staticmethod
    def __apply_to_pixel(pixel: tuple) -> tuple:
        """
        Применяет фильтр к одному пикселю
        :param pixel: кортеж RGB цветов пикселя
        :return: кортеж RGB цветов нового пикселя
        """
        new_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        return new_pixel

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: Объект изображения
        :return: Объект изображения
        """
        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))
                new_pixel = self.__apply_to_pixel(pixel)

                img.putpixel((x, y), new_pixel)
        return img


class ReplaceWhiteFilter(Filter):
    @staticmethod
    def __apply_to_pixel(pixel: tuple) -> tuple:
        """
        Применяет фильтр к одному пикселю
        :param pixel: кортеж RGB цветов пикселя
        :return: кортеж RGB цветов нового пикселя
        """
        new_pixel = pixel
        if pixel[0] in range(200, 256) and pixel[1] in range(200, 256) and pixel[2] in range(200, 256):
            new_pixel = (
                randint(0, 255), randint(0, 255), randint(0, 255)
            )
        return new_pixel

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: Объект изображения
        :return: Объект изображения
        """
        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))
                new_pixel = self.__apply_to_pixel(pixel)
                img.putpixel((x, y), new_pixel)
        return img


class WatterRippleFilter(Filter):
    @staticmethod
    def __create_ripple_effect(data: np.ndarray, scale: int, offset: int) -> np.ndarray:
        """
        Создает эффект волны на изображении
        :param data: Массив пикселей изображения
        :param scale: Масштаб волны
        :param offset: Смещение волны
        :return: Массив пикселей нового изображения
        """
        if isinstance(data, np.ndarray):
            new_data = np.zeros(data.shape)
            for x in range(data.shape[0]):
                for y in range(data.shape[1]):
                    new_x = x  # Новый x
                    new_y = int(y + scale * np.sin(2 * np.pi * x / offset))  # Новый y
                    if 0 <= new_x < data.shape[0] and 0 <= new_y < data.shape[1]:
                        new_data[new_x, new_y] = data[x, y]
            return new_data
        else:
            raise ValueError('Входные данные должны представлять собой массив numpy.')

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: Объект изображения
        :return: Объект изображения
        """
        # Преобразуем изображение в массив пикселей
        input_data = np.array(img)

        output_data = self.__create_ripple_effect(input_data, scale=30, offset=30)
        output_image = Image.fromarray(output_data.astype('uint8'))

        return output_image
