from app.models import User,Comment
from app import db
import unittest

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.user_Maria = User(username = 'maria',password = 'test', email = 'maria@gg.com')
        self.new_comment = Comment("Nice pitch",pitch_id = 123, user_id=self.user_Maria)
        
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"Nice pitch")
        self.assertEquals(self.new_comment.pitch_id,123)
        self.assertEquals(self.new_comment.user,self.user_Maria)
        
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
    