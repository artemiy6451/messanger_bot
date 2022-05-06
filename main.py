import vk_api
from pprint import pprint
import json

token = '35da26e882936ceb1016bddb40c565050a9afccad9b4ae522f82bc36a124f57383e842c3ed6f69a54ed22'

session = vk_api.VkApi(token=token)
vk = session.get_api()


def get_conversation_list(vk_session) -> list:
    """Получение списка бесед и запись в JSON файл"""

    conversations_list = vk_session.messages.getConversations()['items']

    with open('data/conversations.json', 'w') as file:
        json.dump(conversations_list, indent=4, fp=file)

    return conversations_list


def get_unread_conversations(conversations) -> list:
    """Получение списка непрочитанных сообщений"""

    unread_conversation_list: list = []

    for conversation in conversations:
        if conversation['conversation']['is_marked_unread'] is not False:
            unread_conversation_list.append(conversation)

    return unread_conversation_list


conversations_list = get_conversation_list(vk)

print(conversations_list)
un = get_unread_conversations(conversations_list)
pprint(un, indent=4)
