from effective_python.module.models import Model


if __name__ == '__main__':
    cat = Model.env['animal.cat']()
    cat.say()
    cat.get_scared()
    print('\n\n')

    train = Model.env['transport.train']()
    train.view_inside()
