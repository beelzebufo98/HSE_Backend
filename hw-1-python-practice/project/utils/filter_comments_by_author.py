def filter_comments_by_author(comments, author):
    comment = []
    for i in comments:
        if i.author_id == author.id:
            comment.append(i)
    return comment
