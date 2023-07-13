from django.test import TestCase, Client
from django.urls import reverse

from djangoTestDemo.objects_posts.models import Object, Post
from djangoTestDemo.objects_posts.forms import PostCreateForm, PostEditForm, ObjectForm


class ObjectModelTest(TestCase):
    def setUp(self):
        self.object = Object.objects.create(
            name='Test Name',
            image='https://example.com/image.jpg',
            width=10,
            height=5,
            weight=2.5
        )

    def test_object_creation(self):
        self.assertEqual(self.object.name, 'Test Name')
        self.assertEqual(self.object.image, 'https://example.com/image.jpg')
        self.assertEqual(self.object.width, 10)
        self.assertEqual(self.object.height, 5)
        self.assertEqual(self.object.weight, 2.5)


class PostModelTest(TestCase):
    def setUp(self):
        self.object = Object.objects.create(
            name='Test Name',
            image='https://example.com/image.jpg',
            width=10,
            height=5,
            weight=2.5
        )
        self.post = Post.objects.create(
            title='Test Post',
            description='This is a test post',
            author_name='John',
            author_phone='1234567890',
            found=False,
            object=self.object
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.description, 'This is a test post')
        self.assertEqual(self.post.author_name, 'John')
        self.assertEqual(self.post.author_phone, '1234567890')
        self.assertFalse(self.post.found)
        self.assertEqual(self.post.object, self.object)


class PostCreateFormTest(TestCase):
    def test_valid_form(self):
        form = PostCreateForm(data={
            'title': 'Test Title',
            'description': 'Test description',
            'author_name': 'John Doe',
            'author_phone': '1234567890'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PostCreateForm(data={})
        self.assertFalse(form.is_valid())


class PostEditFormTest(TestCase):
    def test_valid_form(self):
        form = PostEditForm(data={
            'title': 'Updated Title',
            'description': 'Updated description',
            'author_name': 'Jane Doe',
            'author_phone': '9876543210'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PostEditForm(data={})
        self.assertFalse(form.is_valid())


class ObjectFormTest(TestCase):
    def test_valid_form(self):
        form = ObjectForm(data={
            'name': 'Test Name',
            'image': 'https://example.com/image.jpg',
            'width': 10,
            'height': 5,
            'weight': 2.5
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ObjectForm(data={})
        self.assertFalse(form.is_valid())


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.object = Object.objects.create(
            name='Test Name',
            image='https://example.com/image.jpg',
            width=10,
            height=5,
            weight=2.5
        )
        self.post = Post.objects.create(
            title='Test Post',
            description='This is a test post',
            author_name='John',
            author_phone='1234567890',
            found=False,
            object=self.object
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_edit_view(self):
        response = self.client.get(reverse('edit', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_edit.html')

    def test_delete_view(self):
        response = self.client.get(reverse('delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting redirect

    def test_found_view(self):
        response = self.client.get(reverse('found', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting redirect

    def test_create_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')

        # Test POST request with valid data
        form_data = {
            'title': 'New Post',
            'description': 'This is a new post',
            'author_name': 'Jane',
            'author_phone': '9876543210',
            'name': 'New Object',
            'image': 'https://example.com/new_image.jpg',
            'width': 8,
            'height': 6,
            'weight': 1.5
        }
        response = self.client.post(reverse('create'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Expecting redirect


class FormsTestCase(TestCase):
    def test_post_create_form(self):
        form_data = {
            'title': 'Test Title',
            'description': 'Test description',
            'author_name': 'John Doe',
            'author_phone': '1234567890'
        }
        form = PostCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_edit_form(self):
        form_data = {
            'title': 'Updated Title',
            'description': 'Updated description',
            'author_name': 'Jane Doe',
            'author_phone': '9876543210'
        }
        form = PostEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_object_form(self):
        form_data = {
            'name': 'Test Object',
            'image': 'https://example.com/image.jpg',
            'width': 10,
            'height': 5,
            'weight': 2.5
        }
        form = ObjectForm(data=form_data)
        self.assertTrue(form.is_valid())
