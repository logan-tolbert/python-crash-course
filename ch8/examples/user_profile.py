# pg.148
def build_profile(first, last, **user_info):
    """Build a dictionary containg everything we know about a user."""
    user_info['first_name'] = first 
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='phyics')

print(user_profile)

