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
from plone.app.blob.content import ATBlob
from plone.i18n.normalizer.interfaces import IUserPreferredFileNameNormalizer
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
            description='Der Text muss immer mit einem H1 umgeben sein (Text markieren -> "Format-Dropdown" -> H1); Für Umbrüche nur weiche Umbrüche benutzen(Shift+Enter)',
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
    BooleanField(
        name='checkheadlinebackground',
        widget=BooleanWidget(
            format='checkbox',
            label='Banner Text Hintergrund',
            description = 'Soll die Überschrift einen transparenten Hintergrund haben?',
        ),
    ),
    StringField(
        required=True,
        name='banner_text_position',
        vocabulary_expr="""content_instance.getAdapter('portal')().getBrowser('easyvoc').get('banner-text-position')""",
        widget=SelectionWidget(
            label='Banner Text Position',
            description = 'Wie soll der Banner Text positioniert werden?',
            i18n_domain='plone',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SliderImage_schema = ATBlob.schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
SliderImage_schema.changeSchemataForField('relatedItems', 'default')
##/code-section after-schema


##code-section HEAD
##/code-section HEAD

class ISliderImage(Interface):
    """Marker interface
    """

class SliderImage(ATBlob):
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
    def _should_set_id_to_filename(self, filename, title):
        form=self.REQUEST.form
        if filename:
            form.update({'title':filename})
            normalize=self.getAdapter('normalize')
            id = normalize(filename)
            if id!=self.getId():
                form.update({'id':id})
        return True


registerType(SliderImage, PROJECTNAME)

##code-section module-footer #fill in your manual code here
##/code-section module-footer



