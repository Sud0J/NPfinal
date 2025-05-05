def display_message(msg):
    print(f"[Server]: {msg}")

def get_user_input(prompt="> "):
    return input(prompt)

def show_progress(percentage):
    print(f"Transfer Progress: {percentage:.2f}%")

def confirm_action(prompt):
    return input(f"{prompt} (y/n): ").strip().lower() == 'y'
