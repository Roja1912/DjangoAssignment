from rest_framework.views import APIView
from .models import User, ActivityPeriod
from rest_framework.response import Response
import datetime


class GetUsers(APIView):
    """
    Class to get the users data from database
    """
    def get(self, request, *args, **kwargs):
        result = dict()
        result["ok"] = True
        members = []
        user_object = User.objects.all()
        for each_user_object in user_object:
            each_user_dict = dict()
            each_user_dict["id"] = each_user_object.userid
            each_user_dict["real_name"] = each_user_object.realname
            each_user_dict["tz"] = each_user_object.tz

            activity_period_object = ActivityPeriod.objects.filter(user=each_user_object)
            activity_period_object_list = []
            for each_activity_period_object in activity_period_object:
                activity_period_object_dict = dict()
                start_time = each_activity_period_object.start_time
                conv_start_time = datetime.datetime.strptime(str(start_time), "%Y-%m-%d %H:%M:%S%z").strftime("%b %d %Y %H:%M%p")
                activity_period_object_dict["start_time"] = conv_start_time
                end_time = each_activity_period_object.end_time
                conv_end_time = datetime.datetime.strptime(str(end_time), "%Y-%m-%d %H:%M:%S%z").strftime("%b %d %Y %H:%M%p")
                activity_period_object_dict["end_time"] = conv_end_time
                activity_period_object_list.append(activity_period_object_dict)
            each_user_dict["activity_periods"] = activity_period_object_list
            members.append(each_user_dict)
            result["members"] = members
        return Response(result)

