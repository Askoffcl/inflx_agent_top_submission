from agent.agent import run_agent

print("AutoStream AI Agent (Offline)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", run_agent(user))
