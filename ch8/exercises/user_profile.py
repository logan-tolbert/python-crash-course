def build_profile(first, last, **user_info):
    """Build a dictionary containg everything we know about a user."""
    user_info['first_name'] = first 
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
                            'Logan',
                            'Tolbert',
                             age=35,
                             location='Birmingham, AL',
                             occupation='unemployed',
                             interest1='guitar',
                             interest2='video games'
                             )

print(user_profile)

