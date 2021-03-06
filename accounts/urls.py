from django.urls import path

from . import views

urlpatterns = [
   path('', views.home,name='home'),
   path('search/', views.search_book,name='search'),
   path('detail_info/<str:pk>/', views.detail_info_book,name='detail'),
   path('cart/', views.cart,name='cart'),
   path('remove_from_cart/<str:cart_pk>/', views.remove_from_cart,name='remove_from_cart'),

   path('login/', views.loginPage,name='login'),
   path('register/', views.register,name='register'),
   path('logout/', views.logoutUser, name='logout'),
   path('password_change/', views.password_change,name='password_change'),
   path('password_change_done/', views.password_change_done,name='password_change_done'),
   path('account/', views.accountSettings, name='account'),
   path('dashboard/', views.dashboard, name='dashboard'),

   
   path('librarian/', views.librarian_home, name="librarian"), 
   path('borrowers/', views.borrowers, name="borrowers"),
   path('register_reader/', views.register_reader, name="register_reader"),
   path('remove_reader/<str:reader_pk>/', views.remove_reader, name="remove_reader"),
   path('update_reader/<str:reader_pk>/', views.update_reader, name="update_reader"),
   path('request_onl_list/', views.request_onl_list, name="request_onl_list"),
   path('request_onl/<str:pk>/', views.request_onl, name="request_onl"),
   path('update_request/<str:pk>/', views.update_request, name="update_request"),
   path('borrow_detail/<str:pk>/', views.borrow_detail, name="borrow_detail"),
   path('request_off/', views.request_off, name="request_off"),
   path('return_book/<str:pk>/', views.return_book, name="return_book"),
   path('penalty_ticket/', views.penalty_ticket, name="penalty_ticket"),
   path('reader_borrow_detail/',views.reader_borrow_detail, name="reader_borrow_detail"),

   path('manager/manager_dashboard/', views.manager_dashboard, name="manager_dashboard"),
   path('manager/add_staff/', views.add_staff, name="add_staff"),
   path('manager/delete_staff/<str:sId>', views.delete_staff, name="delete_staff"),


   path('storekeeper/list_book/', views.list_book, name="list_book"),
   path('storekeeper/thanh_ly/', views.thanh_ly, name="thanh_ly"),
   path('storekeeper/liquidation_info/<str:bId>/', views.liquidation_info, name="liquidation_info"),
   path('storekeeper/add_book/', views.add_book, name="add_book"),
   path('storekeeper/liquidation_history/', views.liquidation_history, name="liquidation_history"),


   path('receipt_list/', views.receipt_list, name="receipt_list"),
   path('add_receipt/', views.add_receipt, name="add_receipt"),
   path('remove_receipt/<str:receipt_pk>/', views.remove_receipt, name="remove_receipt"),
   path('return_book_history/', views.return_book_history, name="return_book_history"),

]  