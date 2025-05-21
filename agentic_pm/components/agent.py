# from textwrap import dedent
# from typing import Any
# from ..utils import setup_logging
# from ..config import groq_client, Agent
# logger = setup_logging()

# class PlanningAgent:
#     """
#     A class that represents a planning agent which generates a plan based on a given goal.
#     """
#     def __init__(self):
#         logger.info("Planning agent initialized.")
#         self.agent = Agent(
#             model=groq_client,
#             description=dedent(
#                 """
#                 You are a planning agent. Your task is to generate a plan based on the given goal.
#                 The plan should be detailed and actionable.
#                 """
#             ),
#             markdown=True,
#         )

#     def generate_plan(self, goal: str) -> Any:
#         """
#         Generate a plan based on the provided goal.
#         """
#         logger.info(f"Generating plan for goal: {goal}")
#         # self.agent.print_response(goal)
#         return self.agent.run(goal).content


# if __name__ == "__main__":
#     # Example test goal
#     test_goal = "Create a 30-day fitness plan for a beginner."

#     # Initialize the planning agent
#     planner = PlanningAgent()

#     # Generate and print the plan
#     plan = planner.generate_plan(test_goal)
#     print("\nGenerated Plan:\n", plan)
