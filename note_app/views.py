from django.shortcuts import render, get_object_or_404
import os


def link_convention(html_name):
    return (html_name.replace('_', '-').lower()).rstrip('lmth.')


def zip_of_pages(directory: str):
    index_list = os.listdir('templates/' + directory)
    step = 0
    title_list = []
    link_list = []
    for element in index_list:
        step += 1
        title_list.append((str(step) + '. ' + directory + ' ' + element[4:-5]))
        link_list.append(link_convention(element))
    index_zip = zip(title_list, link_list)
    return index_zip


def homepage(request):
    return render(request, 'homepage.html')


def javascript_section(request):
    return render(request, 'js_index.html', {'js_zip': zip_of_pages('JavaScript')})


js_section_link_and_render_list = []
for javascript_file in os.listdir('templates/JavaScript'):
    def js_section_render(request, js_file=javascript_file, ):
        return render(request, 'JavaScript/' + js_file, {'js_zip': zip_of_pages('JavaScript')})
    js_section_link_and_render_list.append((link_convention(javascript_file), js_section_render))


def j_qery_section(request):
    return render(request, 'jq_index.html', {'jq_zip': zip_of_pages('JQery')})
