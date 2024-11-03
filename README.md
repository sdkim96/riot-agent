# RIOT-AGENT

🤖 Agent for League of Legends.

---

## English

### 📜 Project Description
`RIOT-AGENT` is an automated agent designed for retrieving and analyzing data from the popular online game, League of Legends. It aims to provide essential information such as player stats, match history, and champion details to support data-driven decision-making and insights.

### 🦜 Features
- Retrieve player (summoner) information
- Access champion statistics and abilities
- Fetch recent match history and details
- Analyze ranked performance and leaderboard standings
- Gather in-game item details for enhanced strategies

### ⚙️ How it Works?

![Pipeline Diagram](./docs/images/pipeline.png)

1. Get query's intent.
2. Plan main tasks depending on it's intent.
3. Do main tasks cocurrently.
4. If all main tasks finished, Plan sub tasks by using **dynamical planning**
5. Do sub tasks cocurrently.
6. Compiling all data driven from all tasks, and preprocess for final agent answer.
7. Get final answer from agent.

### 📝 Dynamical Planning

Dynamical Planning is that agent dynamically chooses functions in tasks pool.
There are conditions to achieve this.

- Each task function **MUST RETURN VOID** and **HAVE FIXED INPUT PARAMETERS**.

Since LLM-based agent can't decide precisely input parameters and return value, we must let agent choose funtions only.

- Each task function **MUST HAVE ITS DOCSTRING**.

Docstrings is best way to let LLM know what functions do.
In our example, we try LLM first, if exception raises, similarity search for docstring.

### 💼 Difference between Main tasks / Sub tasks

**So what is difference?**

We can derive intents from the user’s query. We assign each intent a number from 1 to 6.
The reason for understanding the intent is to identify pre-checks needed to carry out sub-tasks.

For example, fetching all champion information into `QueryWrapper` is not necessary for sub-tasks.
This task needs to be done beforehand to prepare for the sub-tasks.

Additionally, sub-tasks have limited flexibility in adjusting parameters and detailed actions.
Therefore, main tasks based on the intent are performed to handle these fine-tuned tasks and gather the information required for the sub-tasks.