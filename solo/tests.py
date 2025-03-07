from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from .views import MyView

# Create your tests here.


class MyTestcase(TestCase):
    def test_my_view(self):
        factory = RequestFactory()
        request = factory.get(reverse('solo:solo'))
        view = MyView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, 200)

        client = Client()
        response = client.get(reverse('solo:solo'))
        print(response)  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'solo/form.html')
        
        response = client.post(reverse('solo:solo'), data={'field1':'Sagar', 'field2':'Goel'})
        
        print(response)  
        print(response.context)
        print(type(response.context))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'solo/form.html')
        self.assertEqual(response.context['result'],'sagar goel')
        
