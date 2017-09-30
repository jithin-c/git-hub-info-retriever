from django import forms


class UserSearchForm(forms.Form):
    email = forms.EmailField(required=False)
    login = forms.CharField(required=False)
    fullname = forms.CharField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data:
            raise forms.ValidationError("Enter atleast one field value ( email | login | fullname)")

        is_empty = False
        for key, val in cleaned_data.iteritems():
            if val:
                is_empty = is_empty | True

        if not is_empty:
            raise forms.ValidationError("Enter atleast one field value ( email | login | fullname)")

        return cleaned_data