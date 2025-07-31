password = "hunter2"  # Hardcoded password
api_key = "sk-123456789012345678901234567890123456389012345678"  # OpenAI API key
user_input = input("Enter command: ")
eval(user_input)  # Unsafe eval usage
import os
os.system("rm -rf /")  # Dangerous command execution