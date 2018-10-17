import random


def get_r_list(user_id, user_count):
    a = []
    while True:
        choice = random.randint(1, user_count)
        if choice == user_id:
            pass
        elif choice in a:
            pass
        else:
            a.append(choice)
        if len(a) == 5:
            break
    return a


def get_variation(user_id):
    u_sex = UserInfo.objects.get(user_id=user_id)
    a = [user_id]
    l_f_s = UserInfo.objects.filter(sex=u_sex.sex).values('user_id')
    list_of_users = []
    for i in l_f_s:
        list_of_users.append(i['id'])
    while True:
        var = random.choice(list_of_users)
        if var in a:
            pass
        else:
            a.append(var)
        if len(a) == 4:
            break
    return a

