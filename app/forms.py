from django.forms import ModelForm
from app.models import Sure


# Create the form class.
class SureForm(ModelForm):
    class Meta:
       model = Sure
       fields = [ 'q01' , 'q02' , 'q03', 'q04' , 'q05', 'q06' , 'q07', 'q08' , 'q09', 'q10' , 
                    'q11', 'q12' , 'q13', 'q14' , 'q15', 'q16' , 'q17', 'q18' , 'q19', 'q20' ,
                    'q21', 'q22' , 'q23', 'q24' , 'q25', 'q26'    
                ]
        