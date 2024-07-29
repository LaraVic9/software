
import pytest
import json
from flask import Flask
from flask_testing import TestCase
from countries_api import app, get_country_name_rest  # Ajuste conforme a sua estrutura

class TestCountriesAPI(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_country_name_success(self):
        response = self.client.get('/get_country_name?iso_code=US')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['country_name'], 'United States')

    #Erro
    def test_get_country_name_erro(self):
        response = self.client.get('/get_country_name?iso_code=ZZ')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Country not found')

    def test_get_country_name_missing_iso_code(self):
        response = self.client.get('/get_country_name')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'ISO code not provided')

    def test_get_country_name_rest_success(self):
        with self.mock_requests_get('https://restcountries.com/v3.1/alpha/br', json={"name": {"common": "Brazil"}}):
            result = get_country_name_rest()
            self.assertEqual(result, 'Brazil')
