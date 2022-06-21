from django.shortcuts import render
from django.utils import timezone

class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return 'hello'


def test(request):
    people = ['Amy', 'Josh', 'Tobey', 'Josh']
    person = Person('Amy')
    person_list = []
    now = timezone.now()
    past_dt = timezone.datetime(1971,8,22,0,0)
    criteria_dt = timezone.datetime(2001,3,19,0,0)
    future_dt = timezone.datetime(2037,1,1,0,0)

    value ='''
        Miracles happen to only those who believe in them.
        Think like a man of action and act like man of thought.
        Courage is very important. Like a muscle, it is strengthened by use.
        Life is the art of drawing sufficient conclusions from insufficient premises.
        By doubting we come at the truth.
        A man that has no virtue in himself, ever envies virtue in others.
        When money speaks, the truth keeps silent.
        Better the last smile than the first laughter.
    '''
    
    value1 = 'Joel is a slug'
    value2 = '<p>Joel is a slug</p>'
    value3 = "https://www.example.org/foo?a=b&c=d"
    value4 = "Check out www.djangoproject.com"
    value5 = "Send questions to foo@example.com"
    value6 = '<b>Joel</b> \n is a slug'

    return render(request, 'mytest/test.html', {'people':people, 'person':person, 
                                                'person_list':person_list, 
                                                'datetime_obj':now, 'past_dt':past_dt, 
                                                'criteria_dt':criteria_dt, 'future_dt':future_dt,
                                                'value':value, 'value1':value1, 
                                                'value2':value2, 'value3':value3, 
                                                'value4':value4, 'value5':value5, 'value6':value6})
