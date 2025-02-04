class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        print(path)
        for dir in path:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir != "." and dir != "":
                stack.append(dir)
        return "/" + "/".join(stack)
            
            