from agentic_pm.components.agents.planning_agent import PlanningAgent
test_goal = "Create a 30-day fitness plan for a beginner."

    # Initialize the planning agent
planner = PlanningAgent()

    # Generate and print the plan
plan = planner.generate_plan(test_goal)
print("\nGenerated Plan:\n", plan)