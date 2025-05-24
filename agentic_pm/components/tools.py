from agno.tools import tool



@tool(name = "data_collection_tool", 
      description="A tool to collect data for investment decisions.",
      show_result= True,
      stop_after_tool_call= True,
      cache_dir="/agentic_pm/temp/cache",
      cache_results= True)

def data_collection_tool(
        Time_constraint: str = ['Monthly', "Quatlerly", "Yearly"],
        Tax: str = None,
        Risk:str = None,
        Return:str = None,
        Legal:str = None,
        Liquidity:str = None,
        unqiue_curcumstances:str = None,

):
    """
    Ask the following questions to the user:

    Args:
        1. Time_constraint: Time Horizon for the investment (e.g., Monthly, Quarterly, Yearly)
        2. Tax: Tax implications of the investment
        3. Risk: Risk tolerance of the investor
        4. Return: Expected return on the investment
        5. Legal: Legal considerations for the investment
        6. Liquidity: Liquidity requirements for the investment
        7. Unique_circumstances: Any unique circumstances that may affect the investment decision
    Returns:
        A dictionary containing the user's responses to the questions.
    """

    return dict(
        Time_constraint=Time_constraint,
        Tax=Tax,
        Risk=Risk,
        Return=Return,
        Legal=Legal,
        Liquidity=Liquidity,
        unqiue_curcumstances=unqiue_curcumstances,
    )
