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


class GetEmailCampaign(object):
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
        'id': 'int',
        'name': 'str',
        'subject': 'str',
        'type': 'str',
        'status': 'str',
        'scheduled_at': 'str',
        'test_sent': 'bool',
        'header': 'str',
        'footer': 'str',
        'sender': 'GetExtendedCampaignOverviewSender',
        'reply_to': 'str',
        'to_field': 'str',
        'html_content': 'str',
        'share_link': 'str',
        'tag': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'inline_image_activation': 'bool',
        'mirror_active': 'bool',
        'recurring': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subject': 'subject',
        'type': 'type',
        'status': 'status',
        'scheduled_at': 'scheduledAt',
        'test_sent': 'testSent',
        'header': 'header',
        'footer': 'footer',
        'sender': 'sender',
        'reply_to': 'replyTo',
        'to_field': 'toField',
        'html_content': 'htmlContent',
        'share_link': 'shareLink',
        'tag': 'tag',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'inline_image_activation': 'inlineImageActivation',
        'mirror_active': 'mirrorActive',
        'recurring': 'recurring'
    }

    def __init__(self, id=None, name=None, subject=None, type=None, status=None, scheduled_at=None, test_sent=None, header=None, footer=None, sender=None, reply_to=None, to_field=None, html_content=None, share_link=None, tag=None, created_at=None, modified_at=None, inline_image_activation=None, mirror_active=None, recurring=None):
        """
        GetEmailCampaign - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._subject = None
        self._type = None
        self._status = None
        self._scheduled_at = None
        self._test_sent = None
        self._header = None
        self._footer = None
        self._sender = None
        self._reply_to = None
        self._to_field = None
        self._html_content = None
        self._share_link = None
        self._tag = None
        self._created_at = None
        self._modified_at = None
        self._inline_image_activation = None
        self._mirror_active = None
        self._recurring = None

        self.id = id
        self.name = name
        self.subject = subject
        self.type = type
        self.status = status
        if scheduled_at is not None:
          self.scheduled_at = scheduled_at
        self.test_sent = test_sent
        self.header = header
        self.footer = footer
        if sender is not None:
          self.sender = sender
        self.reply_to = reply_to
        self.to_field = to_field
        self.html_content = html_content
        self.share_link = share_link
        self.tag = tag
        self.created_at = created_at
        self.modified_at = modified_at
        if inline_image_activation is not None:
          self.inline_image_activation = inline_image_activation
        if mirror_active is not None:
          self.mirror_active = mirror_active
        if recurring is not None:
          self.recurring = recurring

    @property
    def id(self):
        """
        Gets the id of this GetEmailCampaign.
        ID of the campaign

        :return: The id of this GetEmailCampaign.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetEmailCampaign.
        ID of the campaign

        :param id: The id of this GetEmailCampaign.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GetEmailCampaign.
        Name of the campaign

        :return: The name of this GetEmailCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetEmailCampaign.
        Name of the campaign

        :param name: The name of this GetEmailCampaign.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def subject(self):
        """
        Gets the subject of this GetEmailCampaign.
        Subject of the campaign

        :return: The subject of this GetEmailCampaign.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this GetEmailCampaign.
        Subject of the campaign

        :param subject: The subject of this GetEmailCampaign.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def type(self):
        """
        Gets the type of this GetEmailCampaign.
        Type of campaign

        :return: The type of this GetEmailCampaign.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GetEmailCampaign.
        Type of campaign

        :param type: The type of this GetEmailCampaign.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["classic", "trigger"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this GetEmailCampaign.
        Status of the campaign

        :return: The status of this GetEmailCampaign.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this GetEmailCampaign.
        Status of the campaign

        :param status: The status of this GetEmailCampaign.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["draft", "sent", "archive", "queued", "suspended", "in_process"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def scheduled_at(self):
        """
        Gets the scheduled_at of this GetEmailCampaign.
        Date on which campaign is scheduled (YYYY-MM-DD HH:mm:ss)

        :return: The scheduled_at of this GetEmailCampaign.
        :rtype: str
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """
        Sets the scheduled_at of this GetEmailCampaign.
        Date on which campaign is scheduled (YYYY-MM-DD HH:mm:ss)

        :param scheduled_at: The scheduled_at of this GetEmailCampaign.
        :type: str
        """
        if scheduled_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', scheduled_at):
            raise ValueError("Invalid value for `scheduled_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._scheduled_at = scheduled_at

    @property
    def test_sent(self):
        """
        Gets the test_sent of this GetEmailCampaign.
        Retrieved the status of test email sending. (true=Test email has been sent  false=Test email has not been sent)

        :return: The test_sent of this GetEmailCampaign.
        :rtype: bool
        """
        return self._test_sent

    @test_sent.setter
    def test_sent(self, test_sent):
        """
        Sets the test_sent of this GetEmailCampaign.
        Retrieved the status of test email sending. (true=Test email has been sent  false=Test email has not been sent)

        :param test_sent: The test_sent of this GetEmailCampaign.
        :type: bool
        """
        if test_sent is None:
            raise ValueError("Invalid value for `test_sent`, must not be `None`")

        self._test_sent = test_sent

    @property
    def header(self):
        """
        Gets the header of this GetEmailCampaign.
        Header of the campaign

        :return: The header of this GetEmailCampaign.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this GetEmailCampaign.
        Header of the campaign

        :param header: The header of this GetEmailCampaign.
        :type: str
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")

        self._header = header

    @property
    def footer(self):
        """
        Gets the footer of this GetEmailCampaign.
        Footer of the campaign

        :return: The footer of this GetEmailCampaign.
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """
        Sets the footer of this GetEmailCampaign.
        Footer of the campaign

        :param footer: The footer of this GetEmailCampaign.
        :type: str
        """
        if footer is None:
            raise ValueError("Invalid value for `footer`, must not be `None`")

        self._footer = footer

    @property
    def sender(self):
        """
        Gets the sender of this GetEmailCampaign.

        :return: The sender of this GetEmailCampaign.
        :rtype: GetExtendedCampaignOverviewSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this GetEmailCampaign.

        :param sender: The sender of this GetEmailCampaign.
        :type: GetExtendedCampaignOverviewSender
        """

        self._sender = sender

    @property
    def reply_to(self):
        """
        Gets the reply_to of this GetEmailCampaign.
        Email defined as the \"Reply to\" of the campaign

        :return: The reply_to of this GetEmailCampaign.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this GetEmailCampaign.
        Email defined as the \"Reply to\" of the campaign

        :param reply_to: The reply_to of this GetEmailCampaign.
        :type: str
        """
        if reply_to is None:
            raise ValueError("Invalid value for `reply_to`, must not be `None`")

        self._reply_to = reply_to

    @property
    def to_field(self):
        """
        Gets the to_field of this GetEmailCampaign.
        Customisation of the \"to\" field of the campaign

        :return: The to_field of this GetEmailCampaign.
        :rtype: str
        """
        return self._to_field

    @to_field.setter
    def to_field(self, to_field):
        """
        Sets the to_field of this GetEmailCampaign.
        Customisation of the \"to\" field of the campaign

        :param to_field: The to_field of this GetEmailCampaign.
        :type: str
        """
        if to_field is None:
            raise ValueError("Invalid value for `to_field`, must not be `None`")

        self._to_field = to_field

    @property
    def html_content(self):
        """
        Gets the html_content of this GetEmailCampaign.
        HTML content of the campaign

        :return: The html_content of this GetEmailCampaign.
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """
        Sets the html_content of this GetEmailCampaign.
        HTML content of the campaign

        :param html_content: The html_content of this GetEmailCampaign.
        :type: str
        """
        if html_content is None:
            raise ValueError("Invalid value for `html_content`, must not be `None`")

        self._html_content = html_content

    @property
    def share_link(self):
        """
        Gets the share_link of this GetEmailCampaign.
        Link to share the campaign on social medias

        :return: The share_link of this GetEmailCampaign.
        :rtype: str
        """
        return self._share_link

    @share_link.setter
    def share_link(self, share_link):
        """
        Sets the share_link of this GetEmailCampaign.
        Link to share the campaign on social medias

        :param share_link: The share_link of this GetEmailCampaign.
        :type: str
        """
        if share_link is None:
            raise ValueError("Invalid value for `share_link`, must not be `None`")

        self._share_link = share_link

    @property
    def tag(self):
        """
        Gets the tag of this GetEmailCampaign.
        Tag of the campaign

        :return: The tag of this GetEmailCampaign.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this GetEmailCampaign.
        Tag of the campaign

        :param tag: The tag of this GetEmailCampaign.
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")

        self._tag = tag

    @property
    def created_at(self):
        """
        Gets the created_at of this GetEmailCampaign.
        Creation date of the campaign (YYYY-MM-DD HH:mm:ss)

        :return: The created_at of this GetEmailCampaign.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this GetEmailCampaign.
        Creation date of the campaign (YYYY-MM-DD HH:mm:ss)

        :param created_at: The created_at of this GetEmailCampaign.
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")
        if created_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', created_at):
            raise ValueError("Invalid value for `created_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this GetEmailCampaign.
        Date of last modification of the campaign (YYYY-MM-DD HH:mm:ss)

        :return: The modified_at of this GetEmailCampaign.
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this GetEmailCampaign.
        Date of last modification of the campaign (YYYY-MM-DD HH:mm:ss)

        :param modified_at: The modified_at of this GetEmailCampaign.
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")
        if modified_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', modified_at):
            raise ValueError("Invalid value for `modified_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._modified_at = modified_at

    @property
    def inline_image_activation(self):
        """
        Gets the inline_image_activation of this GetEmailCampaign.
        Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email.

        :return: The inline_image_activation of this GetEmailCampaign.
        :rtype: bool
        """
        return self._inline_image_activation

    @inline_image_activation.setter
    def inline_image_activation(self, inline_image_activation):
        """
        Sets the inline_image_activation of this GetEmailCampaign.
        Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email.

        :param inline_image_activation: The inline_image_activation of this GetEmailCampaign.
        :type: bool
        """

        self._inline_image_activation = inline_image_activation

    @property
    def mirror_active(self):
        """
        Gets the mirror_active of this GetEmailCampaign.
        Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign

        :return: The mirror_active of this GetEmailCampaign.
        :rtype: bool
        """
        return self._mirror_active

    @mirror_active.setter
    def mirror_active(self, mirror_active):
        """
        Sets the mirror_active of this GetEmailCampaign.
        Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign

        :param mirror_active: The mirror_active of this GetEmailCampaign.
        :type: bool
        """

        self._mirror_active = mirror_active

    @property
    def recurring(self):
        """
        Gets the recurring of this GetEmailCampaign.
        FOR TRIGGER ONLY ! Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times

        :return: The recurring of this GetEmailCampaign.
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """
        Sets the recurring of this GetEmailCampaign.
        FOR TRIGGER ONLY ! Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times

        :param recurring: The recurring of this GetEmailCampaign.
        :type: bool
        """

        self._recurring = recurring

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
        if not isinstance(other, GetEmailCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
