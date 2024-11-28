def get_ordered_comments_by_likes(comments):
    return sorted(comments, key=lambda c: c.like_count, reverse=True)
