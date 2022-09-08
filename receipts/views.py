from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.
class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)
