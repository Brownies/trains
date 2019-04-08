from django.test import TestCase
from .models import Train
from django.contrib.auth.models import User


class InvalidMethodsTest(TestCase):
    def test_index_view(self):
        self.assertEqual(self.client.put("/").status_code, 405)
        self.assertEqual(self.client.delete("/").status_code, 405)
        self.assertEqual(self.client.patch("/").status_code, 405)

    def test_register_view(self):
        self.assertEqual(self.client.put("/").status_code, 405)
        self.assertEqual(self.client.delete("/").status_code, 405)
        self.assertEqual(self.client.patch("/").status_code, 405)

    def test_display_trains_view(self):
        self.assertEqual(self.client.put("/").status_code, 405)
        self.assertEqual(self.client.delete("/").status_code, 405)
        self.assertEqual(self.client.patch("/").status_code, 405)

    def test_insert_trains_view(self):
        self.assertEqual(self.client.put("/").status_code, 405)
        self.assertEqual(self.client.delete("/").status_code, 405)
        self.assertEqual(self.client.patch("/").status_code, 405)


class InsertTrainViewTest(TestCase):
    def test_valid_train(self):
        train = Train(
            id=1,
            name="test_train",
            destination="test_destination",
            speed=5,
            latitude=6,
            longitude=7
        )

        train_json = {
            "name": "test_train",
            "destination": "test_destination",
            "speed": 5,
            "coordinates": [6, 7]
        }
        response = self.client.put(
            "/trains/1/location/",
            data=train_json,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "OK")

        train_from_db = Train.objects.all()[0]
        self.assertEqual(train_from_db.id, train.id)
        self.assertEqual(train_from_db.name, train.name)

    def test_invalid_train(self):
        train_json = {}
        response = self.client.put(
            "/trains/1/location/",
            data=train_json,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)


class ViewTrainViewTest(TestCase):
    def test_train_view(self):
        train = Train(
            id=1,
            name="test_train",
            destination="test_destination",
            speed=5,
            latitude=6,
            longitude=7
        )
        train.save()
        u = User.objects.create(username="user", password="pass")
        u.set_password("pass")
        u.save()
        c = self.client
        c.login(username="user", password="pass")

        response = c.get("/trains/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Trains</title>")
        self.assertContains(response, "<td>1</td>")


class IntegrationTest(TestCase):
    def test_register_login_insert_view(self):
        c = self.client
        response = c.post("/register/", {
            'username': 'user',
            'password1': 'Complex_555_Password',
            'password2': 'Complex_555_Password'
        })
        self.assertEquals(response.status_code, 200)

        response = c.post("/login/", {
            'username': 'user',
            'password': 'Complex_555_Password'
        })
        self.assertEquals(response.status_code, 302)  # redirect to front page

        train_json = {
            "name": "test_train",
            "destination": "test_destination",
            "speed": 5,
            "coordinates": [6, 7]
        }
        response = self.client.put(
            "/trains/1/location/",
            data=train_json,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

        response = c.get("/trains/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Trains</title>")
        self.assertContains(response, "<td>1</td>")
