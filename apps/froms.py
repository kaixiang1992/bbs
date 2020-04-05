from wtforms import Form


class BaseForm(Form):
    def get_random_error(self):
        message = self.errors.popitem()[1][0]
        return message

    def get_all_errors(self):
        errors = self.errors
        return errors
