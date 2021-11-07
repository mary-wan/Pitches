from app.models import Pitch,User
from app import db

def setUp(self):
    self.user_Maria = User(username = 'maria',password = 'test', email = 'maria@gg.com')
    self.new_pitch = Pitch(title="Money",post= "Advertise good products",category="Product",user = self.user_Maria )
        
def tearDown(self):
    Pitch.query.delete()
    User.query.delete()
        
def test_check_instance_variables(self):
    self.assertEquals(self.new_pitch.title,"Money")
    self.assertEquals(self.new_pitch.post,"Advertise good products")
    self.assertEquals(self.new_pitch.category,"Product")
    self.assertEquals(self.new_pitch.user,self.user_Maria)
    
def test_save_pitch(self):
    self.new_pitch.save_review()
    self.assertTrue(len(Pitch.query.all())>0)
    