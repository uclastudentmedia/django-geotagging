from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

from geotagging.views import add_edit_geotag,kml_feed, kml_feed_map
from geotagging.models import Line, Point, Polygon
from geotagging.forms import PointForm
from geotagging.forms import LineForm
from geotagging.forms import PolygonForm
from geotagging.feeds import feed_dict

urlpatterns = patterns('',
    url(r'^geo_point/(?P<content_type_id>\d*)/(?P<object_id>\d*)/$',add_edit_geotag,
        {"form_class":PointForm, "geotag_class":Point,
         "template":"geotagging/add_edit_point.html"}
        , name="geotagging-add_edit_point"),
    url(r'^geo_line/(?P<content_type_id>\d*)/(?P<object_id>\d*)/$',add_edit_geotag,
        {"form_class":LineForm,"geotag_class":Line,
         "template":"geotagging/add_edit_point.html"}
        , name="geotagging-add_edit_line"),
    url(r'^geo_polygon/(?P<content_type_id>\d*)/(?P<object_id>\d*)/$',add_edit_geotag,
        {"form_class":PolygonForm,"geotag_class":Polygon,
         "template":"geotagging/add_edit_point.html"}
        , name="geotagging-add_edit_polygon"),

    # GeoRSS Feeds
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     {'feed_dict': feed_dict}),


    # Feeds visualiser GoeRSS
    url(r'^point_georss_feed_map/$', direct_to_template,
        {
            "template" : "geotagging/view_georss_feed.html",
            "extra_context" :
                {
                    "google_key" : settings.GOOGLE_MAPS_API_KEY,
                    "georss_feed" : "http://127.0.0.1:8000/geotagging/feeds/georss_point/",
                }
        }),
    url(r'^line_georss_feed_map/$', direct_to_template,
        {
            "template" : "geotagging/view_georss_feed.html",
            "extra_context" :
                {
                    "google_key" : settings.GOOGLE_MAPS_API_KEY,
                    "georss_feed" : "http://127.0.0.1:8000/geotagging/feeds/georss_line/",
                }
        }),

    # KML feeds
    url(r'^kml_feed/(?P<geotag_class_name>[a-z]+)/$',kml_feed,
        name="geotagging-kml_feed"),
    url(r'^kml_feed/(?P<geotag_class_name>[a-z]+)/(?P<content_type_name>[a-z]+)/$',kml_feed,
        name="geotagging-kml_feed_per_contenttype"),
    # Feeds visualiser KML

    url(r'^kml_feed_map/all/$', direct_to_template,
        {
            "template" : "geotagging/view_kml_feeds.html",
            "extra_context" :
                {
                    "google_key" : settings.GOOGLE_MAPS_API_KEY,
                    "kml_feed_point" : "http://127.0.0.1:8000/geotagging/kml_feed/point/",
                    "kml_feed_line" : "http://127.0.0.1:8000/geotagging/kml_feed/line/",
                    "kml_feed_polygon" : "http://127.0.0.1:8000/geotagging/kml_feed/polygon/",
                }
        }),
    url(r'^kml_feed_map/(?P<geotag_class_name>[a-z]+)/$', kml_feed_map,
        name="geotagging-kml_feed_map"),
    url(r'^kml_feed_map/(?P<geotag_class_name>[a-z]+)/(?P<content_type_name>[a-z]+)/$', kml_feed_map,
        name="geotagging-kml_feed_map_per_contenttype"),
)
