# -*- coding: utf-8 -*-
#
#
# Copyright (c) 2010 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from zope.interface import Interface

##code-section module-header #fill in your manual code here
from Products.ATContentTypes.content.image import ATImage
from Products.CMFPlone import PloneMessageFactory as _

##/code-section module-header

from config import *

schema = Schema((
    TextField('text',
        required=False,
        searchable=True,
        storage=AnnotationStorage(migrate=True),
        validators=('isTidyHtmlWithCleanup',),
        #validators=('isTidyHtml',),
        default_output_type='text/x-html-safe',
        widget=RichWidget(
            description='',
            label=_(u'label_body_text', default=u'Body Text'),
            rows=15,
            allow_file_upload=False
        ),
    ),
    StringField('external_link',
        searchable=True,
        widget=StringWidget(
            description='',
            label=_(u'label_external_link', default=u'External link')
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SliderImage_schema = ATImage.schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
SliderImage_schema.changeSchemataForField('relatedItems', 'default')
##/code-section after-schema


##code-section HEAD
##/code-section HEAD

class ISliderImage(Interface):
    """Marker interface
    """

class SliderImage(ATImage):
    """
    """
    security = ClassSecurityInfo()

    implements(ISliderImage)

    meta_type = 'SliderImage'
    _at_rename_after_creation = True

    schema = SliderImage_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(SliderImage, PROJECTNAME)

##code-section module-footer #fill in your manual code here
##/code-section module-footer



