from ...models import User, ActivityPeriod
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Class to load dumpy data into database
    """
    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return: success messgae
        """
        users = [{"userid": "DW012A3CDE", "realname": "David Tom", "tz": "America/Los_Angeles",
                  "activity_periods": [
                    {
                        "start_time": "2020-02-1 12:45:00",
                        "end_time": "2020-07-21 1:45:00"
                    },
                    {
                        "start_time": "2020-03-21 11:45:00",
                        "end_time": "2020-03-24 12:45:00"
                    },
                    {
                        "start_time": "2020-03-21 1:45:00",
                        "end_time": "2020-07-21 12:45:00"
                    }
			      ]},
                {"userid": "W07QCRPA4", "realname": "Nick Jacks", "tz": "Asia/Kolkata",
                 "activity_periods": [
                     {
                         "start_time": "2020-03-1 4:45:00",
                         "end_time": "2020-07-21 1:45:00"
                     },
                     {
                         "start_time": "2020-04-21 7:45:00",
                         "end_time": "2020-06-24 12:45:00"
                     },
                     {
                         "start_time": "2020-03-21 5:45:00",
                         "end_time": "2020-08-21 12:45:00"
                     }
                 ]}
            ]
        for each_user in users:
            user_object = User.objects.create(userid=each_user['userid'], realname=each_user['realname'], tz=each_user['tz'])
            for each_activityperiod in each_user["activity_periods"]:
                ActivityPeriod.objects.create(user=user_object, start_time=each_activityperiod['start_time'], end_time=each_activityperiod['end_time'])
        return "Users data loded Succesfully"


