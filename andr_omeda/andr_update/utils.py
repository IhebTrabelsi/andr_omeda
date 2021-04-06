from andr_omeda.andr_update.models import Update, Message, Chat, Andruser
from andr_omeda.utils.colorify import colorify

"""iterating through all request data will not be necessary,
   as the depth of a certain value is already known from
   docs
"""
def id_key_sanitize_for_value(data , telegramIdKey, \
    AndromedaIdKey, key1=None, key2=None, key3=None):
    if key1 and data.get(key1, None):
        if not key2:
            if not data[key1].get(telegramIdKey, None):
                raise Exception("Andr_update utils Error")
            data[key1][AndromedaIdKey] = data[key1][telegramIdKey]
            del data[key1][telegramIdKey]
        elif key2 and not key3:
            if not data[key1].get(key2, None):
                raise Exception("Andr_update utils Error")
            data[key1][key2][AndromedaIdKey] = data[key1][key2][telegramIdKey]
            del data[key1][key2][telegramIdKey]
        else:
            if not data[key1].get(key2, None) and \
                not data[key1].get(key2, None).get(key3, None):
                raise Exception("Andr_update utils Error")
            data[key1][key2][key3][AndromedaIdKey] = data[key1][key2][key3][telegramIdKey]
            del data[key1][key2][key3][telegramIdKey]



def unicity_sanitize(data=None, context=None):
    if not data:
        raise Exception("data/context must be provided")
    if context:
        this__context={'validated_data': context['validated_data'], 'unicity': context['unicity']}
    else:
        this__context={'validated_data': data, 'unicity': {}}
    for attr_name in Update.get_need_sanitize_attrs():
        
        colorify(attr_name)

        if isinstance(attr_name, tuple):
            tmp_data = data 
            data = data.get(attr_name[0], None)
            if not data:
                data = tmp_data
                continue 
            else:
                attr_json_data = data.get(attr_name[1], None)
            if not attr_json_data:
                continue
             
            for group in Message.get_message_with_id_attrs():  
                for attr in group:
                    if attr_json_data.get(attr, None):
                        if 'chat' in group:
                            attr_json_data[attr]['chat_id'] = attr_json_data[attr]['id']
                            del attr_json_data[attr]['id']
                            this__context = Chat.context_chat_unicity_check_for_field_and_context(
                                attr_json_data,
                                attr,
                                this__context,
                                attr_name[1]
                            )
                        elif 'from' in group:
                            attr_json_data[attr]['user_id'] = attr_json_data[attr]['id']
                            del attr_json_data[attr]['id']
                            if attr == 'from':
                                attr_json_data['from_user'] = attr_json_data['from']
                                del attr_json_data['from']
                            this__context = Andruser.context_user_unicity_check_for_field_and_context(
                                attr_json_data,
                                attr,
                                this__context,
                                attr_name[1]
                            )
                            
                        else:
                            raise Exception("message attributes group not recognized ! ")
            tmp_data[attr_name[0]][attr_name[1]] = attr_json_data
            this__context['validated_data'] = tmp_data
            data = tmp_data
            continue
            
        if not data.get(attr_name, None):
            continue

        if data.get(attr_name).get('new_chat_participant', None):
            del data.get(attr_name)['new_chat_participant']
        if data.get(attr_name).get('left_chat_participant', None):
            del data.get(attr_name)['left_chat_participant']
        
        if data.get(attr_name).get('reply_to_message', None):
            this__context[attr_name + '__' + 'reply_to_message'] = data.get(attr_name).get('reply_to_message')
            del data.get(attr_name)['reply_to_message']
        if data.get(attr_name).get('pinned_message', None):
            this__context[attr_name + '__' + 'pinned_message'] = data.get(attr_name).get('pinned_message')
            del data.get(attr_name)['pinned_message']

        

        attr_json_data = data.get(attr_name)

        
        
        
        for group in Message.get_message_with_id_attrs():  
            for attr in group:
                if attr_json_data.get(attr, None):
                    if 'chat' in group:
                        attr_json_data[attr]['chat_id'] = attr_json_data[attr]['id']
                        del attr_json_data[attr]['id']
                        this__context = Chat.context_chat_unicity_check_for_field_and_context(
                            attr_json_data,
                            attr,
                            this__context,
                            attr_name
                        )
                    elif 'from' in group:
                        attr_json_data[attr]['user_id'] = attr_json_data[attr]['id']
                        del attr_json_data[attr]['id']
                        if attr == 'from':
                            attr_json_data['from_user'] = attr_json_data['from']
                            del attr_json_data['from']
                        this__context = Andruser.context_user_unicity_check_for_field_and_context(
                            attr_json_data,
                            attr,
                            this__context,
                            attr_name
                        )
                    else:
                        raise Exception("message attributes group not recognized ! ")
        data[attr_name] = attr_json_data
        this__context['validated_data'] = data
    return this__context


"""if attr_json_data.get('new_chat_members', None):
        new_chat_members = []
        for member in attr_json_data.pop('new_chat_members'):
            member['user_id'] = member['id']
            del member['id']
            new_chat_members.append(member)
        attr_json_data[attr_name]['new_chat_members'] = new_chat_members"""