<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Automate Your Browser with AI Agents

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-agent-webui)

**My Portfolio** [Here](https://learn.nextwork.org/easygoing_white_heroic_bilberry/portfolio)

**Author:** Kareshma Rajaananthapadmanaban  
**Linkedin:** [Click here](https://www.linkedin.com/in/kareshma-rajaananthapadmanaban/)

**Automating Browser with AI:** [Detailed](https://github.com/KareshmaAnanth/My_Hands-on_Projects/blob/4c2b4df90de86b3c257e6030e4a6a8054c6d57ae/AI%20and%20ML/Browser%20agent%20automation/Browser%20automation%20with%20ai-agent-webui.pdf)

⚠️*GitHub sometimes just fails to preview certain PDFs, but the file is still downloadable and safe*

---

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_tgeryhfgj)

---

## Introducing Today's Project!

In this project, I will demonstrate how to create AI-powered agents that automate browser tasks like searching, filling out forms, and navigating websites. I’m doing this project to learn how to reduce repetitive manual work using automation tools. It’s a hands-on way to explore browser control with AI and improve productivity through smart agents.

### Tools and concepts

Services I used were Amazon Q WebUI, local Chrome instance, and `.env` configuration. Key concepts I learnt include using remote debugging with Chrome, setting environment variables for browser automation, managing authenticated sessions securely, and resolving agent-browser conflicts during automation tasks.


### Project reflection

This project took me approximately 2.5 hours. The most challenging part was fixing the "No module" error, which required editing parts of `webui.py` to get it running. I also hit a browser control error turns out, Chrome keeps background processes that block agent access. The root cause was Chrome's default behavior, which I solved by launching a debug-enabled instance. It was most rewarding to see the agent finally execute real browser actions.


I did this project to learn how to run real browser automation using AI agents and test local workflows with authenticated sites. It aligned perfectly with my goal of exploring practical agent use cases. I now understand how to control browser sessions securely and troubleshoot common setup issues like Chrome blocking agent access.


---

## Development Environment

WebUI is a visual interface that lets me interact with Browser Use without writing code. To retrieve WebUI's code, I need to clone its GitHub repository using Git, navigate into the project folder, and set up a virtual environment. Once the dependencies are installed and the server is running, I can access WebUI in my browser to start automating tasks.

I installed Python, Pip, UV, and Git because they are essential for running and managing WebUI. Python powers the backend, Pip and UV handle package installations, and Git lets me clone the latest WebUI source code. I also checked for PATH issues and upgraded Pip and UV to avoid compatibility problems.

I set up a virtual environment by running `uv venv --python 3.12.3` and activating it with `.venv\Scripts\activate` (or the Windows equivalent). A virtual environment is helpful for isolating dependencies, avoiding version conflicts, and keeping the project clean and reproducible across different setups.


![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_j5k1l6m0)

---

## Configuring My API

An API key is needed because it authorizes WebUI to communicate with external AI services like Gemini via Google AI Studio. It helps WebUI by allowing the agent to send prompts and receive intelligent responses, powering the decision-making behind each browser automation task. Without it, WebUI can't access any AI model to function.

I set up my API key by generating a new one in Google AI Studio. Then I configured WebUI to use it by entering the API Key in the LLM Configuration tab. I also switched the AI Model from OpenAI (default) to Gemini (Google AI Studio's model).

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_p4q5r6s7)

---

## Running The Agent

My first agent's task was to go to google.com, search for "OpenAI", and return the first URL. The agent by default launches Chromium, which is a fast, open-source browser engine used by Chrome and others. It handled the task smoothly, loaded the page, highlighted elements using Playwright, and clicked through automatically completing the task without manual input through AI-powered decision-making.

The agent interacts with the browser by using Playwright to scan the page, highlight clickable elements, and send them to the Gemini AI model for analysis. I can see this when colored boxes appear around links and buttons in real time, showing what the agent is evaluating and clicking as it follows the task prompt step by step.

The Results tab shows a log of the agent’s actions, including the steps it took, decisions made, and the final output in this case, the first URL found for "OpenAI". This is helpful because it lets me verify if the agent completed the task correctly and provides transparency into how the AI interpreted and interacted with the page.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_e7f2g3h4)

---

## Advanced Navigation

I also tried telling the agent to visit a specific project page on NextWork and see what happens when starting the project. It reported that access was restricted and starting the project required a PRO membership. This confirmed that the agent could handle multi-step tasks and recognize access limitations in real-world websites.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_terraform-access-screenshot)

---

## Debugging and Logs

When my agent encounters an error, three common reasons are: the task description is vague or lacks a clear expected output, the website layout is too complex for the agent to navigate or understand properly, or the site has bot protection that blocks automated browsing. These issues prevent the agent from completing the task as intended.

The terminal logs show a detailed, step-by-step trace of the agent’s actions like navigating to pages, locating elements, clicking, or extracting data. This helps me understand exactly what the agent is doing behind the scenes, how it interprets the task, and where it might have run into issues or succeeded during execution.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_m4n5p6q7)

---

## Advanced Browser Configuration

In this project extension, I will configure the agent to use my own browser instead of the default sandboxed one. Using my own browser is useful because it gives the agent access to existing logins, sessions, and cookies, letting it interact with websites as if it were me, meaning it can access content behind authentication walls like LinkedIn, GitHub, or Substack without having to log in from scratch. This allows the agent to perform tasks that require authentication, like accessing LinkedIn or personalized dashboards.


To use your own browser in WebUI, you have to update the `.env` file with your local Chrome setup. The `BROWSER_PATH` setting tells WebUI where to find the Chrome executable on your machine, while the `BROWSER_USER_DATA` setting tells it which user profile to load. This lets the agent access saved sessions and logins. I also changed `KEEP_BROWSER_OPEN` to `false` and set `USE_OWN_BROWSER` to `true` so WebUI knows to launch and control my personal browser instead of a temporary one.


I chose to test my agent with the task: `Go to LinkedIn and search "nextwork" "ai" "project". Ensure that all search terms are enclosed in double quotes. Your task is to like the first post.` The agent was able to perform this action directly in my personal Chrome browser because I had already logged into LinkedIn. This works only if all Chrome windows are fully closed before launching WebUI, ensuring a clean session. I restarted WebUI by running `python webui.py --ip 127.0.0.1 --port 7788` in the terminal, then reloaded `http://127.0.0.1:7788` in my browser. In Browser Settings, I enabled Use Own Browser to make the agent use my existing Chrome profile with cookies and login sessions. This setup allows the agent to access authenticated websites and perform real actions, such as liking a LinkedIn post or sending an email, without being blocked by login walls.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/ai-agent-webui_m8n3p4q9)

---

---
