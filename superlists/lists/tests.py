from django.test import TestCase

from superlists.lists.models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    """Test model for to-do items."""

    def save_item(self, item_text):
        item = Item()
        item.text = item_text
        item.save()
        return item
    
    def test_saving_and_retrieving_items(self):
        first_item = self.save_item('The first (ever) listed item')
        second_item = self.save_item('Item the second')

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item, first_item)
        self.assertEqual(second_saved_item, second_item)
