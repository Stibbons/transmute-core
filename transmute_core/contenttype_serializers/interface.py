from abc import ABCMeta, abstractmethod, abstractproperty


class ContentTypeSerializer(object):
    """
    A ContentTypeSerializer handles the conversion from
    a python data structure to a bytes object representing
    the content in a particular content type.
    """

    __metaclass__ = ABCMeta

    @abstractproperty
    def content_type(self):
        """
        return back what a list of content types
        this serializer should support.
        """

    @abstractmethod
    def to_type(data):
        """
        should return back a bytes (or string in python 2),
        representation of your object, to be used in e.g. response
        bodies.

        a ValueError should be returned in the case where
        the object cannote be serialized.
        """

    @abstractmethod
    def from_type(raw_bytes):
        """
        given a bytes object, should return a base python data
        structure that represents the object.

        a ValueError should be returned in the case where
        the object cannot be serialized.
        """

    @abstractmethod
    def can_handle(content_type_name):
        """
        given a content type, returns true if this serializer
        can convert bodies of the given type.
        """
