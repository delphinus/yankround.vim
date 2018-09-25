import denite.util
from .word import Kind as Word


class Kind(Word):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'yankround'
        self.default_action = 'append'

    def action_delete(self, context):
        for target in context['targets']:
            try:
                self.vim.vars['_yankround_cache'] = [
                    x for x in self.vim.vars['_yankround_cache']
                        if x != target['source__raw']
                ]
            except ValueError as err:
                denite.util.error(self.vim, 'target not found in cache')
