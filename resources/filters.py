import django_filters
from django import forms
from .models import Standard, Subject,Youtube

class ContentFilter(django_filters.FilterSet):
    standard = django_filters.ModelChoiceFilter(
        queryset=Standard.objects.all(),
        widget=forms.Select(attrs={'placeholder': 'Select Standard'}),
        label='Standard',
        field_name='standard',
        empty_label='--- Select ---',
    )
    subject = django_filters.ModelChoiceFilter(
        queryset=Subject.objects.all(),
        widget=forms.Select(attrs={'placeholder': 'Select Subject'}),
        label='Subject',
        field_name='subject',
        empty_label='--- Select ---',
    )

    class Meta:
        model = Youtube
        fields = ['standard', 'subject']