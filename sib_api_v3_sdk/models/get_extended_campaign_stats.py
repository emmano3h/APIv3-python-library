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


class GetExtendedCampaignStats(object):
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
        'campaign_stats': 'list[object]',
        'mirror_click': 'int',
        'remaining': 'int',
        'links_stats': 'dict(str, GetExtendedCampaignStatsLinksStats)',
        'stats_by_domain': 'GetStatsByDomain'
    }

    attribute_map = {
        'campaign_stats': 'campaignStats',
        'mirror_click': 'mirrorClick',
        'remaining': 'remaining',
        'links_stats': 'linksStats',
        'stats_by_domain': 'statsByDomain'
    }

    def __init__(self, campaign_stats=None, mirror_click=None, remaining=None, links_stats=None, stats_by_domain=None):
        """
        GetExtendedCampaignStats - a model defined in Swagger
        """

        self._campaign_stats = None
        self._mirror_click = None
        self._remaining = None
        self._links_stats = None
        self._stats_by_domain = None

        self.campaign_stats = campaign_stats
        self.mirror_click = mirror_click
        self.remaining = remaining
        self.links_stats = links_stats
        self.stats_by_domain = stats_by_domain

    @property
    def campaign_stats(self):
        """
        Gets the campaign_stats of this GetExtendedCampaignStats.

        :return: The campaign_stats of this GetExtendedCampaignStats.
        :rtype: list[object]
        """
        return self._campaign_stats

    @campaign_stats.setter
    def campaign_stats(self, campaign_stats):
        """
        Sets the campaign_stats of this GetExtendedCampaignStats.

        :param campaign_stats: The campaign_stats of this GetExtendedCampaignStats.
        :type: list[object]
        """
        if campaign_stats is None:
            raise ValueError("Invalid value for `campaign_stats`, must not be `None`")

        self._campaign_stats = campaign_stats

    @property
    def mirror_click(self):
        """
        Gets the mirror_click of this GetExtendedCampaignStats.
        Number of clicks on mirror link

        :return: The mirror_click of this GetExtendedCampaignStats.
        :rtype: int
        """
        return self._mirror_click

    @mirror_click.setter
    def mirror_click(self, mirror_click):
        """
        Sets the mirror_click of this GetExtendedCampaignStats.
        Number of clicks on mirror link

        :param mirror_click: The mirror_click of this GetExtendedCampaignStats.
        :type: int
        """
        if mirror_click is None:
            raise ValueError("Invalid value for `mirror_click`, must not be `None`")

        self._mirror_click = mirror_click

    @property
    def remaining(self):
        """
        Gets the remaining of this GetExtendedCampaignStats.
        Number of remaning emails to send

        :return: The remaining of this GetExtendedCampaignStats.
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """
        Sets the remaining of this GetExtendedCampaignStats.
        Number of remaning emails to send

        :param remaining: The remaining of this GetExtendedCampaignStats.
        :type: int
        """
        if remaining is None:
            raise ValueError("Invalid value for `remaining`, must not be `None`")

        self._remaining = remaining

    @property
    def links_stats(self):
        """
        Gets the links_stats of this GetExtendedCampaignStats.

        :return: The links_stats of this GetExtendedCampaignStats.
        :rtype: dict(str, GetExtendedCampaignStatsLinksStats)
        """
        return self._links_stats

    @links_stats.setter
    def links_stats(self, links_stats):
        """
        Sets the links_stats of this GetExtendedCampaignStats.

        :param links_stats: The links_stats of this GetExtendedCampaignStats.
        :type: dict(str, GetExtendedCampaignStatsLinksStats)
        """
        if links_stats is None:
            raise ValueError("Invalid value for `links_stats`, must not be `None`")

        self._links_stats = links_stats

    @property
    def stats_by_domain(self):
        """
        Gets the stats_by_domain of this GetExtendedCampaignStats.

        :return: The stats_by_domain of this GetExtendedCampaignStats.
        :rtype: GetStatsByDomain
        """
        return self._stats_by_domain

    @stats_by_domain.setter
    def stats_by_domain(self, stats_by_domain):
        """
        Sets the stats_by_domain of this GetExtendedCampaignStats.

        :param stats_by_domain: The stats_by_domain of this GetExtendedCampaignStats.
        :type: GetStatsByDomain
        """
        if stats_by_domain is None:
            raise ValueError("Invalid value for `stats_by_domain`, must not be `None`")

        self._stats_by_domain = stats_by_domain

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
        if not isinstance(other, GetExtendedCampaignStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
