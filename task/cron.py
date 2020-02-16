from .models import  Repeated
from  .models import  Task
import datetime


def create_task(repeated):
    now = datetime.datetime.now()
    end_hours = datetime.timedelta(hours=repeated.duration)
    end_date = str(now+end_hours)
    rep = Repeated.objects.get(id=repeated.id)
    task = Task.objects.create(
        name=repeated.name,
        accountant=repeated.accountant,
        client=repeated.client,
        company=repeated.company,
        status="approved",
        title=repeated.title,
        text=repeated.text,
        repeated=rep,
        is_repeated=True,
        end_date = end_date,
        manager=repeated.manager,
    )

    return  True

def my_scheduled_job():
    print("Today's date:", datetime.date.today())
    print("weekday",datetime.datetime.today().weekday())
    print("year", datetime.datetime.today().timetuple().tm_yday)

    weekday = datetime.datetime.today().weekday()
    year =  datetime.datetime.today().timetuple().tm_yday
    mount_day = datetime.datetime.today().timetuple().tm_mday
    # print("year",datetime.datetime.timetuple().tm_mday)
    print('-----+++++++++++-------')
    repeated = Repeated.objects.filter(is_active=True)
    for rep in repeated:

        print(rep.repeated_value ,'====',weekday,'----',rep.repeated_type)
        print(rep.repeated_value ,'====',year,'----',rep.repeated_type)

        if rep.repeated_type == 1:
            print('active day')
            create_task(rep)
            #sarqel
        elif rep.repeated_type == 2 and  rep.repeated_value == weekday :
            create_task(rep)

            print('active weekday')
        elif rep.repeated_type == 3 and rep.repeated_value == mount_day:
            create_task(rep)
            print('active year')

        elif rep.repeated_type == 4 and  rep.repeated_value == year:
            create_task(rep)
            print('active year')
        else :
            print('not found')
        print(rep.repeated_type,'*****')
        print(rep.repeated_value,'******')

    print(repeated,'******')


