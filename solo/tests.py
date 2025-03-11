from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from .views import MyView
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your tests here.


class MyTestcase(TestCase):
    def test_my_view(self):
        '''
        Testing the solo view via sending request using RequesTFactory.
        This will not work for LoginRequired views
        '''
        # factory = RequestFactory()
        # request = factory.get(reverse('solo:solo'))
        # view = MyView.as_view()

        # response = view(request)
        # self.assertEqual(response.status_code, 200)

        '''
        Testing the solo view via sending request via Client.
        This will not work for LoginRequired views
        # client = Client()

        or we can use self.client as it available from parent TestCase class
        '''
        # response = self.client.get(reverse('solo:solo'))
        # print(response)
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'solo/form.html')

        # response = self.client.post(reverse('solo:solo'), data={
        #                        'field1': 'Sagar', 'field2': 'Goel'})

        # print(response)
        # print(response.context)
        # print(type(response.context))
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'solo/form.html')
        # self.assertEqual(response.context['result'], 'sagar goel')

        '''
        For view that require Login, we need to simulate a login or do login programmatically
        using login function
        '''
        test_user1 = User.objects.create_user(
            username='test1', password='test1')
        # self.client.force_login(test_user1) this will also work
        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('solo:solo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'solo/form.html')

        response = self.client.post(reverse('solo:solo'), data={
            'field1': 'Sagar', 'field2': 'Goel'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'solo/form.html')
        self.assertEqual(response.context['result'], 'sagar goel')
