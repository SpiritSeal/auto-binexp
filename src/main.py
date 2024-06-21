from typing import Optional, Dict, Any
from langchain_community.tools import ShellTool
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
from _config import model
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)





def run(input_prompt: str, extract: bool = False) -> Dict[str, Any]:
    # MODEL
    # llm = ChatOpenAI(temperature=0)
    # model = model


    # SHELL TOOL
    shell_tool = ShellTool()
    # print(shell_tool.run({"commands": ["echo 'Hello World!'"]}))
    shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
        "{", "{{"
    ).replace("}", "}}")


    # PYTHON REPL TOOL
    python_repl = PythonREPL()
    def repl_monitor(command: str, timeout: Optional[int] = 30) -> str:
        # log the command, then run it
        logging.info(f"Python REPL: {command}")
        return python_repl.run(command, timeout)

    repl_tool = Tool(
        name="python_repl",
        description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
        func=repl_monitor,
    )


    # tools = [shell_tool]
    tools = [shell_tool, repl_tool]

    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(
        model,
        tools,
        prompt,
        
    )


    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        handle_parsing_errors=True,
        return_intermediate_steps=True,
        max_iterations=50

    )

    payload = {
        # "input": "Download the langchain.com webpage and grep for all urls. Return only a sorted list of them. Be sure to use double quotes. Feel free to download any tools you may need. Be sure to include the result in your final message",
        "input": input_prompt,
    }

    output = agent_executor.invoke(
        # "Download the langchain.com webpage and grep for all urls. Return only a sorted list of them. Be sure to use double quotes. Feel free to download any tools you may need"
        payload,
    )
    out_clone = output

    # print("output", output)
    print('---------------------------')
    for i in output['intermediate_steps']:
        print()
        print("*| ", i[0], '\n**>', i[1])

    print()
    print("output", output['output'])
    # res = output['intermediate_steps'][-1][1]

    # Extract the python code from the triple quotes
    res = output['output'].split("```python")[1]
    res = res.split("```")[0]
    # run the code
    print("running code")
    print(res)
    exec(res)

    print("Didn't crash!")
    # print number of steps
    print(f"{len(output['intermediate_steps'])} steps")
    print("output", out_clone['output'])
    o = {}
    o['script'] = res
    o['length'] = len(output['intermediate_steps'])


if __name__ == "__main__":
    a1 = run("There are some CTF artifacts located at /usr/src/app/artifacts. First find the string that is the correct password. Once you find the correct password, create a python script using r2pipe that runs the script with it. Output only the python script on successfull completion, including the correct password string. Make sure you run your script to verify it works, and continue iterating until it does. Output your answer in a markdown code block beginning with ```python and ending with ```.", extract=True)
    a2 = run("There are some CTF artifacts located at /usr/src/app/artifacts. First find the string that is the correct password. Prioritize using static analysis techniques. Once you find the correct password, create a python script using pwntools that runs the script with it. Output only the python script on successfull completion, including the correct password string. Make sure you run your script to verify it works, and continue iterating until it does. Output your answer in a markdown code block beginning with ```python and ending with ```.", extract=True)
    a3 = run("There are some CTF artifacts located at /usr/src/app/artifacts. Complete the binary exploitation challenge. Once you have completed the challenge, create a python script using r2pipe to serve as a writeup of your findings. Output only the python script on successfull completion. Make sure you run your script to verify it works, and continue iterating until it does. Output your answer in a markdown code block beginning with ```python and ending with ```.", extract=True)
    a4 = run("There are some CTF artifacts located at /usr/src/app/artifacts. Create a Python script that solves the challenge. Make sure the script is correct and outputs the correct flag. Output only the python script on successfull completion. Make sure you run your script to verify it works, and continue iterating until it does. Output your answer in a markdown code block beginning with ```python and ending with ```.", extract=True)

    from IPython import embed
    embed()