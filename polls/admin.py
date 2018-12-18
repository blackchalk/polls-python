from django.contrib import admin
#Make the poll app modifiable in the admin
from .models import Question, Choice

#admin.site.register(Question)

#Customizing admin form
#You’ll follow this pattern – create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.
# class QuestionAdmin(admin.ModelAdmin):

    # fields = ['pub_date','question_text']

#split the form up into fieldsets:
#     fieldsets = [
#         (None, {'fields':['question_text']}),
#         ('Date Information', {'fields':['pub_date']}),
#     ]

# admin.site.register(Question,QuestionAdmin)

# admin.site.register(Choice)

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)