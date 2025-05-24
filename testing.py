from agentic_pm.components.agent import planning_agent



conversation_history = []

while True:
    input_text = input("User: ")
    if input_text.lower() == "exit":
        break
    conversation_history.append(f"User: {input_text}")
    response = planning_agent.run(input_text).content
    actually_response = planning_agent.run(input_text)

    conversation_history.append(f"Agent: {actually_response}")
    print(f"Agent: {response}")

