import ast
import sys
from rules import DANGEROUS_FUNCTIONS
# print(DANGEROUS_FUNCTIONS)



class VulnerabilityScanner(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Call(self, node):
        func_name = self._get_func_name(node.func)
        if func_name in DANGEROUS_FUNCTIONS:
            issue = {
                "line": node.lineno,
                "function": func_name,
                "risk": DANGEROUS_FUNCTIONS[func_name]
            }
            self.issues.append(issue)
        self.generic_visit(node)

    def _get_func_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return self._get_func_name(node.value) + '.' + node.attr
        return ""

    def report(self):
        if not self.issues:
            print("✅ No known insecure patterns found.")
        for issue in self.issues:
            print(f"[!] {issue['risk']} via `{issue['function']}` on line {issue['line']}")


def main():
    

    if len(sys.argv) != 2:
        print("Usage: python scanner.py <file.py>")
        sys.exit(1)

    target_file = sys.argv[1]
    print(f"🔍 Scanning {target_file}...")
    try:
        with open(target_file, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {target_file}")
        sys.exit(1)

    tree = ast.parse(code, filename=target_file)
    scanner = VulnerabilityScanner()
    scanner.visit(tree)
    scanner.report()


if __name__ == "__main__":
    main()
