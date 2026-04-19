Here are some key ideas from Anthropic's Prompt Engineering to be aware about:

Chain of thought (CoT):
- Getting the model to reason step by step
- Usually good to guide with steps (1,2,3,4)
- Long explanations good for math problems/transparency bias-free

Few-shot prompting:
- Show examples of what you want before asking the real question (basically trains/prepares the model)
- When is it good: formatting outputs (consistent), teaching tone/style when evaluating sentiment (for ex.), complex transformations

System prompts:
- Sets the model behavior upfront: who are you and how should you act?
- Ex. You are a concise, technical assistant. Always answer in bullet points. Avoid speculation. -> Output constraints for optimized result

Where most people go wrong:
- Overusing CoT
- No examples when formatting matters
- Vague prompts/forgetting constraints
