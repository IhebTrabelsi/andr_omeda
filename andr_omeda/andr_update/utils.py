from andr_omeda.andr_update.models import Update, Message, Chat, Andruser, Poll
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




##################################################################################
##################################################################################
##################################################################################
def unicity_sanitize(req_data=None):
    """
    req_data: {'message':{'message_id':123456, ...}, '_id':123456789}
    """
    
    this__unicity = {}
    this__lists = {}
    #TODO remove trimming in get_need_sanitize_attrs()
    for update_attr in Update.get_need_sanitize_attrs()[:10]:
        if not req_data.get(update_attr, None):
            continue 

        req_data[update_attr] = Andruser.from_user_sanitize( req_data[update_attr] )
        req_data[update_attr] = Poll.poll_id_sanitize( req_data[update_attr] )
        this__lists = Poll.extract_lists( req_data[update_attr], this__lists)
        
        if req_data[update_attr].get('pinned_message', None):
            this__unicity[update_attr + '__' + 'pinned_message'] = \
                req_data[update_attr]['pinned_message']['message_id']
            del req_data[update_attr]['pinned_message']
        
        if req_data[update_attr].get('reply_to_message', None):
            this__unicity[update_attr + '__' + 'reply_to_message'] = \
                req_data[update_attr]['reply_to_message']['message_id']
            del req_data[update_attr]['reply_to_message']
        
        for group in Message.get_message_with_id_attrs():
            for id_able in group:
                if 'chat' in group:
                    this__unicity = Chat.context_chat_unicity_check_for_field_and_context(
                        req_data[update_attr],
                        this__unicity,
                        id_able,
                        update_attr
                    )
                if 'user' in group:
                    this__unicity = Andruser.context_user_unicity_check_for_field_and_context(
                        req_data[update_attr],
                        this__unicity,
                        id_able,
                        update_attr
                    )
    this__context = {'validated_data': req_data, 'unicity': this__unicity, 'lists': this__lists}
    return this__context
    

##################################################################################
##################################################################################
##################################################################################
"""def unicity_sanitize(data=None, context=None):
    if not data:
        raise Exception("data/context must be provided")
    if context:
        this__context = context
    else:
        this__context={'validated_data': data, 'unicity': {}}
    for attr_name in Update.get_need_sanitize_attrs():
        
        #colorify(attr_name, fore='RED', back='YELLOW', highlight="ATTR_NAME")

        if isinstance(attr_name, tuple):
            tmp_data = data 
            data = data.get(attr_name[0], None)
            if not data:
                data = tmp_data
                continue 
            else:
                attr_json_data = data.get(attr_name[1], None)
                this__sub_context = {
                    'validated_data': '',
                    'unicity': {}}
            if not attr_json_data:
                continue
             
            for group in Message.get_message_with_id_attrs():  
                for attr in group:
                    if attr_json_data.get(attr, None):
                        if 'chat' in group:
                            attr_json_data[attr]['chat_id'] = attr_json_data[attr]['id']
                            del attr_json_data[attr]['id']
                            this__sub_context = Chat.context_chat_unicity_check_for_field_and_context(
                                attr_json_data,
                                attr,
                                this__sub_context,
                                attr_name[1]
                            )
                        elif 'from' in group:
                            attr_json_data[attr]['user_id'] = attr_json_data[attr]['id']
                            del attr_json_data[attr]['id']
                            if attr == 'from':
                                attr_json_data['from_user'] = attr_json_data['from']
                                del attr_json_data['from']
                            this__sub_context = Andruser.context_user_unicity_check_for_field_and_context(
                                attr_json_data,
                                attr,
                                this__sub_context,
                                attr_name[1]
                            )
                            
                        else:
                            raise Exception("message attributes group not recognized ! ")
            
            this__context['validated_data'][attr_name[0]] = \
                this__sub_context['validated_data']
            
            this__context['unicity'].append(this__sub_context['unicity'])
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
                        # 'id' alwas present in Chat models, hence direct access
                        attr_json_data[attr]['chat_id'] = attr_json_data[attr]['id']
                        del attr_json_data[attr]['id']
                        this__context = Chat.context_chat_unicity_check_for_field_and_context(
                            attr_json_data,
                            attr,
                            this__context,
                            attr_name
                        )
                    elif 'from' in group:
                        # 'id' alwas present in User models, hence direct access
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
                        raise Exception("message attributes group not recognized ! ")"""
        
   

"""if attr_json_data.get('new_chat_members', None):
        new_chat_members = []
        for member in attr_json_data.pop('new_chat_members'):
            member['user_id'] = member['id']
            del member['id']
            new_chat_members.append(member)
        attr_json_data[attr_name]['new_chat_members'] = new_chat_members"""