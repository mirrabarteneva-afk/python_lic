from docxtpl import DocxTemplate


line = input().split('/')
doc = DocxTemplate('decree_template.docx')

context = {
    'ruler': line[0], 'item': line[1], 'palace': line[2]
}

doc.render(context)
doc.save('order.docx')