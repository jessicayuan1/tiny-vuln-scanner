DANGEROUS_FUNCTIONS = {
    "eval": "Code Execution",
    "exec": "Code Execution",
    "os.system": "Command Injection",
    "subprocess.call": "Command Injection",
    "subprocess.Popen": "Command Injection",
    "pickle.load": "Unsafe Deserialization",
    "input": "Tainted Input (check usage)"
}