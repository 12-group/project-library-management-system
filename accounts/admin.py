from django.contrib import admin

# Register your models here.

from .models import *
admin.site.enable_nav_sidebar = False
admin.site.register(Customer)
admin.site.register(Reader)
admin.site.register(Staff)

admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(BorrowOrder)
admin.site.register(BorrowBook)
admin.site.register(ReturnBook)

admin.site.register(FineReceipt)
admin.site.register(PenaltyTicket)
admin.site.register(BookLiquidation)
