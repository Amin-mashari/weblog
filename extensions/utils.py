from . import jalali
from django.utils import timezone

def persian_numbers_converter(mystr):

     numbers = {
          "0":"۰",
          "1":"۱",
          "2":"۲",
          "3":"۳",
          "4":"۴",
          "5":"۵",
          "6":"۶",
          "7":"۷",
          "8":"۸",
          "9":"۹"
     }

     for english, persian in numbers.items():
          mystr = mystr.replace(english, persian)

     return mystr


def jalali_convertor(time):
     jmonth =["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]

     time = timezone.localtime(time)

     time_to_str = "{},{},{}".format(time.year , time.month, time.day, time.hour, time.minute,time.day)
     time_to_list = list(jalali.Gregorian(time_to_str).persian_tuple())
     
     for index , month in enumerate(jmonth):
          if time_to_list[1] == index + 1:
               time_to_list[1] = month
               break

     output = "{} {} {}, ساعت {}:{}".format(
          time_to_list[2],#year
          time_to_list[1],#month
          time_to_list[0],#day
          time.hour,
          time.minute,
     )
     return persian_numbers_converter(output)