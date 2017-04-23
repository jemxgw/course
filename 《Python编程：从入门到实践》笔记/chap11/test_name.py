# test_name_function.py
import unittest
from name_funciton import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py """
    """用于测试的类名最好让它看起来与要测试的函数相关"""
    """每个用于测试的方法名必须以test_打头"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""

        formatted_name = get_formatted_name(first='janis', last='joplin')
        self.assertEqual('Janis Joplin', formatted_name)

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""

        formatted_name = get_formatted_name(
            first='wolfgang', middle='amadeus', last='mozart')
        self.assertEqual('Wolfgang Amadeus Mozart', formatted_name)

unittest.main()
