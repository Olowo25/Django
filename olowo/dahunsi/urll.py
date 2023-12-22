from django.urls import path
from . import views

urlpatterns = [
    path("/song",views.song, name="layemo"),
    path("/album",views.album, name="lay"),
    path("/addalbum",views.addalbum, name="laye"),
    path("/addalbum/addingalbum",views.addingalbum, name="layem"),
    path("/viewsong",views.viewsong, name="viewsong"),
    path("/albumlist",views.viewalbumlist, name="viewalbum"),
    path("/addsong/",views.addsong, name="da"),
    path('/deletealbum/<int:id>', views.deletealbum, name='delete'),
    path('/updatealbum/<int:id>', views.updatealbum, name='update'),
    path('/deletealbum/deletingalbum/<int:id>', views.deletingalbum, name='deleting'),
    path('/updatealbum/updatingalbum/<int:id>', views.updatingalbum, name='updating'),
    path('/updatesong/updatingsong/<int:id>', views.updatingsong, name='updatingsong'),
    path("/addsong/addingsong",views.addingsong, name="dah"),
    path('/updatesong/<int:id>', views.updatesong, name='updatesong'),

]
