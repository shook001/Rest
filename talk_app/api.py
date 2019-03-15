from tastypie.resources import ModelResource
from tastypie.constants import ALL
from talk_app.models import Talk
from tastypie import fields
from tastypie.api import Api


class TalkResource(ModelResource):
    class Meta:
        queryset = Talk.objects.all()
        resource_name = 'talk'
        filtering = {'title': ALL}


v1_api = Api(api_name='v1')
v1_api.register(TalkResource())
