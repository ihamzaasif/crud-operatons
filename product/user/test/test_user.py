from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserView(APITestCase):

    fixtures = ['user_data.json']
    
    def setUp(self):
        self.user_id = User.objects.get(pk=1).pk

    def test_get_view(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_view(self):
        response = self.client.post('/user/', {
            "username": "john",
            "first_name": "john",
            "last_name": "doe",
            "email": "john@doe.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 3)

    def test_detail_view(self):
        response = self.client.get('/user/1')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['username'], 'ahmad')
        
        #Test scenario for invalid id
        response = self.client.get('/user/7')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})
        
        #Test scenario for string type
        response = self.client.get('/user/a')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})


    def test_update_view(self):
        response = self.client.put('/user/1', {
            "username": "ahmad_updated",
            "first_name": "ahmad",
            "last_name": "hassan",
            "email": "ahmad@hassan.com"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=1).username, 'ahmad_updated')

        #Test scenario for invalid id
        response = self.client.put('/user/5', {
            "username": "ahmad_updated",
            "first_name": "ahmad",
            "last_name": "hassan",
            "email": "ahmad@hassan.com"
        })
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

        #Test scenario for String type
        response = self.client.put('/user/a', {
            "username": "ahmad_updated",
            "first_name": "ahmad",
            "last_name": "hassan",
            "email": "ahmad@hassan.com"
        })
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

    def test_delete_view(self):
        response = self.client.delete('/user/1')
        self.assertEquals(response.status_code, 204)
        self.assertEquals(User.objects.count(), 1)

        #Test scenario for invalid id
        response = self.client.delete('/user/9')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

        #Test scenario for invalid id
        response = self.client.delete('/user/a')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})