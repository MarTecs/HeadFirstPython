# 从标准库的string模块导入Template类，它支持简单的字符串替换模板
from string import Template


# 注意resp的缺省值
# 这个函数需要一个可选的字符串作为参数，用它来创建一个CGI "Content-type"行，
# 参数缺省值为"text/html"
def start_response(resp="text/html"):
    return ('Content-type: ' + resp + '\n\n')


# 打开模板文件(HTML),读入文件，嵌入所提供的标题
def include_header(the_title):
    """
    这个函数需要一个字符串作为参数，用在HTML页面最前面的标题中，页面本身存储在一个单独的文件
    'templates/header.html'中，可以根据需要替换标题
    :param the_title:
    :return:
    """
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return header.substitute(title=the_title)



def include_footer(the_links):
    with open('teplates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links + '">' + key + '</a>&nbsp;&nbsp;' \
            + '&nbsp;&nbsp;'
    footer = Template(foot_text)
    return footer.substitute(links=link_string)


def start_form(the_url, form_type="POST"):
    return '<form action="' + the_url + '" method="' + form_type + '">'


def end_form(submit_msg="Submit"):
    return '<p></p><input type="submit value="' + submit_msg + '">'


def radio_button(rb_name, rb_value):
    return '<input type="radio" name="' + rb_name + '" value="' + rb_value + '">' \
                + rb_value + '<br />'


def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return u_string


def header(header_text, header_level=2):
    return '<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>'


def para(para_text):
    return '<p>' + para_text + '</p>'
