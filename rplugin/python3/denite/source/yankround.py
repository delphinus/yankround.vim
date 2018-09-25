import re
import denite.util
from .base import Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'yankround'
        self.kind = 'yankround'

    def gather_candidates(self, context):
        def filter_cache(x):
            match = re.match(r'^(.\d*)\t(.*)', x)
            if not match:
                denite.util.error(self.vim, 'invalid format in cache')
            return {
                'word': match[2],
                'action__regtype': match[1],
                'source__raw': x,
            }
        return list(map(filter_cache, self.vim.vars['_yankround_cache']))
