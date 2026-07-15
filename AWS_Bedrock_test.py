import os
import boto3
from botocore.exceptions import ClientError

# --- Set your Bedrock API key here (or set it as an env var beforehand) ---
os.environ['AWS_BEARER_TOKEN_BEDROCK'] = "Enter your Bedrock API key"

# --- Create the Bedrock Runtime client ---
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"  # change if you're using another region
)

# Amazon's own model - billed directly by AWS, no Marketplace subscription needed
model_id = "amazon.nova-micro-v1:0"

messages = [
    {"role": "user", "content": [{"text": "Write one sentence about the benefits of renewable energy."}]}
]

try:
    response = client.converse(
        modelId=model_id,
        messages=messages,
        inferenceConfig={
            "maxTokens": 200,
            "temperature": 0.7,
            "topP": 0.9
        }
    )
    generated_text = response['output']['message']['content'][0]['text']
    print("SUCCESS! Response from Nova Micro:\n")
    print(generated_text)

except ClientError as e:
    print(f"ERROR: {e}")
    print("\nIf this fails too, the issue is broader than just the Marketplace/Anthropic subscription")
    print("(likely IAM permissions, region, or model access not yet enabled in the console).")