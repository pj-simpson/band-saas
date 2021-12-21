from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "table_header_color": TextInput(attrs={"type": "color"}),
        }
