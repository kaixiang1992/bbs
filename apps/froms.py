from wtforms import Form


class BaseForm(Form):
    def get_random_error(self):
        message = self.errors.popitem()[1][0]
        return message

    def get_all_errors(self):
        errors = self.errors
        return errors

    # TODO: 重写父类validate方法
    def validate(self):
        return super(BaseForm, self).validate()
