# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_path, root_handler):
        self.root_node = RouteTrieNode(root_path)
        self.root_node.handler = root_handler

    def insert(self, path_array, handler_to_insert):
        # Traverse through the nodes of the RouteTrie starting from the root
        current_node = self.root_node
        for path_segment in path_array:
            # Call insert for each path segment from the path array - it will be added if needed
            current_node.insert(path_segment)
            # Continue the traversal for the next part of the path
            current_node = current_node.children[path_segment]
        # Add the handler at the deepest node in the path (the leaf)
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


# Represents a node (part of a path) within the RouteTrie
class RouteTrieNode:
    def __init__(self, node_path):
        # Initialize the node with children and a handler
        self.node_path = node_path
        self.children = {}
        self.handler = None

    def insert(self, path_segment):
        # Insert the child path segment if it doesn't already exist
        if path_segment not in self.children:
            self.children[path_segment] = RouteTrieNode(path_segment)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes and define a "not found" handler
        self.routes = RouteTrie('/', root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path_to_add, handler_for_path):
        # Add a handler for a path
        # Split the path and pass the path parts as a list to the RouteTrie
        path_segments = self.split_path(path_to_add)
        self.routes.insert(path_segments, handler_for_path)

    def lookup(self, path_to_lookup):
        # Lookup path (by parts) and return the associated handler
        # Returns "not found" handler if path not found
        path_segments = self.split_path(path_to_lookup)
        lookup_result = self.routes.find(path_segments)
        if lookup_result is None:
            return self.not_found_handler
        return lookup_result

    def split_path(self, path_to_split='', path_delimiter="/"):
        # Splits the provided path
        # Returns an array with the segments of the path to be used by the add_handler and lookup functions

        # Removing specific leading and trailing character:
        # https://stackoverflow.com/questions/42026036/trim-specific-leading-and-trailing-characters-from-a-string

        # Removes the trailing "/" if it is present
        return path_to_split.rstrip(path_delimiter).split(path_delimiter)[1:]


# Create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# Test Cases
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
