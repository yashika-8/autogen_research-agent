import autogen 
from autogen import ConversableAgent
def main():
    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )
    Agent1 = ConversableAgent(
        name="Agent1",
        llm_config={
            "config_list": config_list,
        },
        human_input_mode="NEVER",
        system_message="Your name is Agent1 and you are a stand-up comedian. You will be given a topic and you will generate a joke on that topic."
            "When you're ready to end the conversation, say 'I gotta go' ",
            is_termination_msg=lambda msg: "I gotta go" in msg["content"],
    )
    Agent2 = ConversableAgent(
        name="Agent2",
        llm_config={
            "config_list": config_list,
        },
        human_input_mode="NEVER",
        system_message="Your name is Agent2 and you are a stand-up comedian. "
        "Start the next joke from the punchline of the previous joke."
         "When you're ready to end the conversation, say 'I gotta go' ",
         is_termination_msg=lambda msg: "I gotta go" in msg["content"],
    )
    chat_result = Agent2.initiate_chat(
    recipient=Agent1, 
    message="I'm Agent1. Agent2 let's keep the jokes rolling.",
 
    )
if __name__ == "__main__":
    main()

