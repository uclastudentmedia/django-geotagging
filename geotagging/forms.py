from django import forms
from django.contrib.gis import admin

from geotagging.models import Point
from geotagging.admin import PointAdmin
from geotagging.models import Line
from geotagging.admin import LineAdmin
from geotagging.models import Polygon
from geotagging.admin import PolygonAdmin

# Getting an instance so we can generate the map widget; also
# getting the geometry field for the model.
admin_instance = PointAdmin(Point, admin.site)
point_field = Point._meta.get_field('point')
# Generating the widget.
PointWidget = admin_instance.get_map_widget(point_field)

# The same pattern is applied for Line to get LineWidget
admin_instance = LineAdmin(Line, admin.site)
line_field = Line._meta.get_field('line')
LineWidget = admin_instance.get_map_widget(line_field)

# The same pattern is applied for Polygon to get PolygonWidget
admin_instance = PolygonAdmin(Polygon, admin.site)
polygon_field = Polygon._meta.get_field('polygon')
PolygonWidget = admin_instance.get_map_widget(polygon_field)

class PointForm(forms.ModelForm):
    point = forms.CharField(widget=PointWidget())
    class Meta:
        model = Point
        exclude = ("content_type","object_id")
    class Media:
        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)

class LineForm(forms.ModelForm):
    line = forms.CharField(widget=LineWidget())
    class Meta:
        model = Line
        exclude = ("content_type","object_id")
    class Media:
        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)

class PolygonForm(forms.ModelForm):
    polygon = forms.CharField(widget=PolygonWidget())
    class Meta:
        model = Polygon
        exclude = ("content_type","object_id")
    class Media:
        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)
