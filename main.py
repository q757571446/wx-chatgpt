import openai, re
from wxchat import WeixinClient, MsgType, Message

# 填入你的apikey
openai.api_key = "xxxx"


def get_response(text: str) -> [str]:
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
    return [choice["message"]["content"] for choice in response["choices"]]


if __name__ == '__main__':
    client = WeixinClient()
    profile = client.login()

    @client.message(wxid="wxid_.*", msgtype=MsgType.TEXT)
    def friend_message(message: Message):
        reply = get_response(message.content)
        for msg in reply:
            client.send_text(message.wxid, msg)


    @client.message(wxid=".*@chatroom", msgtype=MsgType.TEXT, at_users=[profile.wxid])
    def chatroom_message(message: Message):
        content = re.sub(r"\s*@\S+?\s*(:| |$)", "", message.content)
        print("origin: %s, clean: %s" % (message.content, content))
        reply = get_response(content)
        for msg in reply:
            client.send_text(message.wxid, msg)

    client.run_forever()
