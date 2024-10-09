from django import forms

from .models import Strategy

class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = ['margin', 'takeProfit', 'stopLoss']


class StyledFrom(forms.Form):
    margin = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6', 'placeholder': '10000'}),
        label="Margin"
    )
    takeProfit = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6', 'placeholder': '50'}),
        label="Takeprofit"
    )
    stopLoss = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6', 'placeholder': '50'}),
        label="Stoploss"
    )
