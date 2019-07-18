# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_path, root_handler):
        self.root_node = RouteTrieNode(root_path)
        self.root_node.handler = root_handler

    def insert(self, path_array, handler_to_insert):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root_node
        for path_segment in path_array:
            current_node.insert(path_segment)
            current_node = current_node.children[path_segment]
        current_node.handler = handler_to_insert

    def find(self, path_array):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root_node
        for path_segment in path_array:
            if path_segment not in current_node.children:
                return None
            current_node = current_node.children[path_segment]
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, node_path):
        # Initialize the node with children as before, plus a handler
        self.node_path = node_path
        self.children = {}
        self.handler = None

    def insert(self, path_segment):
        # Insert the node as before
        if path_segment not in self.children:
            self.children[path_segment] = RouteTrieNode(path_segment)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie('/', root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path_to_add, handler_for_path):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_segments = self.split_path(path_to_add)
        self.routes.insert(path_segments, handler_for_path)

    def lookup(self, path_to_lookup):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_segments = self.split_path(path_to_lookup)
        lookup_result = self.routes.find(path_segments)
        if lookup_result is None:
            return self.not_found_handler
        return lookup_result

    def split_path(self, path_to_split=''):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here

        # Removing specific leading and trailing character:
        # https://stackoverflow.com/questions/42026036/trim-specific-leading-and-trailing-characters-from-a-string
        return path_to_split.rstrip("/").split("/")[1:]


# Here are some test cases and expected outputs you can use to test your implementation
# Create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
