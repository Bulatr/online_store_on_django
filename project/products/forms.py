from django import forms

class SortForm(forms.Form):
    sort_by = forms.ChoiceField(
        choices=(
            ('name', 'Default sorting'),
            ('popularity', 'Sort by popularity'),
            ('rating', 'Sort by average rating'),
            ('date', 'Sort by newness'),
            ('price', 'Sort by price: low to high'),
            ('price-desc', 'Sort by price: high to low'),
        ),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id' : 'sort_by',
            'onchange': 'handleSortChange(this)',  # Добавляем onchange
        })
    )

class PriceForm(forms.Form):
    price_range = forms.ChoiceField(
        choices=(
            ('0-500', '0 - 500'),
            ('501-900', '501 - 900'),
            ('901-5000', '901 - 5000'),
            ('5001-10000', '5001 - 10000'),
        ),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'price_range',
            'onchange': 'handlePriceChange(this)',  # Добавляем onchange
        })
    )
