from django.urls import path
from . import views
import os

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('js/', views.javascript_section, name="js_section"),
    path('jq/', views.j_qery_section, name="jq_section"),
    path('bs/', views.bootstrap_section, name="bs_section"),
]

for js_path in views.js_section_link_and_render_list:
    urlpatterns.append(path('js/' + js_path[0] + '/', js_path[1]))

for jq_path in views.jq_section_link_and_render_list:
    urlpatterns.append(path('jq/' + jq_path[0] + '/', jq_path[1]))

for bs_path in views.bs_section_link_and_render_list:
    urlpatterns.append(path('bs/' + bs_path[0] + '/', bs_path[1]))



# urlpatterns.append(path('js/js2-data-type/', views.javascript_section))
# # for element in os.listdir('templates/JQery'):
# #     urlpatterns.append(path('jq/' + element, index_renderer(renderer_path='JQery', render_element=element), name=element[4:-5]))
# #

