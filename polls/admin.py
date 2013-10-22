# make the poll app modifiable in the admin

from django.contrib import admin
from polls.models import Question, Choice #model table

# Options StackedInline and TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
 
class PollAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text'] --> ordering model table fields

	# splitting the form into fieldsets]
	# You can assign arbitrary HTML classes to each fieldset. Django provides 
	# a "collapse" class that displays a particular fieldset initially collapsed:
	# 
	#fieldsets = [
	# 	(None,				 {'fields': ['question_text']}),
	# 	('Data information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	# ]
	# add choices to the questions change page

	#list display
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'


admin.site.register(Question, PollAdmin)