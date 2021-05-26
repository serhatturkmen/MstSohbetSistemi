
def Emoji(datas):
    for data in datas:
        data.messageContent = secure(data=data.messageContent)
        data.messageContent = data.messageContent.replace(":aslan", '<i class="em em-zebra_face"></i>')
    return datas


def secure(data):
    data = data.replace("<div>", "")
    data = data.replace("<p>", "")
    data = data.replace("<!--", "")
    data = data.replace("-->", "")
    data = data.replace("<", "")
    data = data.replace("</div>", "")
    data = data.replace("<p>", "")
    data = data.replace("</p>", "")
    data = data.replace("</", "")
    return data


