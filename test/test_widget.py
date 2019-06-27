from unittest import TestCase, main

from proj.main import Widget


class WidgetTestCase(TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget = None

    def test_size(self):
        self.assertEqual(self.widget.get_size(), (40, 40))

    def test_Resize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.get_size(), (100, 100))


if __name__ == '__main__':
    main()
