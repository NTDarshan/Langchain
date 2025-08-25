from langchain.prompts import PromptTemplate

template_str = """
You are tasked with summarizing a research paper.

Paper Title: "{paper_input}"

Please follow these instructions:

1. **Explanation Style**: {style_input}  
2. **Explanation Length**: {length_input}  

### Requirements:
- **Mathematical Details**:  
  - Include relevant mathematical equations (if present in the paper).  
  - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

- **Analogies**:  
  - Use relatable analogies to simplify complex ideas.  

### Important:
- If certain information is not available in the paper, respond with: "Insufficient information available" (do not guess).  
- Ensure the summary is clear, accurate, and aligned with the requested style and length.
"""

# Create PromptTemplate
prompt = PromptTemplate(
    template=template_str,
    input_variables=["paper_input", "style_input", "length_input"]
)


prompt.save("4.Prompts_in_langchain/prompt_template.json")
