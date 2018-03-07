# May use later
# Currently apparently there is no use case?
class ListExtender(list):
    """Creates a list subclass that implements all functions of a given class"""

    def extend_method(self,method_name):
        def func_wrapper(self,*args,**kwargs):
            [getattr(item, method_name)(*args,**kwargs) for item in self]
            return self

        return func_wrapper

    def create(cls, cls_name, method_list, return_elements=False):
        """Creates a new extended list class implementing
            the given methods operating on its elements"""

        # # If a class is not passed in, use class of given object as the template
        # if not instanceof(item_type,'type'):
        #     item_type = type(item_type)

        # Define extended methods
        methods = dict((method, extend_method(method)) for method in method_list)

        # Create
        extended_list_cls = type(cls_name,(list,),{})
