import unittest
from models import sources

Source=sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test class to test the behavior of our souce class

    '''
    def setUp(self):
        '''
        setUp method that is run before every test
        '''
        self.new_source=Source('1234','KBC','broadcasting','www.kbc.co.ke','general','Kenya')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
if __name__ == '__main__':
    unittest.main()