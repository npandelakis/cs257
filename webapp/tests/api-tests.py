'''
    api-tests.py
    Written by Grace de Benedetti and Nick Pandelakis
    19 Feb 2021
'''

from terrorism_api import app
import unittest
import responses

class ApiTester(unittest.TestCase):

    ##### Setup #####

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()


    def tearDown(self):
        pass

    ##### Tests #####

    def test_world(self):
        response = self.app.get_json('/world')
        self.assertEqual(responses.world, response)

    def test_real_country(self):
        response = self.app.get_json('/Germany')
        self.assertEqual(responses.country, response)

    def test_real_country_years_filter(self):
        response = self.app.get_json('/Germany?start_year=1990&end_year=2001')
        self.assertEqual(responses.country_years_filter, response)

    def test_non_country(self):
        response = self.app.get_json('/notreal')
        self.assertEqual([],response)

    def test_real_provstate(self):
        response = self.app.get_json('/Wisconsin')
        self.assertEqual(responses.provstate, response)

    def test_real_provstate_years_filter(self):
        response = self.app.get_json('/Wisconsin?start_year=1990&end_year=2001')
        self.assertEqual(responses.country_years_filter, response)

    def test_non_provstate(self):
        response = self.app.get_json('/nonvince')
        self.assertEqual([], response)
        
    def test_attack(self):
        response = self.app.get_json('/197001210001')
        self.assertEqual(responses.attack, response)
        
    def test_search(self):
        response = self.app.get_json('/areas/name_contains/wis')
        self.assertEqual(responses.search, response)

    def test_provstate_year(self):
        response = self.app.get_json('/Wisconsin/1990')
        self.assertEqual(responses.provstate_year, response)

    def test_country_year(self):
        response = self.app.get_json('/Germany/1990')
        self.assertEqual(responses.country_year, response)


if __name__=='__main__':
    unittest.main()



