
# You may find the function every to be useful
# for implementing the resolve method.  
#
# every(predicate_fn, list) returns true if 
# for each item in list, predicate(item) is true.
# 
# Note that there are ways of solving this that do not use empty,
# so if it does not make sense to you, you do not need to use it.
from csp_lib.utils import every


def AC3(csp):
    """AC3(csp) 
    Compute AC3 constraint propagation on a constraint satisfaction problem
    (CSP) instance.
    ------------------------------------------------------------------------
    While YOU ARE NOT REQUIRED TO DO THIS, if we wanted to implement the
    maintaining arc consistency (MAC) algorithm, we could add two other
    arguments:
        queue - Allow a queue to be passed in as opposed to constructing
        one with variables that have constraints with respect to one another
        
        removals - List of values that have been restricted. As variables
        are eliminated, we would need to add to this list by calling
        csp.prune(var, value, removals) which would append to the list. 
    
    We could then call the backtracking algorithm with AC3 as the inference
    algorithm and MAC constraint propagation would work.
    -------------------------------------------------------------------------
    """

    # The CSP class provided method support_pruning which copies
    # the current set of domains to one called curr_domains.
    # All work should be done on curr_domains.
    csp.support_pruning()

    # Write code here.  Write auxillary function revise as well
    q = [(Xi, Xk) for Xi in csp.vars for Xk in csp.neighbors[Xi]]
    while q:
        Xi, Xj = q.pop()
        if revise(csp, Xi, Xj):
            if len(csp.curr_domains[Xi]) == 0:
                return False
            else:
                for Xk in csp.neighbors[Xi]:
                    if Xk != Xj:
                        q.append((Xk, Xi))
    return True

def revise(csp, Xi, Xj):
    "Return true if we remove a value."
    revised = False
    
    # Write code to check revisions, use csp.prune to remove values from
    # a variable.
    for x in csp.curr_domains[Xi][:]:
        if every(lambda y: not csp.constraints(Xi,x,Xj,y), csp.curr_domains[Xj]):
            csp.prune(Xi,x)
            revised = True
    return revised