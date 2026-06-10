# Install required libraries quietly
!pip install -q langgraph langchain langchain-community transformers torch duckduckgo-search

import os
from typing import TypedDict, List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import HuggingFacePipeline
from