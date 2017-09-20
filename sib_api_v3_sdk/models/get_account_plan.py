# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetAccountPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'type': 'str',
        'credits_type': 'str',
        'credits': 'int'
    }

    attribute_map = {
        'type': 'type',
        'credits_type': 'creditsType',
        'credits': 'credits'
    }

    def __init__(self, type=None, credits_type=None, credits=None):
        """
        GetAccountPlan - a model defined in Swagger
        """

        self._type = None
        self._credits_type = None
        self._credits = None

        self.type = type
        self.credits_type = credits_type
        self.credits = credits

    @property
    def type(self):
        """
        Gets the type of this GetAccountPlan.
        Displays the plan type of the user

        :return: The type of this GetAccountPlan.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GetAccountPlan.
        Displays the plan type of the user

        :param type: The type of this GetAccountPlan.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["payAsYouGo", "unlimited", "free", "subscription", "sms", "reseller"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def credits_type(self):
        """
        Gets the credits_type of this GetAccountPlan.
        This is the type of the credit, \"User Limit\" or \"Send Limit\" are two possible types of credit of a user. \"User Limit\" implies the total number of subscribers you can add to your account, and \"Send Limit\" implies the total number of emails you can send to the subscribers in your account.

        :return: The credits_type of this GetAccountPlan.
        :rtype: str
        """
        return self._credits_type

    @credits_type.setter
    def credits_type(self, credits_type):
        """
        Sets the credits_type of this GetAccountPlan.
        This is the type of the credit, \"User Limit\" or \"Send Limit\" are two possible types of credit of a user. \"User Limit\" implies the total number of subscribers you can add to your account, and \"Send Limit\" implies the total number of emails you can send to the subscribers in your account.

        :param credits_type: The credits_type of this GetAccountPlan.
        :type: str
        """
        if credits_type is None:
            raise ValueError("Invalid value for `credits_type`, must not be `None`")
        allowed_values = ["userLimit", "sendLimit"]
        if credits_type not in allowed_values:
            raise ValueError(
                "Invalid value for `credits_type` ({0}), must be one of {1}"
                .format(credits_type, allowed_values)
            )

        self._credits_type = credits_type

    @property
    def credits(self):
        """
        Gets the credits of this GetAccountPlan.
        Remaining credits of the user. This can either be \"User Limit\" or \"Send Limit\" depending on the plan.

        :return: The credits of this GetAccountPlan.
        :rtype: int
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """
        Sets the credits of this GetAccountPlan.
        Remaining credits of the user. This can either be \"User Limit\" or \"Send Limit\" depending on the plan.

        :param credits: The credits of this GetAccountPlan.
        :type: int
        """
        if credits is None:
            raise ValueError("Invalid value for `credits`, must not be `None`")

        self._credits = credits

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetAccountPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
