from django import forms


class RedirectForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(RedirectForm, self).clean()

        # Either url or external url must be populated.
        if not cleaned_data.get('url') and not cleaned_data.get('external_url'):
            raise forms.ValidationError("""Please specify either a URL *or* an external URL.""")

        # Do not allow both a parent and an external URL to be specified.
        if cleaned_data.get('parent') and cleaned_data.get('external_url'):
            raise forms.ValidationError("""Please choose either a parent *or* specify an external URL, but not both.
                                        Thanks.""")

        # Do not allow both a url and an external URL to be specified.
        if cleaned_data.get('url') and cleaned_data.get('external_url'):
            raise forms.ValidationError("""Please choose either a url *or* specify an external URL, but not both.
                                        Thanks.""")

        return cleaned_data
