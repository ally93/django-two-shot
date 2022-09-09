from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from receipts.models import Receipt, ExpenseCategory, Account

# Create your views here.
class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.purchaser = self.request.user
        item.save()
        return redirect("home")


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "expense_category/list.html"

    def get_queryset(self):
        # print(ExpenseCategory.objects.all)
        return ExpenseCategory.objects.filter(owner=self.request.user)


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"

    def get_queryset(self):
        # print(ExpenseCategory.objects.all)
        return Account.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "expense_category/create.html"
    fields = ["name"]

    def form_valid(self, form):
        expense_category = form.save(commit=False)
        expense_category.owner = self.request.user
        expense_category.save()
        return redirect("list_categories")


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/create.html"
    fields = ["name", "number"]

    def form_valid(self, form):
        expense_category = form.save(commit=False)
        expense_category.owner = self.request.user
        expense_category.save()
        return redirect("list_account")
