from rest_framework import serializers
from playground.models import Questions

class QuestionsSerailizer( serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields= ('QuestionId', 'Title', 'OptionA', 'OptionB', 'OptionC', 'OptionD', 'Answer' )
        