import unittest
from LANVote import LANVote

class LANVoteTest(unittest.TestCase):
   """docstring for LANVoteTest"""
   def setUp(self):
      self.lanvote = LANVote(hostname = "www.iarchis.com", port = 80, timeout = 10)

   def test_add_params(self):
      self.lanvote.add_params('1','xxx')
      self.assertEqual({'1':'xxx'}, self.lanvote.params)

   def test_sendrequest(self):
   	self.assertEqual(1,1)

   def test_httpconnection(self):
   	self.assertIsNotNone(self.lanvote.httpClientConnection)
     


if __name__ == '__main__':
   unittest.main()