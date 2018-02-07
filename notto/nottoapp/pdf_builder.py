"""
module to generate the pdf
"""
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict):
    """
    renders a document to pdf using a template
    """
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result,
                            encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
