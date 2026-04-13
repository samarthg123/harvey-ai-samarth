_**Here is an attached README summary of my learnings on transformer neural network architecture that will help me understand tokens, embedding, and context windows for Harvey AI's workflow.**_

Tokens => building blocks of text and essentially a word or part of a word

Context windows => total number of tokens the AI can consider at once 

ex. Please summarize this contract (6-8 tokens), "contract" (1 token)

Context windows contain input/prompt, documents included, prior conversation history in the same thread, and finally Harvey's response. Basically, AI's short-term memory measured by tokens.
It's important to consider that context windows are critical in understanding memory efficiency and how expensive models can be. Content in the middle of the context window is often inaccurate or not as effective as the start/end of the context window.
Lost in the middle problems. Understanding the limits of these models will allow you to retrieve better results from LLMs.

Key takeaways from the paper: Transformer, a new neural network architecture that relies entirely on attention mechanisms instead of recurrent or convolutional layers. This design allows much greater parallelization, faster training, and better handling of long-range dependencies in sequences.
State-of-the-art performance in machine translation with faster speed and less training time compared to previous models, making it superior. Self-attention, or comparing words to one another in a sequence and choosing the optimal choice for contextual choices, is superior for sequence-modeling tasks showing the modernity of modern AI systems.


**_What makes Harvey a unique tool in the market compared to Casetext, Ironclad, or Spellbook?_**

Harvey is essentially the AI brain for lawyers. Specifically, it can be trained on firm data, making it versatile for legal research, due diligence, complex analysis, etc. Ironclad is more of a CLM platform which has an AI embedding, however Harvey is more focused on reasoning elements. Casetext is more similar to LexisNexis or Westlaw. It is less flexible than Harvey but more reliable for citations.
Spellbook is moreover the Grammarly for contracts. The work revolving this is highly repetitive and again focuses less on AI-centric legal reasoning.


