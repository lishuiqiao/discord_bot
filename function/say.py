def Say(message):
    # #say
    content = message.split(" ", 2)

    # say instruction
    if len(content) == 1:
        return "~say <content>"
    else:
        return content[1]