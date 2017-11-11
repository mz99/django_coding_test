from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll

class Command(BaseCommand):
    def do_something(model_name)
    model_name.each do |m|
      puts "{
        model_name.question + ":" + model_name.question_value,
        model_name.votes + ":" + model_name.votes_value,
        model_name.yes_no + ":" + model_name.yes_no_value
      }"
