from django.shortcuts import render
from wishlist.models import WishlistItem

def show_wishlist(request):
  wishlist_item_data = WishlistItem.objects.all()
  context = {
    'item_list': wishlist_item_data,
    'name': 'Kak Daniel',
  }
  # for item in wishlist_item_data:
  #   print(">>", item.name)
  return render(request, 'wishlist.html', context)
