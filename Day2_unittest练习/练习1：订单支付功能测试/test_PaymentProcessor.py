# 用unittest写测试：
    # 测试正常充值和余额增加
    # 测试充值负数金额时报错
    # 测试余额不足支付时报错
    # 测试支付成功后余额正确减少
    
# TestPaymentProcessor (继承TestCase)
# ├── self (测试对象本身)
# │   ├── self.processor (PaymentProcessor实例)
# │   │   └── self.processor.balance (int型余额数据)
# │   └── self.assertEqual() 等各种断言方法 (从TestCase继承而来)

import unittest
from PaymentProcessor import PaymentProcessor

class Test_PaymentProcessor(unittest.TestCase):
    def setUp(self):
        print('Begin')
        self.account = PaymentProcessor()
        self.account.add_funds(50)

    def tearDown(self):
        print('Over')

    def test_add_funds(self):
        self.assertEqual(self.account.balance, 50)

        with self.assertRaises(ValueError):
            self.account.add_funds(-10)

    def test_pay(self):
        self.account.pay(10)
        self.assertEqual(self.account.balance, 40)

        with self.assertRaises(Exception):
            self.account.pay(100)

        with self.assertRaises(ValueError):
            self.account.pay(-10)

if __name__ == '__main__':
    unittest.main()
    

