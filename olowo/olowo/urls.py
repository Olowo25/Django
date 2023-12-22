from django.contrib import admin
from django.urls import path,include
from peculiar import views
from mummy import view
from babes import viewss
from lorex import vie



urlpatterns = [
    path('admin/', admin.site.urls),
    path('semi',include('semi.url')),
    path('home',include('precious.url')),
    path('peculiar',views.pecu),
    path('dahunsi',include('dahunsi.urll')),
    path('mummy/pelumi',view.daddy),
    path('mummy/practice',view.practice),
    path('peculiar/mum',views.pecupecu),
    path('babes',viewss.babes),
    path('add',viewss.addbabe),
    path('show',viewss.show, name='index'),
    path('edit/<int:id>', viewss.edit),
    path('update/<int:id>', viewss.update),
    path('delete/<int:id>', viewss.destroy),

    path('', vie.index, name='index'),
    path('signin/', vie.signin, name='signin'),
    path('signout/', vie.signout, name='signout'),
    path('signup/', vie.signup, name='signup'),
    path('profile/', vie.profile, name='profile'),

]
