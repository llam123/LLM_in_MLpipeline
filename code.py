# import libary

import pandas as pd
from openai import OpenAI
import re
import time

# read data

file_name = "fall_mbr_address.xlsx"
df = pd.read_excel(file_name)
df["FULL_ADDRESS"] = df["ADDRESS_LINE_PRIMARY"] + ", " + df["ADDRESS_CITY"] + ", " + df["ADDRESS_STATE"] + ", " + df["ADDRESS_ZIP_CODE_BASE"].astype(str)
address_list = df['FULL_ADDRESS'].tolist()

# perplexity access to check number of stories

YOUR_API_KEY = "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"


output_long_redfin = []

counter = 0

for address in address_list:
    counter += 1
    
    # Check if the counter is divisible by 19
    if counter % 19 == 0:
        time.sleep(70)
        
    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant. \
                You search Redfin, Trulia, Realtor.com and Google Street View to answer the question."
            ),
        },
        {
            "role": "user",
            "content": (
                f"You search Redfin to answer the question. \
                The building address is '{address}'. \
                How many stories does this building have?"
            ),
        },
    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    response = client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        #model = "llama-3.1-sonar-small-128k-chat",
        messages=messages,
        max_tokens=2000,
        top_p=0,
    )
    #print(response)

    #extract answer from response
    answer = response.choices[0].message.content

    output_long_redfin.append(answer)

# Store the extracted values from Redfin

number_of_stories_redfin = []
pattern = re.compile(r'(\d+)\s*(?=story|stories)|(\w+)(?= story)|(\w+)(?=-story|-level)|(\w+)\s*(?=of stories)')
matches = [re.search(pattern, building) for building in output_long_redfin] # Extract matches for each element in the list
number_of_stories_redfin = [match.group() if match else None for match in matches] # Extracted results
print(number_of_stories_redfin) # Display the result

# Store the extracted values from Google Street
pattern = re.compile(r'(\d+)\s*(?=story|stories)|(\w+)(?=-story)')

# List to store the extracted values

number_of_stories_googlestreet = []

for building in output_long_googlestreet:
    match = pattern.search(building)
    if match.group(1):  # Match for number before 'stories' or 'stories'
        number_of_stories_googlestreet.append(match.group(1))
        
    elif match.group(2):  # Match for word before '-story'
        number_of_stories_googlestreet.append(match.group(2))

# Merge output from Redfin and Google Street

df_merged = pd.DataFrame({
    'addresses': address_list,
    'num_stories_redfin': number_of_stories_redfin,
    'num_stories_googlestreet': number_of_stories_googlestreet
    
})
df_merged

# Write to new Excel file

df_merged.to_csv("address_num_stories.csv", encoding = 'utf8', index = False)
