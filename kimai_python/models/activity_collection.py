# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen, but we try to avoid them.   # noqa: E501

    OpenAPI spec version: 0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActivityCollection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'visible': 'bool',
        'fixed_rate': 'float',
        'hourly_rate': 'float',
        'color': 'str',
        'project': 'int',
        'meta_fields': 'list[ActivityMeta]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'visible': 'visible',
        'fixed_rate': 'fixedRate',
        'hourly_rate': 'hourlyRate',
        'color': 'color',
        'project': 'project',
        'meta_fields': 'metaFields'
    }

    def __init__(self, id=None, name=None, visible=None, fixed_rate=None, hourly_rate=None, color=None, project=None, meta_fields=None):  # noqa: E501
        """ActivityCollection - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._visible = None
        self._fixed_rate = None
        self._hourly_rate = None
        self._color = None
        self._project = None
        self._meta_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.visible = visible
        if fixed_rate is not None:
            self.fixed_rate = fixed_rate
        if hourly_rate is not None:
            self.hourly_rate = hourly_rate
        if color is not None:
            self.color = color
        if project is not None:
            self.project = project
        if meta_fields is not None:
            self.meta_fields = meta_fields

    @property
    def id(self):
        """Gets the id of this ActivityCollection.  # noqa: E501


        :return: The id of this ActivityCollection.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActivityCollection.


        :param id: The id of this ActivityCollection.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ActivityCollection.  # noqa: E501


        :return: The name of this ActivityCollection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityCollection.


        :param name: The name of this ActivityCollection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 150:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")  # noqa: E501
        if name is not None and len(name) < 2:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `2`")  # noqa: E501

        self._name = name

    @property
    def visible(self):
        """Gets the visible of this ActivityCollection.  # noqa: E501


        :return: The visible of this ActivityCollection.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ActivityCollection.


        :param visible: The visible of this ActivityCollection.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501

        self._visible = visible

    @property
    def fixed_rate(self):
        """Gets the fixed_rate of this ActivityCollection.  # noqa: E501


        :return: The fixed_rate of this ActivityCollection.  # noqa: E501
        :rtype: float
        """
        return self._fixed_rate

    @fixed_rate.setter
    def fixed_rate(self, fixed_rate):
        """Sets the fixed_rate of this ActivityCollection.


        :param fixed_rate: The fixed_rate of this ActivityCollection.  # noqa: E501
        :type: float
        """

        self._fixed_rate = fixed_rate

    @property
    def hourly_rate(self):
        """Gets the hourly_rate of this ActivityCollection.  # noqa: E501


        :return: The hourly_rate of this ActivityCollection.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        """Sets the hourly_rate of this ActivityCollection.


        :param hourly_rate: The hourly_rate of this ActivityCollection.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def color(self):
        """Gets the color of this ActivityCollection.  # noqa: E501


        :return: The color of this ActivityCollection.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ActivityCollection.


        :param color: The color of this ActivityCollection.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def project(self):
        """Gets the project of this ActivityCollection.  # noqa: E501


        :return: The project of this ActivityCollection.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ActivityCollection.


        :param project: The project of this ActivityCollection.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def meta_fields(self):
        """Gets the meta_fields of this ActivityCollection.  # noqa: E501


        :return: The meta_fields of this ActivityCollection.  # noqa: E501
        :rtype: list[ActivityMeta]
        """
        return self._meta_fields

    @meta_fields.setter
    def meta_fields(self, meta_fields):
        """Sets the meta_fields of this ActivityCollection.


        :param meta_fields: The meta_fields of this ActivityCollection.  # noqa: E501
        :type: list[ActivityMeta]
        """

        self._meta_fields = meta_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ActivityCollection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActivityCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
