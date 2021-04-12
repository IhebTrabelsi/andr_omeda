from andr_omeda.andr_update.models import Update, Message, Chat, Andruser, Poll, \
    InlineQuery
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

def is_entities__users(l):
    for u in l:
        if u:
            return True
    return False
##################################################################################
##################################################################################
##################################################################################
def unicity_sanitize(req_data=None):
    """
    req_data: {'message':{'message_id':123456, ...}, '_id':123456789}
    """
    req_data = InlineQuery.inlinequery_validation( req_data )
   

    this__unicity = {}
    this__lists = {}
    this__specials = {}
    for update_attr in Update.get_need_sanitize_attrs():
        if isinstance(update_attr, tuple):
            if not req_data.get(update_attr[0], None):
                continue 
            if not req_data[update_attr[0]].get(update_attr[1], None):
                continue 

            for group in Message.get_message_with_id_attrs():
                for id_able in group:
                    if 'chat' in group:
                        this__unicity = Chat.context_chat_unicity_check_for_field_and_context(
                            req_data[update_attr[0]][update_attr[1]],
                            this__unicity,
                            id_able,
                            update_attr[1]
                        )
                    if 'user' in group:
                        this__unicity = Andruser.context_user_unicity_check_for_field_and_context(
                            req_data[update_attr[0]][update_attr[1]],
                            this__unicity,
                            id_able,
                            update_attr[1]
                        )
            continue





        #############################
        if not req_data.get(update_attr, None):
            continue 

        req_data[update_attr] = Andruser.from_user_sanitize( req_data[update_attr] )
        req_data[update_attr] = Poll.poll_id_sanitize( req_data[update_attr] )

        this__lists = Poll.extract_lists( req_data[update_attr], this__lists )
        if update_attr in Update.get_need_sanitize_attrs()[:4]:
            this__lists, this__specials = Message.extract_lists( req_data[update_attr], this__lists, this__specials )
        
        
        if req_data[update_attr].get('pinned_message', None):
            this__unicity[update_attr + '__' + 'pinned_message'] = \
                req_data[update_attr]['pinned_message']['message_id']
            del req_data[update_attr]['pinned_message']
        
        if req_data[update_attr].get('reply_to_message', None):
            this__unicity[update_attr + '__' + 'reply_to_message'] = \
                req_data[update_attr]['reply_to_message']['message_id']
            del req_data[update_attr]['reply_to_message']
        #############################
        
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
    this__context = {'validated_data': req_data, 'unicity': this__unicity, 'lists': this__lists, 'specials': this__specials}
    return this__context
    

