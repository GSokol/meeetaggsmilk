from django.forms import ModelForm

from main.models.supply import Supply

class SupplyForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(SupplyForm, self).__init__(*args, **kwargs)
    instance = getattr(self, 'instance')
    if instance and not (instance.status == instance.NEW):
      self.fields['supplyDate'].widget.attrs['readonly'] = True
 
  def clean_supplydate(self):
    instance = getattr(self, 'instance')
    if instance and not (instance.status == instance.NEW):
      return instance.supplyDate
    else:
      return self.cleaned_data['supplyDate']
 
  class Meta:
    model = Supply
    fields = ['supplyDate', 'partnerGoods']

