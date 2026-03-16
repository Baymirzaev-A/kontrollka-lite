from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class BaseScript(ABC):
    """Базовый класс для всех скриптов"""

    def __init__(self):
        self.name = self.get_name()
        self.description = self.get_description()

    @abstractmethod
    def get_name(self):
        """Возвращает название скрипта"""
        pass

    @abstractmethod
    def get_description(self):
        """Возвращает описание скрипта"""
        pass

    @abstractmethod
    def execute(self, connection, device_info):
        """
        Выполняет скрипт на подключенном устройстве
        connection - активное подключение netmiko
        device_info - информация об устройстве (dict)
        """
        pass

    def pre_check(self, connection, device_info):
        """
        Проверка перед выполнением (опционально)
        Должна вернуть (success, message)
        """
        return True, "OK"

    def post_check(self, connection, device_info):
        """
        Проверка после выполнения (опционально)
        Должна вернуть (success, message)
        """
        return True, "OK"