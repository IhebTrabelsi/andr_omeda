from django.core.exceptions import ValidationError


class TelegramBotDoesNotExist(ValidationError):
    def __init__(self, token, message="This Bot does not exist on telegraam, please create one!"):
        self.token = token
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.token, self.message)


class TBDE(ValidationError):
    pass


class TelegramBotAsyncCreationError(ValidationError):
    def __init__(self, token, message="This Bot is already saved!"):
        self.token = token
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.token, self.message)


class TelegramBotAsyncCreationFieldError(ValidationError):
    def __init__(self, token, message="Attempting to create bot model without token set!"):
        self.token = token
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.token, self.message)


class TelegramBotWebhookSetError(ValidationError):
    def __init__(self, description, message="Something went wrong when sending setWebHook request!"):
        self.description = description
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "description: {} -> {}".format(self.description, self.message)


class TelegramBotFieldAccessError(ValidationError):
    def __init__(self, field, message="Trying to access this field caused an error!"):
        self.field = field
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "field: {} -> {}".format(self.field, self.message)


class TelegramAPIResultParsingError(ValidationError):
    def __init__(self, method_name, message="Trying to parse result from telegram api request caused an error!"):
        self.method_name = method_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "method name: {} -> {}".format(self.method_name, self.message)
