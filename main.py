import argparse
from apiWrapper import api
from databaseManager import activityManager


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', choices=['new', 'list'])
    parser.add_argument('--type')
    parser.add_argument('--participants', type=int)
    parser.add_argument('--price_min', type=float)
    parser.add_argument('--price_max', type=float)
    parser.add_argument('--accessibility_min', type=float)
    parser.add_argument('--accessibility_max', type=float)

    args = parser.parse_args()

    if args.command == 'new':
        api_obj = api.Api(args.type, args.participants, args.price_min, args.price_max, args.accessibility_min,
                          args.accessibility_min)
        response = api_obj.random_activity()
        # print(response)
        try:
            activity = response['activity']
            print(activity)
        except: print("Error, No activity found with the specified parameters")

        if activity:
            db = activityManager.ActivityManager('./databases/activities.sqlite')
            db.add_activity(activity)
            db.close()
        else:
            print("Error, Check your input")

    if args.command == 'list':
        db = activityManager.ActivityManager('./databases/activities.sqlite')
        activities_list = db.get_last_activities()
        for act in activities_list[:5]:
            print(act)
        db.close()


if __name__ == '__main__':
    main()

