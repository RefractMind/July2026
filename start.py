#import numpy as np
#import pandas as pd

#from sklearn.modei_selection import train_test_split
#client = anthropic.Anthropic(
 #   api_key=os.environ.get("ANTHROPIC_API_KEY"),
#)

import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}]
)
print(message.content[0].text)