# Creating custom filter

from django import template
import random
import re

register = template.Library()

@register.filter
def randomizeAnswers(correctAns, incorrectAns):
    incorrectAns = re.findall('[\w|\d]+[A-Za-z\s0-9-.]*', incorrectAns)
    correctAns = re.findall('[A-Za-z\s.-]+', correctAns)
    ans_list = list(incorrectAns)
    ans_list.extend(correctAns)
    return ans_list

@register.filter
def to_char(val):
    return chr(96+val)