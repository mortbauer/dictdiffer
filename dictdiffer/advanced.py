import difflib
from .dictdiffer import DictDiffer

class AdvancedDictDiffer(DictDiffer):
    def _diff_str(self,first,second,node):
        diff12 = list(difflib.ndiff(first.split('\n'),second.split('\n')))
        yield self.CHANGE,self._join_nodes(node), ('str',diff12,1)

    def _patch_change_str(self,destination,node,changes):
        self._set_nodes(destination,node,''.join(difflib.restore(changes[0],changes[1]+1)))

    def _swap_change_str(self,node,changes):
        return self.CHANGE,node, ('str',changes[0],(1,0)[changes[1]])

