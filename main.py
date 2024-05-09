from my_coloram import GREEN, RED
import players
import events


def main():
    """Главная исполняемая функция через которую запускается программа."""
    print(f"{GREEN}Добро пожаловать в увлекательную игру! "
          f"Следуйте подсказкам, чтобы начать свое увлекательное путешествие по {RED}ЗАТЕРЯННОМУ МИРУ! \n{GREEN}"
          f"Предлагаем Вам создать уникального персонажа для начала игры.\n")
    print_press_enter()
    print('-' * 33)
    player = players.Player.create_player()  # Создание объекта player
    print(f"\n{GREEN}Теперь твоё путешествие начинается, ты отправляешь в путь, на встречу приключениям...\n")
    events.Event.situation(player, enemy_list=None)  # Запуск цикла событий с переданным объектом player


def print_press_enter():
    """Функция для отображения надписи - нажмите Enter, чтобы продолжить."""
    input(f"{GREEN}Нажмите {RED}ENTER, {GREEN}чтобы продолжить...")
    print()


if __name__ == "__main__":
    main()
