"""
A fully initialized instance to be copied or cloned
Example: Chess game - Initial setup
"""
import copy


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """
        Clone a prototype and update inner attributes dictionary
        """

        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)

        return obj


class PrototypeDispatcher(object):

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """
        Get all objects
        """

        return self._objects

    def register_object(self, name, obj):
        """
        Register an object
        """

        self._objects[name] = obj

    def unregister_object(self, name):
        """
        Unregister an object
        """

        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    print "Object a", a
    print "Dict values ", a.__dict__
    b = prototype.clone(value='b-value', is_checked=True)
    print "Object b", b
    print "Dict values ", b.__dict__
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print "=================================="
    print "Dispatcher object ", dispatcher.get_objects()
    print "Dispatcher values ", ([{n: p.value} for n, p in dispatcher.get_objects().items()])

if __name__ == '__main__':
    main()
