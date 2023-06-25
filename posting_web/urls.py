from django.urls import path
from posting_web import views

urlpatterns = [

    path('', views.home, name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/rate/', views.RatingCreateView.as_view(), name='rating_create'),
    path('products/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
]
