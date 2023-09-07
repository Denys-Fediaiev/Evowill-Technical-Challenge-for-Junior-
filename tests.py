import unittest
from apiWrapper import api
from databaseManager import activityManager


class TestClass(unittest.TestCase):

    def test_random_activity_not_error(self):
        api_obj = api.Api('education', 1, 0.1, 30, 0.1, 0.5)
        self.assertNotEqual(api_obj.random_activity(), {'error': 'No activity found with the specified parameters'}, 'No activity found with the specified parameters')

    def test_add_to_db(self):
        db = activityManager.ActivityManager('test.slite')
        db.add_activity('Learn Python')
        self.assertEqual(db.get_last_activities(), [(1, 'Learn Python')], )


# class TestDB(unittest.TestCase):
#
#     def test_add(self):
#         db = activityManager.ActivityManager()
#         db.add_activity('Learn Python')
#         self.assertEqual(db.get_last_activities(), "(1, 'Learn Python')", )


if __name__ == '__main__':
    unittest.main()
