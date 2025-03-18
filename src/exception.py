# Class exeption


class ShellScript(Exception):
    """Общий класс исключений"""

    def __init__(self, *args, **kwargs):
        if args:
            self.message = args[0]
        else:
            self.message = "Неизвестная ошибка скрипта."
