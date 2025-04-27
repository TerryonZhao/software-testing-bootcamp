# 用unittest+mock写测试：
    # 模拟服务器返回温度25°C，验证返回值正确
    # 模拟服务器返回错误（比如500），验证抛出异常
    
import unittest
from unittest.mock import patch
from WeatherService import WeatherService

class test_WeatherService(unittest.TestCase):
    def setUp(self):
        print('Begin')
        self.weather_service = WeatherService()
        
    def tearDown(self):
        print('Over')
    
    def test_get_temperature_success(self):
        with patch('WeatherService.requests.get') as mock_get:
            response = mock_get.return_value
            response.status_code = 200
            response.json.return_value = {"temperature": 25}
            temperature = self.weather_service.get_temperature()
            self.assertEqual(temperature, 25)
            
            response.status_code = 500
            with self.assertRaises(Exception):
                self.weather_service.get_temperature()
            

if __name__ == '__main__':
    unittest.main()