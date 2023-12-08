from random import randint

from PIL import Image
from config import ConfigVariables
from utils import save_image
import os


def main():
    filter_dict = ConfigVariables.image_filters.value
    is_finished = False

    print("Добро пожаловать в консольный фоторедактор.")

    while not is_finished:
        # Спрашиваем путь к файлу
        image_path = input('\nВведите путь к файлу: ')

        # Проверяем ввод на корректность
        while not os.path.exists(image_path):
            image_path = input('Файл не найден! Введите путь заново: ')

        img = Image.open(image_path).convert("RGB")

        # Выводим меню редактора
        print("\nМеню фильтров:")
        for i in range(1, len(filter_dict)):
            print(f"{i}: {filter_dict[i]['name']}")
        print("0: Выход\n")

        choice = input("Выберите фильтр (или 0 для выхода): ")

        # Проверяем выбор фильтра на корректность
        while choice not in map(str, range(len(filter_dict))):
            choice = input('Некорректный ввод! Выбери фильтр заново: ')

        # Выбираем фильтр
        img_filter = filter_dict[int(choice)]['class']

        # Если фильтр None, то это значит, что пользователь ввел Выход
        if img_filter is None:
            print("\nДо свидания!")
            exit(0)

        # Выводим название и описание фильтра
        print(
            f"\n{filter_dict[int(choice)]['name']}:\n"
            f"{filter_dict[int(choice)]['description']}\n"
        )

        is_agree = input('Применить фильтр к картинке? (Да/Нет): ')

        # Проверяем корректность ввода
        while is_agree.lower() not in ConfigVariables.correct_inputs.value:
            is_agree = input('Некорректный ввод! Применить фильтр к картинке? (Да/Нет): ')

        if is_agree.lower() in ConfigVariables.agree_inputs.value:
            path_to_save = input('\nКуда сохранить: ')

            # Проверяем расширение файла на корректность
            while not save_image(img, img_filter, path_to_save):
                path_to_save = input('Неверное расширение файла! Введи куда сохранить заново: ')

            is_repeat = input('\nЕщё раз? (Да/Нет): ')

            # Проверяем корректность ввода
            while is_repeat.lower() not in ConfigVariables.correct_inputs.value:
                is_repeat = input('Ещё раз? (Да/Нет): ')

            if is_repeat.lower() in ConfigVariables.disagree_inputs.value:
                print("\nДо свидания!")
                exit(0)


if __name__ == '__main__':
    main()
