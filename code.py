", # wait, key mapping
        route_after_execution,
        {
            "end": END,
            "writer": "writer"
        }
    )

    # Compile the graph
    app = workflow.compile()

    # Run the multi-agent system
    print("Starting Multi-Agent Collaborative Workflow...")
    final_state