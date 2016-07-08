def log(to_log):
    print(">> " + to_log)


def log_title_upper_case(to_log):

    text_size = len(to_log)

    title = "{0}   {1}   {2}".format(build_str_hashtag(text_size / 2 + 2),
                                     to_log.upper(),
                                     build_str_hashtag(text_size / 2 + 2))

    print("\n")
    print(build_str_hashtag(len(title)))
    print(title)
    print(build_str_hashtag(len(title)))


def build_str_hashtag(size):
    size = int(size)

    hashtag_str = ""

    for index in range(size):
        hashtag_str = hashtag_str + "#"

    return hashtag_str
