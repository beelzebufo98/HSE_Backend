def select_top_users_by_rate(users, top_size):
    users = sorted(users, key=lambda u: u.rate, reverse=True)
    return users[:top_size]
