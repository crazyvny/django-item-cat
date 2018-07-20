from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from .models import MenuItem 
import ipdb
# from .forms import PostForm
# Create your views here.
def index(request):
    # import ipdb
    # ipdb.set_trace()
    res = Restaurant.objects.all()
    return render(request, 'restaurants.html', {'restaurants': res})

# def index(home/admin/):
#     return render(request, 'restaurants.html', {'restuarants': res})

def menu(request,id):
    # ipdb.set_trace()
    res = MenuItem.objects.get(pk=id)

    return render(request, 'menu.html', {'menu': res,'id':id})


def edit(request,id):
    return render(request, 'editRestaurant.html')

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
'''class AddRestaurant(TemplateView):
    template_name = 'editRestaurant.html'

    def get(self, request):
        form = EditForm()
        return render(request,self.template_name, {'form':form} )'''
