from django import forms




class AddForm(forms.Form):


	title = forms.CharField(max_length=200)
	# pic = forms.CharField()
	pic = forms.ImageField(label="Upload Image")