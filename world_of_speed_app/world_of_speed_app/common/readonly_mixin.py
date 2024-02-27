class ReadonlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        
        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            
        return form