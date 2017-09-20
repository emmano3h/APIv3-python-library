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


class CreateSmtpTemplate(object):
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
        'tag': 'str',
        'sender': 'CreateSmtpTemplateSender',
        'template_name': 'str',
        'html_content': 'str',
        'html_url': 'str',
        'subject': 'str',
        'reply_to': 'str',
        'to_field': 'str',
        'attachment_url': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'tag': 'tag',
        'sender': 'sender',
        'template_name': 'templateName',
        'html_content': 'htmlContent',
        'html_url': 'htmlUrl',
        'subject': 'subject',
        'reply_to': 'replyTo',
        'to_field': 'toField',
        'attachment_url': 'attachmentUrl',
        'is_active': 'isActive'
    }

    def __init__(self, tag=None, sender=None, template_name=None, html_content=None, html_url=None, subject=None, reply_to=None, to_field=None, attachment_url=None, is_active=None):
        """
        CreateSmtpTemplate - a model defined in Swagger
        """

        self._tag = None
        self._sender = None
        self._template_name = None
        self._html_content = None
        self._html_url = None
        self._subject = None
        self._reply_to = None
        self._to_field = None
        self._attachment_url = None
        self._is_active = None

        if tag is not None:
          self.tag = tag
        if sender is not None:
          self.sender = sender
        self.template_name = template_name
        if html_content is not None:
          self.html_content = html_content
        if html_url is not None:
          self.html_url = html_url
        self.subject = subject
        if reply_to is not None:
          self.reply_to = reply_to
        if to_field is not None:
          self.to_field = to_field
        if attachment_url is not None:
          self.attachment_url = attachment_url
        if is_active is not None:
          self.is_active = is_active

    @property
    def tag(self):
        """
        Gets the tag of this CreateSmtpTemplate.
        Tag of the template

        :return: The tag of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this CreateSmtpTemplate.
        Tag of the template

        :param tag: The tag of this CreateSmtpTemplate.
        :type: str
        """

        self._tag = tag

    @property
    def sender(self):
        """
        Gets the sender of this CreateSmtpTemplate.

        :return: The sender of this CreateSmtpTemplate.
        :rtype: CreateSmtpTemplateSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this CreateSmtpTemplate.

        :param sender: The sender of this CreateSmtpTemplate.
        :type: CreateSmtpTemplateSender
        """

        self._sender = sender

    @property
    def template_name(self):
        """
        Gets the template_name of this CreateSmtpTemplate.
        Name of the template

        :return: The template_name of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """
        Sets the template_name of this CreateSmtpTemplate.
        Name of the template

        :param template_name: The template_name of this CreateSmtpTemplate.
        :type: str
        """
        if template_name is None:
            raise ValueError("Invalid value for `template_name`, must not be `None`")

        self._template_name = template_name

    @property
    def html_content(self):
        """
        Gets the html_content of this CreateSmtpTemplate.
        Body of the message (HTML version). The field must have more than 10 characters. REQUIRED if htmlUrl is empty

        :return: The html_content of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """
        Sets the html_content of this CreateSmtpTemplate.
        Body of the message (HTML version). The field must have more than 10 characters. REQUIRED if htmlUrl is empty

        :param html_content: The html_content of this CreateSmtpTemplate.
        :type: str
        """

        self._html_content = html_content

    @property
    def html_url(self):
        """
        Gets the html_url of this CreateSmtpTemplate.
        Url which contents the body of the email message. REQUIRED if htmlContent is empty

        :return: The html_url of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this CreateSmtpTemplate.
        Url which contents the body of the email message. REQUIRED if htmlContent is empty

        :param html_url: The html_url of this CreateSmtpTemplate.
        :type: str
        """

        self._html_url = html_url

    @property
    def subject(self):
        """
        Gets the subject of this CreateSmtpTemplate.
        Subject of the template

        :return: The subject of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CreateSmtpTemplate.
        Subject of the template

        :param subject: The subject of this CreateSmtpTemplate.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def reply_to(self):
        """
        Gets the reply_to of this CreateSmtpTemplate.
        Email on which campaign recipients will be able to reply to

        :return: The reply_to of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this CreateSmtpTemplate.
        Email on which campaign recipients will be able to reply to

        :param reply_to: The reply_to of this CreateSmtpTemplate.
        :type: str
        """

        self._reply_to = reply_to

    @property
    def to_field(self):
        """
        Gets the to_field of this CreateSmtpTemplate.
        This is to personalize the «To» Field. If you want to include the first name and last name of your recipient, add [FNAME] [LNAME]. To use the contact attributes here, these must already exist in SendinBlue account

        :return: The to_field of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._to_field

    @to_field.setter
    def to_field(self, to_field):
        """
        Sets the to_field of this CreateSmtpTemplate.
        This is to personalize the «To» Field. If you want to include the first name and last name of your recipient, add [FNAME] [LNAME]. To use the contact attributes here, these must already exist in SendinBlue account

        :param to_field: The to_field of this CreateSmtpTemplate.
        :type: str
        """

        self._to_field = to_field

    @property
    def attachment_url(self):
        """
        Gets the attachment_url of this CreateSmtpTemplate.
        Absolute url of the attachment (no local file). Extensions allowed xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff and rtf

        :return: The attachment_url of this CreateSmtpTemplate.
        :rtype: str
        """
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, attachment_url):
        """
        Sets the attachment_url of this CreateSmtpTemplate.
        Absolute url of the attachment (no local file). Extensions allowed xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff and rtf

        :param attachment_url: The attachment_url of this CreateSmtpTemplate.
        :type: str
        """

        self._attachment_url = attachment_url

    @property
    def is_active(self):
        """
        Gets the is_active of this CreateSmtpTemplate.
        Status of template. isActive = true means template is active and isActive = false means template is inactive

        :return: The is_active of this CreateSmtpTemplate.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this CreateSmtpTemplate.
        Status of template. isActive = true means template is active and isActive = false means template is inactive

        :param is_active: The is_active of this CreateSmtpTemplate.
        :type: bool
        """

        self._is_active = is_active

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
        if not isinstance(other, CreateSmtpTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
