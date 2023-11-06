class TemplateEngine:
    def render(self, template, context):
        return template.replace('{content}', context)
